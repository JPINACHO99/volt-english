// Job interviews topic: reading texts (with explanations) and grammar items
DATA.reading.push(
{id:"job_B1",t:"job",l:"B1",title:"Ten minutes early",
p:["Sara had her first job interview last Monday. The job was in a hotel, and she wanted it very much. The night before, she chose her clothes, printed her CV and looked at the hotel's website.",
"She arrived ten minutes early. While she was waiting, she smiled at the receptionist and said good morning to a man in the corridor. She did not know it, but he was the hotel manager. He watched how she talked to people.",
"In the interview, Sara was nervous and forgot one answer. But at the end the manager said, 'You were polite to everybody, even when you didn't know who they were. That is what we need.' She started work the next week."],
mc:[{q:"What did Sara do the night before the interview?",o:["She visited the hotel","She prepared her clothes, CV and research","She called the manager","She worked at the hotel"],a:1},
{q:"Who was the man in the corridor?",o:["A receptionist","Another candidate","The hotel manager","A guest"],a:2},
{q:"Why did Sara get the job?",o:["Her answers were perfect","She was polite to everyone","She had a lot of experience","She arrived very late"],a:1}],
rm:["The night before, she chose her clothes, printed her CV and looked at the hotel's website.","He watched how she talked to people."],
dis:"The hotel has a swimming pool and two restaurants.",
match:["It describes how she got ready.","It describes something that happened while she was waiting.","It explains the result of the interview."]},

{id:"job_B2",t:"job",l:"B2",title:"The question everyone fears",
p:["Of all the questions asked in job interviews, 'What is your biggest weakness?' is probably the most dreaded. Candidates know that an honest answer could cost them the job, while a dishonest one may sound false. Many choose a disguised strength, such as 'I work too hard', which experienced interviewers have heard hundreds of times.",
"Recruiters say that the purpose of the question is not to catch you out. What they want to see is self-awareness: whether you understand your limitations and are doing something about them. A real weakness, described calmly, is far more convincing than a clever trick.",
"The best answers usually follow a simple pattern. First, name a genuine weakness that is not essential for the job. Then explain how it has affected you in the past, and finally describe what you are doing to improve. A candidate who says they find public speaking difficult, but have joined a course to practise, sounds both honest and determined."],
mc:[{q:"Why do many candidates fear this question?",o:["They don't understand it","An honest answer might harm their chances","Interviewers ask it too often","It is always the first question"],a:1},
{q:"What are recruiters really looking for?",o:["Candidates with no weaknesses","Clever answers","Self-awareness and effort to improve","People who work too hard"],a:2},
{q:"Which weakness would be a good choice, according to the text?",o:["One that is essential for the job","A strength disguised as a weakness","A genuine one that is not central to the job","One you cannot change"],a:2}],
rm:["Many choose a disguised strength, such as 'I work too hard', which experienced interviewers have heard hundreds of times.","The best answers usually follow a simple pattern."],
dis:"Most interviews last between thirty and sixty minutes.",
match:["It explains why candidates find the question difficult.","It reveals the real purpose of the question.","It gives a practical method for answering."]},

{id:"job_C1",t:"job",l:"C1",title:"Interviewing the interviewer",
p:["At the end of almost every interview comes the same moment: 'Do you have any questions for us?' Many candidates, relieved that the ordeal is nearly over, reply that they don't. It is a missed opportunity, and recruiters notice it.",
"A thoughtful question signals genuine interest and, just as importantly, shows that the candidate has been listening. Asking what success would look like after six months, or what the biggest challenge facing the team is, invites the interviewer to imagine you in the role. Questions about salary and holidays, by contrast, are better kept for a later stage.",
"There is a further benefit that candidates often forget. An interview is a two-way process, and the answers can be revealing. An interviewer who struggles to describe the team's goals, or who speaks of constant 'restructuring', may be telling you more about the job than any advertisement ever could."],
mc:[{q:"What does the writer think of candidates who have no questions?",o:["They are being polite","They are wasting a chance to make an impression","They have prepared well","They are usually hired"],a:1},
{q:"Why is asking what success would look like a good question?",o:["It helps the interviewer picture you doing the job","It shows you want a high salary","It shortens the interview","It avoids difficult topics"],a:0},
{q:"What 'further benefit' does the final paragraph mention?",o:["Candidates can negotiate earlier","Interviewers prefer short answers","The answers can help candidates judge the job","Advertisements become unnecessary"],a:2}],
rm:["It is a missed opportunity, and recruiters notice it.","There is a further benefit that candidates often forget."],
dis:"Some companies now record every interview for training purposes.",
match:["It describes a common reaction at the end of an interview.","It suggests the kind of questions to ask and which to avoid.","It points out that the interview also informs the candidate."]},

{id:"job_C2",t:"job",l:"C2",title:"The tyranny of the 'culture fit'",
p:["Few phrases have spread through recruitment as rapidly as 'culture fit'. On the face of it, the idea is unobjectionable: a company naturally wants people who share its values and will thrive in its environment. Yet in practice the term has become dangerously elastic, capable of meaning almost anything an interviewer wishes.",
"All too often, 'fit' turns out to mean familiarity. Interviewers warm to candidates who went to similar universities, share their hobbies or laugh at the same jokes, and then rationalise the preference as a judgement about values. The result is a workforce that looks, thinks and talks alike, and an organisation that mistakes its comfort for cohesion.",
"Some firms have begun to replace the question 'Will this person fit in?' with 'What will this person add?' The shift may sound cosmetic, but it alters what interviewers look for. Instead of rewarding resemblance, it rewards difference that can be put to use, and in a world of rapidly changing problems, an organisation of near-identical minds is less a strength than a vulnerability."],
mc:[{q:"What is the writer's main criticism of 'culture fit'?",o:["It is a new and untested idea","Its meaning has become vague enough to justify personal preferences","Companies should not have values","It is only used by large firms"],a:1},
{q:"According to the second paragraph, what does 'fit' often disguise?",o:["A preference for candidates similar to the interviewer","A need for technical skills","Concern about salaries","A lack of applicants"],a:0},
{q:"Why does the writer consider uniformity a 'vulnerability'?",o:["It increases costs","It makes interviews longer","It leaves an organisation poorly equipped for new problems","It causes conflict between employees"],a:2}],
rm:["Yet in practice the term has become dangerously elastic, capable of meaning almost anything an interviewer wishes.","The shift may sound cosmetic, but it alters what interviewers look for."],
dis:"Remote working has, of course, transformed the way teams communicate.",
match:["It concedes that the original idea is reasonable.","It describes how a judgement can conceal personal bias.","It proposes an alternative question."]}
);

Object.assign(DATA.rexp, {
job_B1:[
 {e:"Paragraph 1: 'she chose her clothes, printed her CV and looked at the hotel's website'.",w:["She looked at the website, not the hotel itself.","","She didn't call anyone.","She started working there after the interview."]},
 {e:"Paragraph 2: 'She did not know it, but he was the hotel manager.'",w:["She smiled at the receptionist; the man was someone else.","Nothing says he was a candidate.","","Guests aren't mentioned."]},
 {e:"Paragraph 3: 'You were polite to everybody… That is what we need.'",w:["She was nervous and forgot one answer.","","Her experience isn't mentioned; it was her first interview.","She arrived ten minutes early."]}],
job_B2:[
 {e:"Paragraph 1: 'an honest answer could cost them the job, while a dishonest one may sound false'.",w:["They understand it; the problem is how to answer.","","Frequency isn't the reason they fear it.","Its position in the interview isn't mentioned."]},
 {e:"Paragraph 2: 'What they want to see is self-awareness… and are doing something about them.'",w:["Everyone has weaknesses; the text asks for a real one.","'A real weakness… is far more convincing than a clever trick.'","","'I work too hard' is criticised as a disguised strength."]},
 {e:"Paragraph 3: 'name a genuine weakness that is not essential for the job'.",w:["It should NOT be essential for the job.","Disguised strengths are criticised in paragraph 1.","","You should describe 'what you are doing to improve'."]}],
job_C1:[
 {e:"Paragraph 1: saying you have no questions 'is a missed opportunity, and recruiters notice it'.",w:["The writer sees it as a mistake, not politeness.","","It suggests a lack of preparation.","It says the opposite: recruiters notice it negatively."]},
 {e:"Paragraph 2: such questions invite 'the interviewer to imagine you in the role'.",w:["","Salary questions are 'better kept for a later stage'.","Length isn't mentioned.","It's a thoughtful question, not a way to avoid topics."]},
 {e:"Paragraph 3: the interviewer's answers 'may be telling you more about the job than any advertisement'.",w:["Negotiation isn't mentioned.","Interviewers' preferences aren't discussed.","","Adverts aren't unnecessary; the answers simply reveal more."]}],
job_C2:[
 {e:"Paragraph 1: the term 'has become dangerously elastic, capable of meaning almost anything an interviewer wishes'.",w:["Its newness isn't the problem; its vagueness is.","","The writer accepts that companies want shared values.","Company size isn't mentioned."]},
 {e:"Paragraph 2: 'fit turns out to mean familiarity' — similar universities, hobbies, jokes.",w:["","Technical skills aren't mentioned.","Salary isn't mentioned.","The number of applicants isn't mentioned."]},
 {e:"Paragraph 3: 'in a world of rapidly changing problems, an organisation of near-identical minds is less a strength than a vulnerability'.",w:["Cost isn't mentioned.","Interview length isn't mentioned.","","It warns about 'comfort', not conflict."]}]
});

DATA.grammar.push(
["mc","B1","job","I ___ in this company for three years now.",["work","am working","have worked","worked"],2,"'For three years now' (until today) needs the present perfect."],
["open","B1","job","I'm interested ___ the job you advertised.",["in"],"'Interested in'."],
["wf","B1","job","I sent my ___ for the job yesterday.","APPLY",["application"],"Noun: apply → application."],
["kt","B1","job","I'm sure I can do this job well.","ABLE","I'm sure I'm ___ this job well.",["able to do"],"'Be able to' + infinitive."],
["mc","B2","job","If I ___ the job, I'll move to Madrid.",["get","will get","got","would get"],0,"First conditional: if + present, will + infinitive."],
["open","B2","job","I look forward ___ hearing from you.",["to"],"'Look forward to' + -ing."],
["wf","B2","job","She was praised for her ___ during the interview.","CONFIDENT",["confidence"],"Noun: confident → confidence."],
["kt","B2","job","'Have you ever led a team?' the interviewer asked me.","HAD","The interviewer asked me if ___ a team.",["I had ever led","I'd ever led"],"Reported question: if + past perfect."],
["mc","C1","job","Had I known about the dress code, I ___ a suit.",["would wear","will have worn","would have worn","wore"],2,"Third conditional: would have + participle."],
["open","C1","job","I'm writing with regard ___ the vacancy for a project engineer.",["to"],"'With regard to' = about."],
["wf","C1","job","The panel was impressed by her ___ to change.","ADAPT",["adaptability"],"Noun: adapt → adaptable → adaptability."],
["kt","C1","job","They will let me know their decision next week.","INFORMED","I will ___ their decision next week.",["be informed of","be informed about"],"Passive: will be informed of."],
["mc","C2","job","Only after the third interview ___ the job.",["I was offered","was I offered","I offered","did I offered"],1,"'Only after…' at the start causes inversion: was I offered."],
["open","C2","job","She was offered the post on the strength ___ her presentation.",["of"],"'On the strength of' = because of."],
["wf","C2","job","His answers were ___ vague, so he wasn't hired.","FRUSTRATE",["frustratingly"],"Adverb: frustrate → frustrating → frustratingly."],
["kt","C2","job","It is unlikely that she will accept the offer.","CHANCES","The ___ accepting the offer are slim.",["chances of her","chances of her actually"],"'The chances of someone doing something are slim' = it is unlikely."]
);

Object.assign(DATA.gopt, {
"I ___ in this company for three years now.":["The present simple doesn't connect a period from the past to now.","The continuous is possible in some contexts, but with 'for three years now' the usual form is the present perfect.","","The past simple suggests you no longer work there, but 'now' says you still do."],
"If I ___ the job, I'll move to Madrid.":["","'Will' doesn't go in the if-clause of a first conditional.","'Got' belongs to the second conditional, which would need 'would move'.","'Would' never goes in the if-clause."],
"Had I known about the dress code, I ___ a suit.":["'Would wear' is for the present; 'Had I known' is about the past.","'Will have worn' is future perfect and doesn't fit a past condition.","","The past simple can't be the result of a third conditional."],
"Only after the third interview ___ the job.":["After 'Only after…' at the start, the main clause needs inversion.","","Active voice: it would mean you offered something.","After 'did', the verb must be in the base form, and here we need the passive."]
});
