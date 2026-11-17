# Source for data/listening5.json — job interview dialogues. Speaker A = man, B = woman.
import json, os, re

D = []
def add(id, l, title, lines, q, gaps):
    D.append({"id": id, "t": "job", "l": l, "title": title, "lines": lines,
              "q": [{"q": a, "a": b, "k": k} for a, b, k in q], "gaps": [{"s": s, "a": a} for s, a in gaps]})

# ---------- B1 ----------
add("job_B1_3", "B1", "A phone call about an interview", [
 ["B", "Hello, is that Daniel Ruiz? This is Maria from Greenline Solar."],
 ["A", "Yes, speaking. Hello!"],
 ["B", "We received your CV for the technician job, and we'd like to invite you for an interview."],
 ["A", "Oh, that's great news. When is it?"],
 ["B", "Is Thursday at eleven o'clock OK for you?"],
 ["A", "Thursday is difficult, because I work in the morning. Is Friday possible?"],
 ["B", "Yes, Friday at eleven is fine. Please bring a copy of your driving licence and your certificates."],
 ["A", "No problem. Where exactly is the office?"],
 ["B", "We're on the second floor of the building next to the train station. Ask for me at reception."],
 ["A", "Perfect. Thank you very much, Maria. See you on Friday."]],
 [("Why does the woman call the man?", "To invite him to an interview for the technician job.", [["interview", "invite"]]),
  ("Why can't he go on Thursday?", "Because he works in the morning.", [["work"], ["morning"]]),
  ("What must he bring to the interview?", "A copy of his driving licence and his certificates.", [["licence", "license"], ["certificate"]]),
  ("Where is the office?", "On the second floor of the building next to the train station.", [["second"], ["station", "train"]])],
 [("We received your ___ for the technician job.", "CV"),
  ("Thursday is difficult, because I work in the ___.", "morning"),
  ("We're on the second floor of the building next to the train ___.", "station")])

add("job_B1_4", "B1", "After the interview", [
 ["A", "Hi, Laura! I've just finished my interview."],
 ["B", "Hi, Tom! How did it go?"],
 ["A", "I think it went well. There were two people, a manager and a woman from human resources."],
 ["B", "What did they ask you?"],
 ["A", "They asked why I wanted to change jobs, and what I know about their company."],
 ["B", "And what did you say?"],
 ["A", "I said I want more responsibility. Luckily, I read about the company on their website last night."],
 ["B", "Well done. Did they say anything about money?"],
 ["A", "Yes, the salary is a bit higher than now, and there are twenty-five days of holiday."],
 ["B", "That sounds really good. When will you know?"],
 ["A", "They'll call me next week. I'm trying not to think about it!"]],
 [("How many people interviewed the man, and who were they?", "Two: a manager and a woman from human resources.", [["two", "2"], ["manager", "human resources"]]),
  ("Why does he want to change jobs?", "Because he wants more responsibility.", [["responsibility"]]),
  ("How did he prepare for the question about the company?", "He read about the company on their website the night before.", [["website", "read"]]),
  ("When will he get an answer?", "Next week, by phone.", [["next week"]])],
 [("I've just finished my ___.", "interview"),
  ("Luckily, I read about the company on their ___ last night.", "website"),
  ("They'll call me next ___.", "week")])

add("job_B1_5", "B1", "Questions at the end", [
 ["B", "So, Mark, that's all from me. Do you have any questions for us?"],
 ["A", "Yes, I have a few. What does a normal day look like in this job?"],
 ["B", "Well, in the morning you visit clients, and in the afternoon you write reports in the office."],
 ["A", "Will I have a company car?"],
 ["B", "Yes, you will. And we pay for your phone too."],
 ["A", "Great. Is there any training at the beginning?"],
 ["B", "Yes. For the first two weeks you'll work with an experienced colleague."],
 ["A", "That's really useful. And when would the job start?"],
 ["B", "At the beginning of next month. We'll tell you our decision by Wednesday."],
 ["A", "Thank you for your time. It was nice to meet you."]],
 [("What does a normal day in the job look like?", "Visiting clients in the morning and writing reports in the office in the afternoon.", [["client"], ["report"]]),
  ("What does the company give the employee, apart from the salary?", "A company car and they pay for his phone.", [["car"], ["phone"]]),
  ("What happens in the first two weeks?", "He works with an experienced colleague.", [["colleague", "experienced"]]),
  ("When will they tell him their decision?", "By Wednesday.", [["wednesday"]])],
 [("Do you have any ___ for us?", "questions"),
  ("In the afternoon you write ___ in the office.", "reports"),
  ("For the first two weeks you'll work with an experienced ___.", "colleague")])

# ---------- B2 ----------
add("job_B2_3", "B2", "Explaining a gap in your CV", [
 ["B", "I notice there's a gap of about a year in your CV. Could you tell me about that?"],
 ["A", "Of course. After my company closed, I decided to take some time to retrain. I did a course in renewable energy installations."],
 ["B", "Was that a full-time course?"],
 ["A", "It was part-time, so I also worked in my uncle's business, mostly helping with electrical repairs."],
 ["B", "I see. And why renewable energy, specifically?"],
 ["A", "Honestly, I could see that most new projects in the region were solar or wind, and I didn't want to be left behind."],
 ["B", "That makes sense. How have you applied what you learned?"],
 ["A", "Last spring I helped design a small solar installation for a farm. It's now producing around forty per cent of their electricity."],
 ["B", "That's impressive. Did you have any problems with the project?"],
 ["A", "The roof was weaker than we expected, so we had to change the mounting system. It delayed us by two weeks, but the client was happy in the end."]],
 [("Why is there a gap in the man's CV?", "His company closed and he took time to retrain with a course in renewable energy installations.", [["closed"], ["course", "retrain"]]),
  ("What else did he do during that year?", "He worked part-time in his uncle's business, mostly on electrical repairs.", [["uncle"]]),
  ("Why did he choose renewable energy?", "Because most new projects in the region were solar or wind and he didn't want to be left behind.", [["solar", "wind", "projects"]]),
  ("What problem did the farm project have, and what was the result?", "The roof was weaker than expected, so they changed the mounting system; it was delayed by two weeks but the client was happy.", [["roof"], ["two weeks", "delay", "happy"]])],
 [("I decided to take some time to ___.", "retrain"),
  ("I didn't want to be left ___.", "behind"),
  ("The roof was ___ than we expected.", "weaker")])

add("job_B2_4", "B2", "Talking about salary", [
 ["B", "Before we finish, I'd like to talk about your salary expectations."],
 ["A", "Sure. Based on my research, similar positions in the area pay between thirty-two and thirty-six thousand."],
 ["B", "Our budget for this role is closer to thirty thousand, I'm afraid."],
 ["A", "I understand. Is there any flexibility, considering that I already have experience with the software you use?"],
 ["B", "There might be a little. We could start at thirty-one and review it after the probation period."],
 ["A", "How long is the probation period?"],
 ["B", "Six months. If everything goes well, you'd also receive an annual bonus."],
 ["A", "What would the bonus depend on?"],
 ["B", "Mainly on the team's results, and on your own objectives, which we'd agree together."],
 ["A", "That sounds fair. Could you send me the details in writing so I can think about it?"],
 ["B", "Of course. You'll have an email by tomorrow."]],
 [("What salary range does the man mention, and how did he get it?", "Between thirty-two and thirty-six thousand, based on his research on similar positions in the area.", [["thirty-two", "32", "thirty-six", "36"], ["research", "similar"]]),
  ("What argument does he use to ask for more money?", "That he already has experience with the software the company uses.", [["software"]]),
  ("What does the woman finally offer?", "To start at thirty-one thousand and review it after the six-month probation period, plus an annual bonus.", [["thirty-one", "31"], ["review", "probation", "bonus"]]),
  ("What does the man ask for at the end?", "For the details in writing so he can think about it.", [["writing", "email"]])],
 [("I'd like to talk about your salary ___.", "expectations"),
  ("Is there any ___, considering that I already have experience?", "flexibility"),
  ("If everything goes well, you'd also receive an annual ___.", "bonus")])

add("job_B2_5", "B2", "A video interview goes wrong", [
 ["A", "Hello? Can you hear me? I think my camera isn't working."],
 ["B", "I can hear you, but I can't see you. Try turning the video off and on again."],
 ["A", "Is that better?"],
 ["B", "Yes, perfect. Don't worry, it happens all the time. Shall we start?"],
 ["A", "Yes, sorry about that. I tested everything this morning."],
 ["B", "No problem at all. So, tell me why you applied for a job that's mostly remote."],
 ["A", "I've worked from home for two years, so I know how to organise myself. And I'd save almost two hours of commuting every day."],
 ["B", "How do you stay in touch with your team when you're not in the office?"],
 ["A", "We have a short video call every morning, and we use a chat app for quick questions. I also try to meet colleagues in person once a month."],
 ["B", "That's a good habit. Remote work can feel lonely sometimes."]],
 [("What technical problem does the man have at the start?", "His camera isn't working, so she can hear him but can't see him.", [["camera", "video", "see"]]),
  ("How does she suggest solving it?", "By turning the video off and on again.", [["off", "on again"]]),
  ("Why does he want a remote job?", "He has worked from home for two years and would save almost two hours of commuting every day.", [["two years", "organise", "organize"], ["commut", "two hours"]]),
  ("How does he stay in touch with his team?", "A short video call every morning, a chat app for quick questions, and meeting colleagues once a month.", [["call"], ["chat", "once a month", "in person"]])],
 [("I think my ___ isn't working.", "camera"),
  ("Don't worry, it happens all the ___.", "time"),
  ("I'd save almost two hours of ___ every day.", "commuting")])

# ---------- C1 ----------
add("job_C1_3", "C1", "A competency-based question", [
 ["B", "Can you give me an example of a time when you had to persuade someone who disagreed with you?"],
 ["A", "Certainly. In my previous role, our site manager wanted to postpone a safety inspection because we were behind schedule."],
 ["B", "And you disagreed?"],
 ["A", "Strongly. We'd just modified the switchboard, and I wasn't comfortable energising it without testing. But rather than simply refusing, I tried to understand his concern, which was the penalty for late delivery."],
 ["B", "So how did you approach it?"],
 ["A", "I proposed splitting the inspection. We tested the modified section that evening, outside working hours, and left the rest for the following week."],
 ["B", "And the outcome?"],
 ["A", "We found a loose connection that could have caused a serious fault. After that, he actually asked me to review the testing plan for the whole project."],
 ["B", "What would you do differently, looking back?"],
 ["A", "I'd raise the issue earlier. If testing had been built into the schedule from the start, the conflict wouldn't have arisen at all."]],
 [("Why did the site manager want to postpone the inspection?", "Because they were behind schedule and he was worried about the penalty for late delivery.", [["behind schedule", "penalty", "late"]]),
  ("How did the man solve the disagreement?", "He proposed splitting the inspection and testing the modified section that evening, outside working hours.", [["split", "evening", "modified section"]]),
  ("What did the test reveal, and how did the manager react?", "A loose connection that could have caused a serious fault; the manager then asked him to review the testing plan for the whole project.", [["loose connection", "fault"], ["review", "testing plan"]]),
  ("What would he do differently now?", "Raise the issue earlier so testing is built into the schedule from the start.", [["earlier", "start", "schedule"]])],
 [("Our site manager wanted to ___ a safety inspection.", "postpone"),
  ("I wasn't comfortable ___ it without testing.", "energising"),
  ("We found a ___ connection that could have caused a serious fault.", "loose")])

add("job_C1_4", "C1", "Panel interview: leadership", [
 ["B", "You'd be managing a team of six, some of whom are older and more experienced than you. How would you handle that?"],
 ["A", "I think the key is not to pretend I know more than they do. I'd spend the first weeks listening, finding out what works and what frustrates them."],
 ["B", "And if someone openly challenged your authority?"],
 ["A", "I'd talk to them privately rather than in front of the team. Often, resistance comes from feeling that their experience isn't being valued, so I'd try to give them real responsibility."],
 ["B", "What if that didn't work?"],
 ["A", "Then I'd be clear about expectations and the consequences of not meeting them. Being respectful doesn't mean avoiding difficult conversations."],
 ["B", "Have you ever had to give negative feedback?"],
 ["A", "Yes, to a technician whose reports were consistently late. I focused on the impact, explaining that clients were complaining, rather than criticising him personally. It turned out he was struggling with the software, so we arranged some training."],
 ["B", "So the problem wasn't really motivation."],
 ["A", "Exactly. That's why I always try to understand the cause before jumping to conclusions."]],
 [("What would the man do in his first weeks as manager?", "Listen and find out what works and what frustrates the team.", [["listen"]]),
  ("How would he deal with someone who openly challenged his authority?", "Talk to them privately and give them real responsibility; if that failed, be clear about expectations and consequences.", [["private"], ["responsibilit", "expectations", "consequences"]]),
  ("How did he give negative feedback to the technician?", "He focused on the impact, explaining that clients were complaining, instead of criticising him personally.", [["impact", "clients", "complain"]]),
  ("What was the real cause of the problem?", "The technician was struggling with the software, so they arranged training.", [["software", "training"]])],
 [("You'd be managing a team of six, some of whom are older and more ___ than you.", "experienced"),
  ("Being respectful doesn't mean avoiding difficult ___.", "conversations"),
  ("I always try to understand the cause before jumping to ___.", "conclusions")])

add("job_C1_5", "C1", "Feedback after a rejection", [
 ["A", "Thanks for calling back. I was hoping to get some feedback on why I wasn't selected."],
 ["B", "Of course. I should say first that it was a very close decision. Your technical answers were excellent."],
 ["A", "That's good to hear. So what tipped the balance?"],
 ["B", "Honestly, the other candidate had more experience managing clients directly, and that's a big part of the role."],
 ["A", "I see. I did mention my client work, but perhaps I didn't give enough detail."],
 ["B", "That's fair. Your examples were mostly about technical problems. Next time, I'd include one about handling a difficult client."],
 ["A", "That's really helpful. Was there anything else?"],
 ["B", "Just one small thing. Some of your answers were quite long. It's worth practising more concise versions."],
 ["A", "I appreciate your honesty. Would you keep my CV in case something else comes up?"],
 ["B", "Definitely. In fact, we may be opening a design position in spring, which might suit you even better."]],
 [("What did the interviewer say about the man's technical answers?", "That they were excellent.", [["excellent"]]),
  ("Why did the company choose the other candidate?", "They had more experience managing clients directly, which is a big part of the role.", [["client"], ["experience"]]),
  ("What two pieces of advice does she give him?", "To include an example about handling a difficult client and to practise more concise answers.", [["difficult client", "client"], ["concise", "long", "shorter"]]),
  ("What opportunity does she mention at the end?", "A design position that may open in spring.", [["design"], ["spring"]])],
 [("I should say first that it was a very ___ decision.", "close"),
  ("So what tipped the ___?", "balance"),
  ("It's worth practising more ___ versions.", "concise")])

# ---------- C2 ----------
add("job_C2_3", "C2", "The curveball question", [
 ["B", "Here's a slightly unusual question. If you joined us and found out after a month that a project you'd inherited was fundamentally flawed, what would you do?"],
 ["A", "I suppose the temptation would be to keep quiet, especially as the new person. But that would only postpone the problem and make it more expensive."],
 ["B", "So you'd go straight to your manager?"],
 ["A", "Not immediately. First I'd want to be sure I wasn't missing something, so I'd quietly check my assumptions with whoever designed it. Coming in as the newcomer and declaring everything wrong is a fairly reliable way to lose allies."],
 ["B", "And if you were right?"],
 ["A", "Then I'd go to my manager with a clear account of the risk, an estimate of what it would cost to fix now versus later, and at least one realistic alternative. Bringing a problem without a proposal just shifts the burden."],
 ["B", "What if your manager told you to carry on regardless?"],
 ["A", "That depends on the nature of the flaw. If it's a matter of efficiency, I'd put my concerns in writing and accept the decision. If it were a safety issue, frankly, I wouldn't sign it off, whatever the consequences for me."],
 ["B", "That's a fairly uncompromising position."],
 ["A", "On safety, I think it has to be. Everything else is negotiable."]],
 [("Why does the man say keeping quiet would be a mistake?", "It would only postpone the problem and make it more expensive.", [["postpone", "expensive"]]),
  ("What would he do before going to his manager, and why?", "Check his assumptions with whoever designed it, because declaring everything wrong as a newcomer would make him lose allies.", [["check", "assumption", "designed"], ["allies", "newcomer"]]),
  ("What three things would he bring to his manager?", "A clear account of the risk, an estimate of the cost of fixing it now versus later, and a realistic alternative.", [["risk"], ["cost", "estimate"], ["alternative", "proposal"]]),
  ("How would his reaction differ between an efficiency problem and a safety problem?", "For efficiency he'd put his concerns in writing and accept the decision; for safety he wouldn't sign it off.", [["writing", "accept"], ["sign", "safety"]])],
 [("A project you'd inherited was fundamentally ___.", "flawed"),
  ("Bringing a problem without a proposal just shifts the ___.", "burden"),
  ("Everything else is ___.", "negotiable")])

add("job_C2_4", "C2", "Two offers on the table", [
 ["A", "I'll be straightforward with you. I've received another offer, and I need to give them an answer by Friday."],
 ["B", "I appreciate you telling us. May I ask what makes it attractive?"],
 ["A", "Partly the salary, which is around ten per cent higher. But mainly it's the chance to lead projects from the outset, rather than joining them halfway through."],
 ["B", "I see. I can't promise to match the figure, but I can certainly go back to the director. As for leading projects, that's something we'd envisaged for the second year."],
 ["A", "Could that be made more concrete? At the moment it's rather vague."],
 ["B", "That's a reasonable request. We could put a review in writing at twelve months, specifically tied to taking over a project of your own."],
 ["A", "That would go a long way. To be honest, I'd prefer to join you. The team impressed me, and your work in storage is exactly where I want to specialise."],
 ["B", "Then let's try to make it work. I'll speak to the director this afternoon and come back to you by Thursday."],
 ["A", "Thank you. I hope you don't feel I'm using the other offer as leverage."],
 ["B", "Not at all. You've been open with us, which is exactly the attitude we're looking for."]],
 [("What is the deadline for the other offer?", "Friday.", [["friday"]]),
  ("What are the two attractions of the other offer?", "A salary around ten per cent higher and, mainly, the chance to lead projects from the outset.", [["ten per cent", "10", "salary"], ["lead", "outset", "beginning"]]),
  ("What does the woman propose to address his concern about leading projects?", "A written review at twelve months tied to taking over a project of his own.", [["review", "writing"], ["twelve", "12", "project"]]),
  ("Why does the man prefer this company?", "The team impressed him and their work in storage is where he wants to specialise.", [["team"], ["storage", "specialis", "specializ"]])],
 [("Rather than joining them ___ through.", "halfway"),
  ("At the moment it's rather ___.", "vague"),
  ("I hope you don't feel I'm using the other offer as ___.", "leverage")])

add("job_C2_5", "C2", "Coaching session before a final interview", [
 ["B", "Let's look at your answer about your biggest failure. You described it well, but you rushed through the part about what you learned."],
 ["A", "I know. I suppose I'm uncomfortable dwelling on mistakes in an interview."],
 ["B", "That's understandable, but it's precisely the part they're interested in. Anyone can describe a failure; what distinguishes candidates is the insight they draw from it."],
 ["A", "So I should spend less time on the story itself?"],
 ["B", "Roughly a third on the situation, a third on what you did, and a third on what changed afterwards. And make the lesson specific. 'I learned to communicate better' is meaningless."],
 ["A", "Fair enough. What I actually learned was to agree on acceptance criteria in writing before starting any design work."],
 ["B", "Much better, because it's concrete and it shows you changed your practice. Now, the other thing is your body language. When you're unsure, you look down at the table."],
 ["A", "I had no idea. I'll try to keep eye contact."],
 ["B", "Don't overcorrect, though. Staring is just as off-putting. Glance away when you're thinking, then come back to them when you deliver the key point."],
 ["A", "That's useful. It's strange how much of this has nothing to do with the actual job."],
 ["B", "Interviews test whether you can do the job, but also whether people want to work with you. Both matter."]],
 [("What was wrong with the man's answer about his biggest failure?", "He rushed through the part about what he learned.", [["rush", "learned", "learnt"]]),
  ("How does the woman suggest dividing the answer?", "A third on the situation, a third on what he did, and a third on what changed afterwards.", [["third"]]),
  ("What specific lesson did he actually learn?", "To agree on acceptance criteria in writing before starting any design work.", [["acceptance criteria", "criteria"], ["writing", "before"]]),
  ("What advice does she give about eye contact?", "Not to overcorrect by staring; glance away when thinking and look back when delivering the key point.", [["stare", "staring", "overcorrect"], ["glance", "key point"]])],
 [("I suppose I'm uncomfortable ___ on mistakes in an interview.", "dwelling"),
  ("What distinguishes candidates is the ___ they draw from it.", "insight"),
  ("Staring is just as ___.", "off-putting")])

# ---- checks: gaps verbatim, keywords present in answer ----
for d in D:
    txt = " ".join(t for _, t in d["lines"])
    for g in d["gaps"]:
        assert g["s"].count("___") == 1 and g["s"].replace("___", g["a"]).rstrip(".?!").lower() in txt.lower(), (d["id"], g["s"])
    for q in d["q"]:
        for grp in q["k"]:
            assert any(w.lower() in q["a"].lower() for w in grp), (d["id"], q["q"], grp)
out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "listening5.json")
json.dump(D, open(out, "w"), ensure_ascii=False, indent=1)
print("ok", len(D))
