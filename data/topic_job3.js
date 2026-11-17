// Job interviews topic, second batch: one more reading text per level (with explanations)
DATA.reading.push(
{id:"job_B1_2",t:"job",l:"B1",title:"The online interview",
p:["Last month Tom had his first online interview. He was happy because he did not need to travel. But he forgot something important: to test his computer before the interview.",
"Five minutes before the start, the camera did not work. Tom tried everything. In the end, he used his phone, but the screen was very small and the sound was bad. He could not hear some questions, and he was embarrassed to ask again and again.",
"He did not get the job. Now Tom always checks his camera, microphone and internet the day before. He also puts a light in front of him and closes the door, so his dog cannot come in. 'An online interview is still a real interview,' he says."],
mc:[{q:"Why was Tom happy at first?",o:["The job paid well","He did not need to travel","He knew the interviewer","The interview was short"],a:1},
{q:"What went wrong?",o:["He arrived late","His dog bit the camera","His camera did not work","He forgot the time"],a:2},
{q:"What does Tom do now before an online interview?",o:["He uses his phone","He tests his equipment the day before","He asks for an interview in person","He asks questions again and again"],a:1}],
rm:["But he forgot something important: to test his computer before the interview.","He also puts a light in front of him and closes the door, so his dog cannot come in."],
dis:"Many companies now have offices in different countries.",
match:["It explains the situation and a mistake.","It describes the problems during the interview.","It tells what he learned."]},

{id:"job_B2_2",t:"job",l:"B2",title:"What your CV says about you",
p:["Recruiters often spend less than ten seconds on a CV before deciding whether to read it properly. In that short time, they are not looking for your life story. They want to see, at a glance, whether you have the experience and skills the job requires.",
"This is why the most common mistakes are also the easiest to avoid. Long paragraphs, unusual fonts and photos taken on holiday all make a CV harder to read. Listing duties, such as 'responsible for reports', is far less convincing than describing results, such as 'reduced report time by 20%'.",
"Another frequent error is sending the same CV to every company. A few minutes spent adapting it to each advertisement, using the same key words that appear in the job description, can make the difference between being invited to an interview and being ignored. Many large companies now use software that filters CVs automatically, so those key words matter more than ever."],
mc:[{q:"What do recruiters want to see quickly?",o:["Your life story","Your hobbies","Whether you have the required experience and skills","Your photo"],a:2},
{q:"Why is 'reduced report time by 20%' better than 'responsible for reports'?",o:["It is shorter","It shows a result, not just a duty","It uses an unusual font","It sounds more modest"],a:1},
{q:"Why should you adapt your CV to each advertisement?",o:["Because companies prefer long CVs","Because software and recruiters look for key words from the job description","Because it is required by law","Because it makes the CV longer"],a:1}],
rm:["They want to see, at a glance, whether you have the experience and skills the job requires.","Another frequent error is sending the same CV to every company."],
dis:"Some people still send their CV by post.",
match:["It describes how recruiters read CVs.","It gives examples of what makes a CV weak.","It explains the importance of adapting a CV."]},

{id:"job_C1_2",t:"job",l:"C1",title:"The silence after the interview",
p:["Few experiences are as unsettling as the wait after an interview. Candidates replay every answer, check their inbox obsessively and interpret each day of silence as a sign of rejection. Yet the delay usually has nothing to do with them.",
"Behind the scenes, hiring decisions tend to move slowly. Several people must agree, budgets need approval and other candidates may still be in the process. A recruiter who promised an answer 'by Friday' may simply be waiting for a manager who is on holiday.",
"Career advisers recommend a single, polite follow-up email about a week after the promised date, followed by patience. Bombarding the company with messages rarely helps and may create the very impression of desperation that candidates fear. Meanwhile, the most useful thing to do is to keep applying elsewhere: a second offer is the best cure for anxiety and, should the first company finally call, a valuable negotiating card."],
mc:[{q:"How do candidates typically interpret a delay?",o:["As a sign they will be hired","As a sign of rejection","As normal administration","As a test of patience"],a:1},
{q:"According to the second paragraph, why are decisions often slow?",o:["Recruiters are lazy","The candidate performed badly","Several people and procedures are involved","Companies want to save money on salaries"],a:2},
{q:"What does the writer recommend while waiting?",o:["Sending frequent reminders","Calling the manager directly","Continuing to apply to other companies","Withdrawing the application"],a:2}],
rm:["Yet the delay usually has nothing to do with them.","A recruiter who promised an answer 'by Friday' may simply be waiting for a manager who is on holiday."],
dis:"Interviews by video have become the norm in many sectors.",
match:["It describes the candidates' anxiety.","It explains the reasons for delays.","It gives practical advice."]},

{id:"job_C2_2",t:"job",l:"C2",title:"The overqualified candidate",
p:["'Overqualified' is one of the more curious reasons for rejection. On the face of it, a candidate who exceeds the requirements ought to be a bargain: more knowledge and experience for the same salary. Yet employers routinely turn such applicants away, and their reasoning, though rarely voiced, is not entirely irrational.",
"The fear is essentially one of flight. A seasoned professional who accepts a modest role, the thinking goes, will grow bored within months and leave as soon as something better appears, taking with them the time and money invested in their training. There may also be a less flattering anxiety: that a subordinate who knows more than their manager will prove difficult to direct.",
"Candidates in this position are therefore advised to address the concern before it is raised. Explaining a deliberate change of direction, a wish for a better balance between work and life, or a genuine interest in the company's field can turn an apparent liability into a reassuring story. What they should avoid is pretending to know less than they do, a strategy that tends to be both transparent and demeaning."],
mc:[{q:"Why might an overqualified candidate seem like 'a bargain'?",o:["They demand a higher salary","They offer more than is required for the same pay","They need less training than the job requires","They are easier to manage"],a:1},
{q:"What is the employer's main fear?",o:["That the candidate will leave once something better appears","That the candidate lacks experience","That training will be too short","That the salary is too high"],a:0},
{q:"What does the writer advise such candidates to avoid?",o:["Explaining their motives","Mentioning work-life balance","Showing interest in the company","Hiding the extent of their knowledge"],a:3}],
rm:["Yet employers routinely turn such applicants away, and their reasoning, though rarely voiced, is not entirely irrational.","Candidates in this position are therefore advised to address the concern before it is raised."],
dis:"Unemployment among graduates has, meanwhile, fallen to a record low.",
match:["It presents an apparent paradox.","It explains what lies behind employers' hesitation.","It suggests how candidates can respond."]}
);

Object.assign(DATA.rexp, {
job_B1_2:[
 {e:"Paragraph 1: 'He was happy because he did not need to travel.'",w:["The salary isn't mentioned.","","Nothing says he knew the interviewer.","The length of the interview isn't mentioned."]},
 {e:"Paragraph 2: 'Five minutes before the start, the camera did not work.'",w:["He was at home; arriving late isn't possible here.","The dog is only mentioned in paragraph 3, as a precaution.","","He knew the time; the problem was technical."]},
 {e:"Paragraph 3: 'Now Tom always checks his camera, microphone and internet the day before.'",w:["Using the phone was his emergency solution, which went badly.","","He still does online interviews; he prepares better.","Asking again and again embarrassed him."]}],
job_B2_2:[
 {e:"Paragraph 1: they want to see 'whether you have the experience and skills the job requires'.",w:["'They are not looking for your life story.'","Hobbies aren't mentioned.","","Holiday photos are given as a mistake."]},
 {e:"Paragraph 2: listing duties 'is far less convincing than describing results'.",w:["Length isn't the reason.","","Unusual fonts are listed as a mistake.","Modesty isn't mentioned."]},
 {e:"Paragraph 3: use 'the same key words that appear in the job description' because software filters CVs.",w:["Long paragraphs are given as a mistake.","","No law is mentioned.","Length isn't the point; matching the advert is."]}],
job_C1_2:[
 {e:"Paragraph 1: candidates 'interpret each day of silence as a sign of rejection'.",w:["They fear the opposite.","","They don't see it as normal; the writer explains that it is.","A test of patience isn't how they interpret it."]},
 {e:"Paragraph 2: 'Several people must agree, budgets need approval and other candidates may still be in the process.'",w:["Laziness isn't suggested.","'The delay usually has nothing to do with them.'","","Salary savings aren't mentioned."]},
 {e:"Paragraph 3: 'the most useful thing to do is to keep applying elsewhere'.",w:["'Bombarding the company with messages rarely helps.'","It recommends a single polite email, not calling the manager.","","Withdrawing isn't suggested."]}],
job_C2_2:[
 {e:"Paragraph 1: 'more knowledge and experience for the same salary'.",w:["The same salary, not a higher one.","","Training is mentioned later as a cost if they leave.","Paragraph 2 suggests they may be harder to direct."]},
 {e:"Paragraph 2: 'The fear is essentially one of flight… leave as soon as something better appears.'",w:["","They have too much experience, not too little.","The fear is losing the training investment, not its length.","Salary isn't the main fear."]},
 {e:"Paragraph 3: avoid 'pretending to know less than they do', which is 'transparent and demeaning'.",w:["Explaining motives is recommended.","Work-life balance is one of the suggested explanations.","Interest in the company's field is recommended.",""]}]
});
