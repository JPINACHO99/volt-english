"""Generate listening audio (mp3) and app icons. Run locally: TTS_ENGINE=kokoro python tools/build_assets.py
Audio is only regenerated for dialogues whose text changed."""
import asyncio, hashlib, json, os, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUDIO = os.path.join(ROOT, "audio")
ICONS = os.path.join(ROOT, "icons")
os.makedirs(AUDIO, exist_ok=True)
os.makedirs(ICONS, exist_ok=True)

EDGE_PAIRS = [("en-GB-RyanNeural", "en-GB-SoniaNeural"), ("en-US-GuyNeural", "en-US-JennyNeural"),
              ("en-AU-WilliamNeural", "en-AU-NatashaNeural"), ("en-IE-ConnorNeural", "en-IE-EmilyNeural"),
              ("en-US-AndrewNeural", "en-GB-LibbyNeural"), ("en-GB-ThomasNeural", "en-US-AriaNeural")]
KOKORO_PAIRS = [(9, 7), (6, 1), (10, 8), (5, 3), (9, 4), (6, 7)]
RATE = {"B1": ("-12%", 0.88), "B2": ("-2%", 0.97), "C1": ("+4%", 1.03), "C2": ("+8%", 1.07)}
ENGINE_VERSION = "1"

_kokoro = None


def kokoro():
    global _kokoro
    if _kokoro is None:
        if os.environ.get("SHERPA_PATH"):
            sys.path.insert(0, os.environ["SHERPA_PATH"])
        import sherpa_onnx  # 1.10.x + kokoro-en-v0_19 (espeak phonemes, no out-of-vocabulary words)
        d = os.environ.get("KOKORO_DIR", "/tmp/kokoro-en-v0_19")
        cfg = sherpa_onnx.OfflineTtsConfig(model=sherpa_onnx.OfflineTtsModelConfig(
            kokoro=sherpa_onnx.OfflineTtsKokoroModelConfig(
                model=d + "/model.onnx", voices=d + "/voices.bin", tokens=d + "/tokens.txt",
                data_dir=d + "/espeak-ng-data"),
            num_threads=2, provider="cpu"))
        _kokoro = sherpa_onnx.OfflineTts(cfg)
    return _kokoro


def synth_line(engine, text, idx, speaker, level, out):
    if engine == "edge":
        import edge_tts
        voice = EDGE_PAIRS[idx % len(EDGE_PAIRS)][0 if speaker == "A" else 1]

        async def run():
            await edge_tts.Communicate(text, voice, rate=RATE[level][0]).save(out)
        asyncio.run(run())
    else:
        import soundfile as sf
        sid = KOKORO_PAIRS[idx % len(KOKORO_PAIRS)][0 if speaker == "A" else 1]
        a = kokoro().generate(text, sid=sid, speed=RATE[level][1])
        sf.write(out, a.samples, a.sample_rate)


def build_dialogue(engine, item, idx, dest):
    with tempfile.TemporaryDirectory() as tmp:
        parts = []
        for n, (spk, text) in enumerate(item["lines"]):
            p = os.path.join(tmp, f"{n}.{'mp3' if engine == 'edge' else 'wav'}")
            synth_line(engine, text, idx, spk, item["l"], p)
            parts.append(p)
        cmd = ["ffmpeg", "-y", "-loglevel", "error"]
        for p in parts:
            cmd += ["-i", p]
        flt = "".join(f"[{i}:a]aresample=24000,apad=pad_dur=0.45[a{i}];" for i in range(len(parts)))
        flt += "".join(f"[a{i}]" for i in range(len(parts))) + f"concat=n={len(parts)}:v=0:a=1[out]"
        cmd += ["-filter_complex", flt, "-map", "[out]", "-ac", "1", "-b:a", "48k", dest]
        subprocess.run(cmd, check=True)


def make_audio():
    items = json.load(open(os.path.join(ROOT, "data", "listening.json"), encoding="utf-8"))
    man_path = os.path.join(AUDIO, "manifest.json")
    manifest = json.load(open(man_path)) if os.path.exists(man_path) else {}
    engine = os.environ.get("TTS_ENGINE", "edge")
    for idx, it in enumerate(items):
        h = hashlib.sha1((ENGINE_VERSION + json.dumps(it["lines"])).encode()).hexdigest()
        dest = os.path.join(AUDIO, it["id"] + ".mp3")
        if manifest.get(it["id"]) == h and os.path.exists(dest):
            continue
        try:
            build_dialogue(engine, it, idx, dest)
        except Exception as e:  # edge-tts blocked or failed: fall back to local model
            if engine == "edge":
                print("edge-tts failed (%s); switching to kokoro" % e, flush=True)
                engine = "kokoro"
                build_dialogue(engine, it, idx, dest)
            else:
                raise
        manifest[it["id"]] = h
        print("audio", it["id"], engine, flush=True)
        json.dump(manifest, open(man_path, "w"), indent=0)


def make_icons():
    from PIL import Image, ImageDraw
    bolt = [(0.56, 0.10), (0.26, 0.56), (0.47, 0.56), (0.40, 0.90), (0.74, 0.42), (0.52, 0.42)]
    for name, size, pad in [("icon-192.png", 192, 0.0), ("icon-512.png", 512, 0.0),
                            ("maskable-512.png", 512, 0.14), ("apple-180.png", 180, 0.0)]:
        path = os.path.join(ICONS, name)
        if os.path.exists(path):
            continue
        s = size * 4
        img = Image.new("RGBA", (s, s), (0, 0, 0, 0))
        d = ImageDraw.Draw(img)
        if pad or name.startswith("apple"):
            d.rectangle([0, 0, s, s], fill=(15, 23, 42, 255))
        else:
            d.rounded_rectangle([0, 0, s - 1, s - 1], radius=int(s * 0.22), fill=(15, 23, 42, 255))
        k = 1 - 2 * pad
        pts = [((pad + x * k) * s, (pad + y * k) * s) for x, y in bolt]
        d.polygon(pts, fill=(250, 204, 21, 255))
        img.resize((size, size), Image.LANCZOS).save(path)


if __name__ == "__main__":
    make_icons()
    if "--icons-only" not in sys.argv:
        make_audio()
