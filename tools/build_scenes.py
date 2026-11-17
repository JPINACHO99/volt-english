"""Draws the 28 speaking scenes (4 per topic) and writes data/scenes_art.js."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scenes_lib import *

SC = {}


def add(topic, cap, art, model):
    SC.setdefault(topic, []).append({"cap": cap, "svg": art, "model": model})


# ================= ENGINEERING =================
add("eng", "A factory floor", svg(
    room("#dfe7f1", "#9aa5b4", 175), rect(0, 20, 400, 8, "#94a3b8"), "".join(rect(30 + i * 90, 20, 4, 155, "#94a3b8") for i in range(5)),
    ceiling_lamp(120, 28, 52, True), ceiling_lamp(300, 28, 52, True),
    conveyor(220, 178, 170), robot_arm(330, 160),
    machine(40, 226), toolbox(170, 244),
    person(150, 244, skin=1, hair=1, top="#1d4ed8", bottom="#1e3a8a", arms=("out", "front"), hat="helmet", vest="#f97316", face="focus", beard=True),
    person(265, 236, skin=3, hair=3, top="#475569", bottom="#1f2937", hairstyle="bun", arms=("hold", "down"), hat="helmet_w", glasses=True, face="neutral", holding=clipboard(259, 160), s=0.92),
), "In this picture I can see the inside of a factory. In the foreground, a worker in a yellow helmet and an orange safety vest is repairing a large machine, probably because one of the lights is red. His toolbox is open on the floor. Behind him, a colleague with glasses is holding a clipboard, so she may be supervising the repair or doing an inspection. On the right there's a robot arm next to a conveyor belt carrying boxes, which suggests the factory is quite modern and automated.")

add("eng", "A construction site", svg(
    sky(), sun(345, 42), cloud(70, 55), cloud(215, 38, 0.8),
    crane(40, 185, 140), bridge_wip(140, 185, 250), rect(0, 185, 400, 75, "#c8b28a"),
    barrier(285, 240, 95), cone(260, 245), cone(30, 240),
    person(205, 242, skin=1, hair=0, top="#0ea5e9", bottom="#334155", hairstyle="pony", arms=("hold", "point"), hat="helmet", vest="#f97316", holding=paper(190, 162, 24, 18, 0, 3)),
    person(120, 238, skin=3, hair=3, top="#64748b", bottom="#1f2937", arms=("hip", "hip"), hat="helmet", vest="#facc15", face="neutral", s=0.9),
), "This picture shows a construction site on a sunny day. In the background there's a tall crane and a bridge that is still being built; one section is clearly missing. In the foreground, a female engineer wearing a helmet and a safety vest is holding a plan and pointing at the bridge, maybe explaining the next stage of the work to her colleague, who is listening with his hands on his hips. There are cones and a barrier, so the area is probably closed to the public.")

add("eng", "An engineering design office", svg(
    room("#eef2f7", "#a3a9b5", 190), window(270, 24, 110, 78, sun=True), whiteboard(20, 26, 120, 76, True, "plan"),
    plant(380, 190, 1.1), clock(200, 40, 13, 3, 30),
    person(120, 214, skin=0, hair=2, top="#16a34a", bottom="#1e293b", hairstyle="long", arms=("type", "type"), sit=True, legs=False, face="focus", glasses=True),
    person(268, 238, skin=2, hair=0, top="#f8fafc", bottom="#334155", arms=("hip", "point"), face="smile", beard=True),
    desk(90, 206, 170, "#d1d5db", "#6b7280"),
    monitor(190, 204, 70, 44, "#0b1220", path("M168 168 h44 M172 168 v-22 h18 v22 M192 168 l8 -26 l8 26", stroke="#38bdf8", sw=1.4)),
    cup(240, 203), paper(70, 195, 20, 14, 10, 2),
), "Here we can see two engineers working in a bright office. A woman with glasses is sitting at a desk and looking carefully at a technical drawing on her computer screen. Her colleague is standing next to her and pointing at something, so perhaps he has noticed a mistake or is suggesting a change to the design. There's a whiteboard with a sketch on the wall and a cup of coffee on the desk. The clock shows half past three, so they're probably in the middle of a busy afternoon.")

add("eng", "Inspecting a wind turbine", svg(
    sky("#9fd3ff", "#e3f2ff", "#86c06c", 200), cloud(40, 40), cloud(250, 60, 0.7),
    turbine(300, 200, 165, 1.3, 20), turbine(70, 200, 110, 0.85, 75), turbine(170, 200, 90, 0.7, 40),
    "".join(rect(i * 40, 200, 30, 3, "#6aa957") for i in range(10)),
    person(150, 248, skin=1, hair=1, top="#ef4444", bottom="#1f2937", arms=("hold", "point"), hat="helmet_w", vest="#a3e635", face="smile", holding=rect(138, 168, 22, 16, "#111827", 2) + rect(140, 170, 18, 12, "#60a5fa")),
    person(220, 246, skin=4, hair=2, top="#334155", bottom="#1e293b", hairstyle="bun", arms=("down", "ear"), hat="helmet_w", vest="#a3e635", face="neutral", holding=phone(232, 146), s=0.95),
), "This picture shows a wind farm in the countryside on a fairly windy day, judging by the clouds. In the foreground, two technicians in white helmets and high-visibility vests are standing near the turbines. The man is holding a tablet and pointing up at one of the blades, perhaps because he has detected a fault. The woman is talking on the phone, maybe reporting the problem or calling for a crane. It looks like a routine inspection, but it could also be a repair.")

# ================= ELECTRICITY =================
add("elec", "An electrician at work", svg(
    room("#fbf3e4", "#c9a77c", 195), ceiling_lamp(250, 0, 48, False), rect(205, 0, 4, 34, "#374151"),
    window(30, 40, 90, 80, sun=True), rect(330, 120, 26, 34, "#f8fafc", 3, 'stroke="#cbd5e1" stroke-width="1.5"') + rect(337, 128, 12, 16, "#e5e7eb", 2),
    ladder(220, 70, 240, 30, "#a16207"),
    person(238, 166, skin=1, hair=1, top="#1d4ed8", bottom="#1e3a8a", arms=("up", "up"), face="focus", s=0.92, beard=True),
    path("M224 50 q-10 18 4 26", stroke="#dc2626", sw=2) + path("M233 48 q8 20 -6 28", stroke="#2563eb", sw=2),
    toolbox(120, 244), rect(150, 236, 40, 6, "#facc15", 2) + text(170, 233, "OFF", 7, "#b91c1c"),
), "In this picture an electrician is working inside a house. He is standing on a ladder and reaching up to the ceiling, where there's a lamp with some wires hanging out, so he is probably installing or repairing the light fitting. His toolbox is on the floor next to the ladder. There's a small sign that says 'off', which suggests he has switched off the power before starting, which is the safe way to do it. It's daytime, so he doesn't need the lamp to see.")

add("elec", "A solar home", svg(
    sky("#a7dcff", "#e6f6ff", "#8fcf74", 205), sun(60, 44, 18), cloud(250, 40, 0.8),
    house(120, 205, 140, 80, "#fef3c7", "#9a3412", True), battery_wall(270, 205), charger(305, 210),
    car(350, 234, "#0ea5e9", True), path("M305 195 q8 26 20 22", stroke="#111827", sw=2.5), tree(40, 210, 0.9),
    person(220, 246, skin=2, hair=3, top="#f59e0b", bottom="#1f2937", arms=("down", "point"), face="smile", s=0.85),
), "This image shows a modern house with solar panels on the roof on a bright, sunny day. Next to the house there's a battery mounted on the wall, which probably stores the energy the panels produce so it can be used at night. An electric car is plugged into a charging point. A man is standing in the garden and pointing at the panels, perhaps showing them to a neighbour. It seems the family produces a large part of its own electricity.")

add("elec", "Repairing power lines after a storm", svg(
    sky("#8ca3b8", "#cdd8e2", "#7a9b6b", 200), cloud(30, 40, 1, "#9aa8b6"), cloud(220, 30, 1.2, "#9aa8b6"), rain(0, 400, 0, 200, 40),
    pylon(300, 205, 165), path("M0 75 Q150 105 300 72 M300 72 Q350 70 400 80", stroke="#1f2937", sw=1.5), path("M0 100 Q100 140 180 175", stroke="#1f2937", sw=1.5),
    tree(70, 210, 0.9, "#3f7d43"), rect(150, 190, 70, 12, "#7a5230", 4, 'transform="rotate(-12 185 196)"'),
    bucket_truck(160, 252, (110, 80)),
    person(110, 118, skin=1, hair=1, top="#f97316", bottom="#1f2937", arms=("up", "out"), hat="helmet", face="focus", s=0.6, legs=False),
    person(60, 250, skin=3, hair=3, top="#facc15", bottom="#1f2937", arms=("ear", "down"), hat="helmet", face="worried", s=0.85, holding=phone(70, 165)),
), "This picture shows a repair crew working after a storm. It's still raining and the sky is grey. A fallen tree branch is lying on the ground near some damaged cables. One worker is standing in the bucket of a crane truck, high up next to the power line, trying to reconnect the cables. On the ground, another worker is talking on the phone and looks worried, perhaps because many homes in the area are without electricity. It looks like a dangerous and stressful job.")

add("elec", "A grid control room", svg(
    room("#1f2a3a", "#334155", 196, "#273449"), screen_wall(20, 20, 360, 110),
    desk(40, 206, 320, "#475569", "#1f2937"),
    person(130, 214, skin=0, hair=4, top="#e2e8f0", bottom="#1e293b", arms=("type", "type"), sit=True, legs=False, face="focus", headphones=True, glasses=True),
    person(270, 214, skin=2, hair=2, top="#0f766e", bottom="#1e293b", hairstyle="bun", arms=("type", "point"), sit=True, legs=False, face="worried"),
    desk(40, 206, 320, "#475569", "#1f2937"), monitor(70, 204, 50, 32, "#0b1220"), monitor(330, 204, 50, 32, "#0b1220"),
    cup(195, 202), clock(370, 150, 10, 2, 0),
), "This picture shows the control room of an electricity company. There's a huge wall of screens displaying graphs, a map of the grid with some warning points, and lists of data. Two operators are sitting at a long desk. The man on the left is wearing a headset, so he's probably talking to technicians in the field. The woman on the right looks concerned and is pointing at one of the screens, maybe because she has seen an alarm. The clock shows two o'clock, and since the room is dark, it's probably the middle of the night.")

# ================= WORK =================
add("work", "A business meeting", svg(
    room("#e9e7f7", "#a9a3c2", 190), whiteboard(230, 30, 140, 92, True, "bars"), clock(60, 46, 15, 9, 0), window(30, 80, 70, 50),
    person(310, 238, skin=4, hair=2, top="#be185d", bottom="#1f2937", hairstyle="long", arms=("down", "point"), face="smile", skirt=True),
    person(130, 214, skin=2, hair=3, top="#1e40af", bottom="#111827", arms=("type", "front"), sit=True, legs=False, tie="#facc15", face="neutral"),
    table(70, 206, 140, "#9a6b47", "#6f4a30"), laptop(110, 204, -1), cup(170, 203),
), "The picture shows a business meeting in an office. A woman is standing in front of a whiteboard with a bar chart and a line going up, so she's probably presenting good results, perhaps sales figures. A man in a suit and tie is sitting at the table with his laptop, listening to her. There's a cup of coffee on the table, and the clock shows nine o'clock, so it's likely the first meeting of the day. The atmosphere seems quite formal but positive.")

add("work", "Working from home", svg(
    room("#fce7f3", "#d6b48c", 192), window(260, 30, 110, 84, sun=True), shelf_items(30, 70, 110), shelf_items(30, 110, 90),
    person(190, 212, skin=1, hair=1, top="#4b5563", bottom="#1e293b", arms=("type", "type"), sit=True, legs=False, headphones=True, face="smile", beard=True),
    desk(110, 206, 170, "#c08a5a", "#8b5e34"), laptop(190, 204, -1), cup(250, 203, "#f8fafc"), plant(130, 203, 0.8), cat(90, 244),
), "In this picture a man is working from home. He's sitting at a wooden desk in front of his laptop and wearing headphones, so he's probably in a video call. He's smiling, so the call seems to be going well. There's a cup of tea next to him, a small plant on the desk and some shelves with books behind him. A cat is lying on the floor. It looks comfortable and relaxed, although the cat might be a distraction during meetings.")

add("work", "A busy open-plan office", svg(
    room("#eef2ff", "#a5b4c8", 190), window(20, 24, 100, 70), window(280, 24, 100, 70), clock(200, 40, 13, 5, 50),
    person(78, 214, skin=0, hair=5, top="#16a34a", bottom="#1e293b", hairstyle="curly", arms=("ear", "type"), sit=True, legs=False, face="laugh", holding=phone(90, 130)),
    person(222, 214, skin=2, hair=3, top="#7c3aed", bottom="#1e293b", arms=("up", "up"), sit=True, legs=False, face="worried"),
    sweat(240, 128), person(330, 238, skin=4, hair=0, top="#0ea5e9", bottom="#1f2937", hairstyle="pony", arms=("hold", "down"), face="neutral", holding=cup(318, 168, "#fff", False)),
    desk(40, 206, 230, "#e5e7eb", "#9ca3af"), monitor(128, 204, 46, 30), monitor(172, 204, 46, 30),
    "".join(paper(250, 172 - i * 5, 26, 30, (i % 3 - 1) * 4, 2) for i in range(6)),
), "This picture shows a busy open-plan office late in the afternoon; the clock says ten to six. On the left, a woman is laughing while she talks on the phone, so it might be a personal call. In the middle, a man has his hands on his head and looks stressed, perhaps because of the huge pile of documents next to him. On the right, a colleague is walking past with a cup of coffee. It shows one of the disadvantages of open offices: it's hard to concentrate with so much going on.")

add("work", "A training session", svg(
    room("#f1f5f9", "#94a3b8", 190), rect(140, 20, 180, 104, "#e2e8f0", 4) + rect(146, 26, 168, 92, "#ffffff") + text(230, 52, "SAFETY FIRST", 13, "#1e3a8a") + path("M170 90 l14 -20 l14 20 z", "#facc15") + text(184, 88, "!", 12) + "".join(rect(214, 70 + i * 9, 80, 3, "#94a3b8") for i in range(4)),
    person(80, 238, skin=3, hair=3, top="#f8fafc", bottom="#1e293b", arms=("down", "point"), face="smile", glasses=True, beard=True, s=0.95),
    chair(160, 212, "#1d4ed8", True), chair(230, 212, "#1d4ed8", True), chair(300, 212, "#1d4ed8", True),
    person(160, 212, skin=1, hair=0, top="#f97316", bottom="#1f2937", hairstyle="pony", arms=("hold", "down"), sit=True, face="focus", s=0.82, holding=paper(150, 168, 18, 14, 0, 2)),
    person(230, 212, skin=4, hair=1, top="#22c55e", bottom="#1f2937", arms=("wave", "down"), sit=True, face="smile", s=0.82),
    person(300, 212, skin=0, hair=2, top="#64748b", bottom="#1f2937", arms=("down", "down"), sit=True, face="closed", s=0.82),
), "In this picture a trainer is giving a safety course to a small group of employees. He's standing next to a screen that says 'Safety first' and pointing at it. Three people are sitting on chairs in front of him. The woman on the left is taking notes, and the man in the middle has his hand up, so he probably wants to ask a question. The man on the right seems to have his eyes closed, so maybe he's bored or tired. It's a typical training session, and not everyone looks equally interested.")

# ================= DAILY LIFE =================
add("daily", "At the market", svg(
    sky("#bde4ff", "#eef8ff", "#d6c3a3", 195), sun(360, 36, 14), cloud(60, 40, 0.8),
    rect(0, 100, 400, 95, "#f3e1c0") + "".join(window(20 + i * 100, 112, 50, 40) for i in range(4)),
    stall(40, 230, 220), produce(70, 180, "apples"), produce(120, 180, "broccoli"), produce(175, 180, "oranges"), produce(225, 180, "cheese"),
    crate(60, 228) + crate(150, 228) + produce(80, 212, "tomatoes"),
    person(150, 178, skin=1, hair=1, top="#16a34a", bottom="#1f2937", arms=("hold", "out"), face="smile", s=0.7, beard=True, legs=False),
    person(320, 246, skin=4, hair=4, top="#c026d3", bottom="#6b21a8", hairstyle="bun", arms=("down", "out"), face="smile", skirt=True, s=0.95),
    rect(334, 200, 24, 22, "#a16207", 4) + path("M336 200 q10 -14 20 0", stroke="#a16207", sw=2), circ(362, 176, 3, "#facc15") + circ(358, 172, 3, "#facc15"),
), "This picture shows a street market on a sunny morning. There's a stall with a red and white awning selling fresh fruit, vegetables and cheese. The stallholder, a man with a beard, is smiling and handing something to a customer. The customer is an elderly woman with a shopping basket, and she's holding out some coins, so she's probably paying. The atmosphere looks friendly, and the food seems fresh and local, which is why many people prefer markets to supermarkets.")

add("daily", "The morning commute", svg(
    sky("#9fb2c4", "#d9e2ea", "#8c9aa6", 200), cloud(20, 40, 1.1, "#a9b6c3"), cloud(240, 30, 1.2, "#a9b6c3"), rain(0, 400, 0, 200, 70),
    rect(0, 70, 400, 130, "#c7cfd8") + "".join(window(15 + i * 80, 90, 40, 50, night=False) for i in range(5)),
    rect(0, 200, 400, 30, "#64748b"), bus(250, 226, "#e11d48"), bus_stop(60, 246),
    person(130, 248, skin=2, hair=3, top="#0f766e", bottom="#1f2937", arms=("down", "front"), face="neutral", s=0.95), umbrella(158, 190, "#7c3aed"),
    person(176, 248, skin=2, hair=0, top="#facc15", bottom="#1d4ed8", hairstyle="pony", arms=("front", "down"), face="smile", s=0.62, skirt=True),
    clock(30, 30, 13, 8, 5),
), "Here we can see a typical weekday morning in the city. It's raining and the sky is grey. A father and his young daughter are standing at a bus stop sharing a purple umbrella, and they're probably on the way to school and work. A red bus is arriving. The clock shows five past eight, so they might be in a hurry. The girl looks quite happy despite the weather, while the father looks a bit tired.")

add("daily", "Sunday in the park", svg(
    sky("#a9dcff", "#ebf7ff", "#8ed175", 175), sun(350, 40, 15), cloud(40, 40, 0.8), tree(60, 180, 1.1), tree(330, 180, 0.9), tree(250, 172, 0.6),
    path("M0 225 Q200 190 400 230 L400 260 L0 260 Z", "#e9d8a6"),
    bench(150, 210), person(185, 186, skin=0, hair=4, top="#64748b", bottom="#1f2937", arms=("hold", "hold"), sit=True, legs=True, face="smile", glasses=True, s=0.8, holding=rect(176, 140, 18, 13, "#dc2626", 1) + rect(185, 140, 1, 13, "#fff")),
    person(300, 246, skin=3, hair=0, top="#ec4899", bottom="#111827", hairstyle="pony", arms=("hip", "front"), face="laugh", s=0.9),
    person(80, 250, skin=1, hair=1, top="#2563eb", bottom="#78716c", arms=("down", "front"), face="smile", s=0.95), dog(130, 252), line(108, 196, 120, 230, "#7c2d12", 1.5),
), "This picture shows a park on a sunny Sunday. An elderly man with glasses is sitting on a bench reading a book, and he looks very relaxed. On the path, a young woman is jogging; she's laughing, so maybe she's listening to something funny. On the left, a man is walking his dog. There are big trees and the sky is clear. It's a peaceful scene that shows how people use parks to rest, exercise and enjoy their free time.")

add("daily", "Moving house", svg(
    sky("#bfe3ff", "#f0f9ff", "#9ca3af", 205), house(250, 205, 130, 90, "#e0f2fe", "#334155"), van(20, 238),
    sofa(150, 214, "#0d9488"),
    person(140, 246, skin=1, hair=1, top="#f97316", bottom="#1e293b", arms=("out", "out"), face="worried", s=0.9, beard=True), sweat(156, 150),
    person(258, 246, skin=2, hair=0, top="#6366f1", bottom="#1f2937", hairstyle="long", arms=("out", "out"), face="laugh", s=0.9),
    box(320, 250, 38, 30, "BOOKS") + box(326, 220, 30, 24, "KITCHEN") + box(170, 254, 34, 18),
    plant(380, 250, 0.9),
), "This picture shows a couple moving house. A white van is parked outside, and they're carrying a green sofa together towards the door of the new house. The man looks exhausted and is sweating, while the woman is laughing, maybe because the sofa is heavier than they expected. There are cardboard boxes labelled 'books' and 'kitchen' on the pavement. Moving is usually stressful, but it can also be exciting because it's a fresh start.")

# ================= COOKING =================
add("cook", "In the kitchen", svg(
    room("#fff7ed", "#b0a08c", 190), wall_tiles(110, 185), window(30, 30, 90, 70, sun=True), shelf_items(260, 60, 110),
    stove(250, 240, True), pan(270, 176, "sauce"), pot(316, 176, True),
    person(160, 246, skin=0, hair=5, top="#f8fafc", bottom="#1f2937", hairstyle="bun", arms=("front", "hold"), face="smile", vest="#dc2626", s=0.98),
    table(60, 220, 120, "#d6a76b", "#9a6b3c"), board(120, 214, produce(110, 210, "tomatoes") + circ(140, 206, 6, "#f5f5dc") + circ(146, 208, 4, "#f5f5dc")), knife(84, 211),
), "The picture shows a woman cooking in a bright kitchen. She's wearing a red apron and smiling, so she's clearly enjoying it. On the worktop there's a chopping board with some tomatoes and garlic, and a knife next to them. On the cooker, a pan of tomato sauce is cooking and there's a pot with steam coming out, maybe with pasta. My guess is she's preparing a pasta dish, perhaps for lunch, since it's sunny outside.")

add("cook", "A family dinner", svg(
    room("#fdf2e2", "#a07850", 190), window(150, 26, 100, 72, night=True), rect(20, 40, 50, 60, "#fcd34d", 4) + rect(24, 44, 42, 52, "#fde68a"),
    person(80, 214, skin=2, hair=1, top="#1d4ed8", bottom="#1f2937", arms=("front", "hold"), sit=True, legs=False, face="laugh", beard=True),
    person(160, 214, skin=2, hair=0, top="#be123c", bottom="#1f2937", hairstyle="long", arms=("hold", "front"), sit=True, legs=False, face="smile"),
    person(240, 220, skin=2, hair=1, top="#16a34a", bottom="#1f2937", arms=("cheer", "hold"), sit=True, legs=False, face="laugh", s=0.75),
    person(320, 214, skin=2, hair=4, top="#7c3aed", bottom="#1f2937", hairstyle="bun", arms=("hold", "front"), sit=True, legs=False, face="smile", glasses=True),
    table(30, 208, 340, "#8b5e3c", "#6b4529", 48, "#fef3c7"),
    plate(80, 202, "#f59e0b") + plate(160, 202, "#84cc16") + plate(240, 202, "#f59e0b") + plate(320, 202, "#84cc16"),
    ell(200, 198, 22, 8, "#c2410c") + candle(130, 202) + candle(275, 202) + glass(108, 204) + glass(345, 204) + bottle(198, 186),
), "This image shows a family having dinner together in the evening; it's dark outside. Four people of different generations are sitting around a table with a tablecloth: probably parents, a child and a grandmother. There's roast chicken in the middle, salad, candles and a bottle of wine, so it may be a special occasion like a birthday. The child has his arm in the air and everyone is laughing, so the atmosphere is warm and cheerful.")

add("cook", "A busy restaurant kitchen", svg(
    room("#e5e7eb", "#9ca3af", 190), wall_tiles(20, 185, "#f1f5f9", "#e2e8f0"), rect(0, 20, 400, 10, "#94a3b8"),
    "".join(paper(30 + i * 34, 34, 26, 30, (i % 2) * 4 - 2, 4) for i in range(5)),
    stove(220, 240, True), pan(242, 176, "egg"), pot(288, 176, True),
    person(140, 244, skin=1, hair=3, top="#ffffff", bottom="#1f2937", arms=("point", "hip"), hat="chef", face="shout", beard=True),
    person(345, 244, skin=3, hair=0, top="#111827", bottom="#111827", hairstyle="pony", arms=("out", "out"), face="worried", s=0.92) + plate(312, 170, "#f59e0b") + plate(378, 170, "#84cc16"),
    person(60, 240, skin=0, hair=2, top="#ffffff", bottom="#1f2937", arms=("front", "front"), hat="chef", face="focus", s=0.8),
), "This picture shows a professional kitchen during a busy service. Lots of orders are hanging at the top, which suggests the restaurant is full. The head chef, a man with a beard and a tall white hat, is shouting and pointing, probably giving instructions or complaining that a dish is late. On the right, a waitress is carrying two plates and looks nervous. In the background, a younger cook is concentrating on her work. It shows how stressful working in a restaurant can be.")

add("cook", "A barbecue with friends", svg(
    sky("#ffd7a8", "#fff1dc", "#86c06c", 190), sun(340, 70, 20), tree(40, 196, 1.0), tree(370, 196, 0.8),
    rect(0, 150, 400, 6, "#a16207") + "".join(rect(i * 22, 120, 6, 70, "#b45309") for i in range(19)),
    grill(200, 242),
    person(200, 216, skin=1, hair=1, top="#0ea5e9", bottom="#1f2937", arms=("front", "out"), face="smile", beard=True, s=0.9, vest="#f8fafc", legs=False),
    person(100, 246, skin=2, hair=0, top="#f43f5e", bottom="#1e293b", hairstyle="long", arms=("hold", "down"), face="laugh", s=0.9, holding=glass(92, 172, "#fbbf24")),
    person(300, 246, skin=3, hair=3, top="#22c55e", bottom="#1e293b", arms=("cheer", "down"), face="laugh", s=0.9, holding=bottle(328, 152, "#92400e")),
), "This picture shows a group of friends having a barbecue in a garden in the late afternoon; the sun is quite low. A man wearing an apron is cooking meat on the grill, and there's smoke coming from it. On each side, a friend is holding a drink, and they're both laughing. One of them is raising his bottle, maybe to make a toast. It looks like a relaxed weekend, and it reminds me of an Argentine asado, where the cooking is part of the fun.")

# ================= FOOTBALL =================
add("foot", "Match day", svg(
    crowd(140, 30), rect(0, 140, 400, 120, "#4ade80") + "".join(rect(i * 50, 140, 25, 120, "#22c55e") for i in range(8)) + line(0, 200, 400, 200, "#f0fdf4", 2),
    goal(150, 172, 110, 52),
    person(206, 170, skin=1, hair=3, top="#facc15", bottom="#111827", arms=("out", "out"), face="focus", s=0.6),
    ball(250, 228, 8),
    person(310, 252, skin=3, hair=3, top="#dc2626", bottom="#ffffff", arms=("down", "front"), face="focus", s=0.95),
    person(80, 250, skin=0, hair=1, top="#111827", bottom="#111827", arms=("down", "up"), face="neutral", s=0.9, holding=card_yellow(108, 136)),
), "This picture shows a professional football match in a full stadium. The stands are packed with fans, some of them waving scarves. A player in a red shirt is about to shoot, and the goalkeeper, in yellow, is ready to dive. On the left, the referee is holding up a yellow card, so perhaps a player has just committed a foul. The atmosphere must be incredibly tense and noisy.")

add("foot", "Playing in the park", svg(
    sky("#b5e3ff", "#eef9ff", "#8fd472", 175), sun(50, 40, 14), tree(330, 180, 1.1), tree(40, 185, 0.8),
rect(110, 222, 14, 10, "#64748b", 2) + rect(180, 222, 14, 10, "#ef4444", 2),
    person(150, 248, skin=2, hair=0, top="#2563eb", bottom="#1e293b", arms=("out", "down"), face="laugh", s=0.7),
    person(230, 248, skin=0, hair=5, top="#f97316", bottom="#1e293b", hairstyle="pony", arms=("cheer", "cheer"), face="laugh", s=0.66, skirt=False),
    ball(186, 244, 7),
), "This picture shows two children playing football in a park on a sunny day. They don't have a real pitch; they've used two bags as goalposts. The boy in blue is about to kick the ball, and the girl in orange has her arms in the air, maybe because she has just scored or is celebrating early. They look very happy. It reminds me that football can be played anywhere, with very little equipment.")

add("foot", "Training in the rain", svg(
    sky("#8ea2b5", "#c9d4de", "#4f9a55", 175), cloud(40, 40, 1.2, "#9fb0c0"), cloud(250, 50, 1.1, "#9fb0c0"), rain(0, 400, 0, 260, 90),
    "".join(cone(70 + i * 55, 232) for i in range(6)),
    person(80, 250, skin=2, hair=3, top="#1e293b", bottom="#1e293b", arms=("point", "hip"), face="shout", s=0.95, hat="cap"),
    person(200, 246, skin=1, hair=1, top="#dc2626", bottom="#111827", arms=("out", "down"), face="worried", s=0.85), sweat(214, 150),
    person(320, 246, skin=4, hair=0, top="#dc2626", bottom="#111827", arms=("down", "out"), face="focus", s=0.85), ball(260, 244, 7),
), "Here we can see a football training session on a cold, rainy day. The players in red are running between orange cones, probably doing a dribbling exercise. On the left, the coach, who is wearing a cap, is shouting and pointing, perhaps telling them to go faster. One of the players looks tired and is sweating. It shows that professional football isn't only about matches; it also involves hard, repetitive work in bad conditions.")

add("foot", "Fans watching a match", svg(
    room("#3b2f2a", "#5b4636", 196, "#4a3a30"), rect(0, 150, 400, 50, "#6b4f3a") + rect(0, 146, 400, 8, "#8b6b4a"),
    tv(200, 100, 150, 80, ball(230, 70, 5) + rect(132, 32, 2, 50, "#fff") + rect(268, 32, 2, 50, "#fff")),
    "".join(rect(28 + i * 26, 120 - (i % 2) * 6, 12, 26 + (i % 2) * 6, ["#92400e", "#14532d", "#1e3a8a"][i % 3], 3) for i in range(4)),
    person(90, 250, skin=1, hair=1, top="#38bdf8", bottom="#1f2937", arms=("cheer", "cheer"), face="laugh", s=0.95, beard=True),
    person(200, 250, skin=3, hair=0, top="#38bdf8", bottom="#1f2937", hairstyle="long", arms=("cheer", "hold"), face="laugh", s=0.92, holding=glass(206, 178, "#fbbf24")),
    person(310, 250, skin=0, hair=4, top="#ef4444", bottom="#1f2937", arms=("up", "up"), face="worried", s=0.95),
), "This picture shows a group of football fans watching a match on a big TV in a bar. Two of them are wearing light blue shirts and celebrating with their arms in the air, so their team has probably just scored. The woman is holding a drink. In contrast, the man in red has his hands on his head and looks disappointed, so he obviously supports the other team. It's a good example of how football brings people together, even rivals.")

# ================= JOB INTERVIEWS =================
add("job", "A job interview", svg(
    room("#e8eefc", "#b9c3d6", 190), window(260, 30, 110, 80, sun=True), clock(70, 50, 16, 9), plant(375, 192, 1.1),
    rect(20, 90, 60, 80, "#1e3a8a", 3) + text(50, 120, "VOLT", 9, "#fff") + text(50, 132, "ENERGY", 7, "#93c5fd"),
    person(150, 244, skin=0, hair=1, top="#7c3aed", bottom="#1e293b", hairstyle="long", arms=("down", "shake"), face="smile"),
    person(262, 244, skin=2, hair=3, top="#1e40af", bottom="#111827", arms=("shake", "down"), tie="#dc2626", face="smile"),
    table(140, 236, 140, "#a8794f", "#7c5535", 26), paper(190, 216, 24, 16, -8, 3), cup(240, 226),
), "This picture shows a job interview in an office. A woman and a man are shaking hands across a table, so the interview is probably either starting or finishing. They're both smiling, which is a good sign. There's a CV on the table and a cup of coffee. The clock shows nine o'clock, so this might be the first interview of the day. The man is wearing a suit and tie, which suggests it's a fairly formal company.")

add("job", "An online interview", svg(
    room("#fce7f3", "#c9a77c", 192), window(40, 30, 90, 70), shelf_items(250, 60, 120), plant(360, 192, 1),
    person(200, 214, skin=1, hair=1, top="#f8fafc", bottom="#1e293b", arms=("type", "front"), sit=True, legs=False, headphones=True, tie="#1e3a8a", face="worried"),
    desk(110, 206, 180, "#c08a5a", "#8b5e34"), laptop(200, 204, -1), cup(265, 203), rect(130, 186, 12, 18, "#111827", 2) + circ(136, 192, 3, "#ef4444"),
    path("M110 40 a10 10 0 0 1 20 0 M114 44 a6 6 0 0 1 12 0", stroke="#ef4444", sw=2) + circ(120, 48, 2, "#ef4444"),
), "Here we can see someone having an online interview from home. The man is wearing a shirt and tie, but we can't see if he's wearing smart trousers, which is a common joke about video calls. He has headphones on and looks a bit worried. There's a red symbol showing a weak signal, so maybe his internet connection is failing at the worst possible moment. A cup of coffee is next to his laptop. It shows that online interviews have their own specific problems.")

add("job", "In the waiting room", svg(
    room("#eef2f7", "#a3a9b5", 190), clock(200, 42, 15, 10, 55), sign(200, 80, "INTERVIEWS", 90),
    rect(300, 120, 90, 70, "#e5e7eb") + person(345, 196, skin=4, hair=0, top="#0ea5e9", bottom="#1f2937", hairstyle="bun", arms=("type", "type"), sit=True, legs=False, face="neutral", s=0.85) + rect(300, 176, 90, 18, "#94a3b8", 3),
    chair(60, 214, "#334155", True), chair(130, 214, "#334155", True), chair(210, 214, "#334155", True),
    person(60, 214, skin=1, hair=3, top="#1e40af", bottom="#111827", arms=("hold", "hold"), sit=True, tie="#dc2626", face="worried", s=0.85, holding=paper(46, 166, 26, 18, 0, 3)),
    person(130, 214, skin=0, hair=2, top="#475569", bottom="#1f2937", hairstyle="long", arms=("front", "hold"), sit=True, face="focus", s=0.85),
    person(210, 214, skin=2, hair=1, top="#16a34a", bottom="#1f2937", arms=("hold", "front"), sit=True, face="smile", s=0.85, beard=True, holding=phone(204, 170)),
    sweat(76, 132), plant(270, 250, 1),
), "This picture shows a waiting room outside an interview room. Three candidates are sitting on chairs, waiting for their turn. The man on the left is reading his notes and looks very nervous; he's even sweating. The woman in the middle seems more focused, perhaps going over her answers in her head. The man on the right is looking at his phone and smiling, so he appears quite relaxed, or maybe he's trying to distract himself. A receptionist is working behind a desk. The clock shows five to eleven, so someone's interview is about to start.")

add("job", "A panel interview", svg(
    room("#f5f3ff", "#a5a1c4", 190), window(160, 24, 90, 64), rect(24, 30, 80, 60, "#ffffff", 3, 'stroke="#cbd5e1" stroke-width="2"') + path("M34 80 l14 -18 l12 10 l14 -22 l20 16", stroke="#16a34a", sw=2),
    person(80, 214, skin=0, hair=4, top="#111827", bottom="#1f2937", arms=("type", "hold"), sit=True, legs=False, face="neutral", glasses=True),
    person(150, 214, skin=3, hair=3, top="#64748b", bottom="#1f2937", arms=("hold", "front"), sit=True, legs=False, face="smile", tie="#1e3a8a"),
    person(220, 214, skin=1, hair=2, top="#be185d", bottom="#1f2937", hairstyle="bob" if False else "long", arms=("front", "type"), sit=True, legs=False, face="focus"),
    table(40, 206, 220, "#6b7280", "#4b5563"), paper(60, 190, 22, 14, 6, 2) + paper(200, 190, 22, 14, -6, 2) + glass(130, 204, "#bae6fd"),
    person(330, 248, skin=2, hair=1, top="#f8fafc", bottom="#334155", arms=("out", "point"), face="smile", s=1.0, tie="#16a34a", beard=True),
), "In this picture a candidate is being interviewed by a panel of three people sitting behind a long table. He's standing up and gesturing as he speaks, so he may be giving a presentation or explaining a project. He looks confident. The interviewers react differently: the man in the middle is smiling, the woman on the right is concentrating and probably taking notes, while the older man with glasses has a neutral expression that's hard to read. Panel interviews can be intimidating because you have to convince several people at once.")

COMPARE2 = {
    "eng": "Compare working in an office with working outdoors. Which suits you better, and why?",
    "elec": "Compare these two jobs in the electricity sector. Which is more stressful, and why?",
    "work": "Compare these two working situations. What makes a workplace stressful or useful?",
    "daily": "Compare these two moments in people's lives. Why is change often stressful?",
    "cook": "Compare cooking under pressure with cooking for pleasure. What are the main differences?",
    "foot": "Compare being a player with being a fan. Which requires more commitment?",
    "job": "Compare waiting for an interview with being interviewed by a panel. Which is harder?",
}

if __name__ == "__main__":
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for t, v in SC.items():
        assert len(v) == 4, t
    js = "// Speaking scenes: hand-drawn SVG illustrations (generated by tools/build_scenes.py)\n"
    js += "DATA.scenes = " + json.dumps(SC, ensure_ascii=False, separators=(",", ":")) + ";\n"
    js += "DATA.compareQ2 = " + json.dumps(COMPARE2, ensure_ascii=False) + ";\n"
    open(os.path.join(root, "data", "scenes_art.js"), "w").write(js)
    html = '<body style="margin:0;background:#334;font:12px sans-serif;color:#fff">' + "".join(
        f'<div style="display:inline-block;margin:4px;width:400px"><div>{t} {i}: {s["cap"]}</div>{s["svg"]}</div>' for t, v in SC.items() for i, s in enumerate(v)) + "</body>"
    open("/home/claude/vtest/sc/all.html", "w").write(html)
    print("scenes", sum(len(v) for v in SC.values()), "bytes", len(js))
