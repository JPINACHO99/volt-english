// Phrasal verbs for job interviews — tagged "job" (5th field). If a verb already exists at that level, it is only tagged.
(function () {
  const J = [
    // B1
    ["fill in","B1","to complete a form by writing information","Please [fill in] the application form."],
    ["send off","B1","to post or email something to someone","I [sent off] my CV yesterday."],
    ["turn up","B1","to arrive","He [turned up] ten minutes late for the interview."],
    ["dress up","B1","to wear more formal clothes than usual","You don't need to [dress up] for this company."],
    ["hear back","B1","to receive a reply","When will I [hear back] from you?"],
    ["call back","B1","to phone someone again","They promised to [call] me [back] on Monday."],
    ["get on with","B1","to have a good relationship with someone","I [get on with] my colleagues very well."],
    ["look forward to","B1","to feel happy about something that will happen","I [look forward to] hearing from you."],
    ["take on","B1","to employ someone","The company is [taking on] new staff."],
    ["find out","B1","to discover information","[Find out] about the company before the interview."],
    ["sit down","B1","to take a seat","Please [sit down], and we'll begin."],
    ["give up","B1","to stop trying","Don't [give up] if you get a no."],
    ["hand in","B1","to give a document to someone in charge","I [handed in] my application on time."],
    ["write down","B1","to write something on paper","She [wrote down] my phone number."],
    ["work out","B1","to find the answer to a problem","I [worked out] the answer quickly."],
    // B2
    ["follow up","B2","to contact someone again about something","I'll [follow up] with an email next week."],
    ["stand out","B2","to be easy to notice because you are better","Your CV must [stand out] from the rest."],
    ["brush up on","B2","to improve a skill you have not used for a while","I need to [brush up on] my English."],
    ["get across","B2","to communicate an idea successfully","I couldn't [get] my point [across]."],
    ["sum up","B2","to give a short summary","Could you [sum up] your experience in a minute?"],
    ["take over","B2","to take responsibility for something from someone else","I [took over] the project when my manager left."],
    ["deal with","B2","to handle a problem or situation","How do you [deal with] stress?"],
    ["turn down","B2","to refuse an offer","She [turned down] the job because of the salary."],
    ["move on","B2","to leave a job to do something new","After five years, I decided to [move on]."],
    ["step down","B2","to leave an important position","The director [stepped down] in March."],
    ["lay off","B2","to stop employing someone because there is no work","The factory [laid off] fifty workers."],
    ["put forward","B2","to suggest an idea or a person","My boss [put] me [forward] for the role."],
    ["pick up","B2","to learn something without formal study","I [picked up] some German while working there."],
    ["back up","B2","to give evidence that supports a claim","[Back up] your answers with examples."],
    ["carry out","B2","to do a task or piece of work","I [carried out] several site inspections."],
    // C1
    ["come across","C1","to give a particular impression","You [come across] as very confident."],
    ["play down","C1","to make something seem less important","Don't [play down] your achievements."],
    ["talk up","C1","to describe something as better than it is","He [talked up] his role in the project."],
    ["draw on","C1","to use your knowledge or experience","I can [draw on] ten years of experience."],
    ["map out","C1","to plan something in detail","I've [mapped out] my career for the next five years."],
    ["run through","C1","to explain or practise something quickly","Let me [run through] the main points of my CV."],
    ["iron out","C1","to solve small problems","We [ironed out] the details of the contract."],
    ["weed out","C1","to remove unsuitable people or things","The test [weeds out] weak candidates."],
    ["narrow down","C1","to reduce the number of options","They [narrowed] the list [down] to three."],
    ["head up","C1","to lead a team or department","She [heads up] the design team."],
    ["follow through","C1","to complete something you started","He always [follows through] on his promises."],
    ["take up","C1","to accept an offer","I'd like to [take up] your offer."],
    ["take in","C1","to understand and remember information","There was too much information to [take in]."],
    ["bring up","C1","to mention a subject","When should I [bring up] the salary?"],
    ["fall through","C1","to fail to happen","The offer [fell through] at the last minute."],
    // C2
    ["hold out for","C2","to wait until you get what you want","I'm [holding out for] a better offer."],
    ["fob off","C2","to give someone an unsatisfactory answer to make them go away","They [fobbed] me [off] with vague promises."],
    ["gloss over","C2","to avoid dealing with something in detail","Don't [gloss over] the gap in your CV."],
    ["sound out","C2","to find out what someone thinks, informally","The headhunter [sounded] me [out] about the role."],
    ["bow out","C2","to withdraw from something","I [bowed out] of the process after the second round."],
    ["home in on","C2","to focus closely on something","The panel [homed in on] my leadership experience."],
    ["rule out","C2","to decide that something is not possible","They haven't [ruled out] an internal candidate."],
    ["hammer out","C2","to reach an agreement after long discussion","We [hammered out] the terms of the contract."],
    ["pass over","C2","to ignore someone for a promotion","He was [passed over] for promotion twice."],
    ["butter up","C2","to praise someone too much to get something","Don't try to [butter up] the interviewer."],
    ["stumble over","C2","to make mistakes when speaking","I [stumbled over] the question about my weaknesses."],
    ["churn out","C2","to produce large amounts without much care","Some candidates [churn out] identical applications."],
    ["bank on","C2","to depend on something happening","Don't [bank on] getting a counter-offer."],
    ["lure away","C2","to persuade someone to leave one place, often with an offer","A rival firm tried to [lure] her [away]."],
    ["string along","C2","to deceive someone by keeping them waiting","They [strung] me [along] for weeks."]
  ];
  J.forEach((p) => {
    const ex = DATA.phrasal.find((x) => x[0] === p[0] && x[1] === p[1]);
    if (ex) ex[4] = 'job'; else DATA.phrasal.push(p.concat('job'));
  });
})();
