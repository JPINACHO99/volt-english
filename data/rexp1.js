// Reading explanations: e = where the answer is and why; w = why each wrong option is wrong ("" = correct option)
window.DATA = window.DATA || {};
DATA.rexp = DATA.rexp || {};
Object.assign(DATA.rexp, {
// ---------- B1 ----------
eng_B1:[
 {e:"Paragraph 1: 'Every morning she arrives at seven and walks around the machines.'",w:["She writes the report after the repair (paragraph 3), not every morning.","","Repairing happened only yesterday, not every morning.","The technician only appears in the repair, not in her morning routine."]},
 {e:"Paragraph 2: 'One of the machines was making parts that were too big.'",w:["The machine kept working; it made parts that were too big.","Nobody was hurt; the text never mentions an accident.","","Metal is mentioned as the cause (a loose piece), not as something missing."]},
 {e:"Paragraph 3: she changed the checklist 'so the workers will look at that piece every week'.",w:["","No manager is mentioned in the text.","She wants correct parts, not bigger ones; big parts were the problem.","The report isn't described as wrong; she wrote it herself."]}],
elec_B1:[
 {e:"Paragraph 1: 'LED bulbs use much less and they last for many years.'",w:["Size is never mentioned.","","It's the old bulbs that 'get very hot'.","The price of buying them isn't mentioned."]},
 {e:"Paragraph 2: 'Many people leave the television or the computer on all night.'",w:["Washing clothes appears in paragraph 3 as advice, not as a night habit.","Changing bulbs is advice from paragraph 1.","","The bill is mentioned at the end, not as something people do at night."]},
 {e:"Paragraph 3: 'Washing clothes with cold water is cheaper than washing with hot water, and the clothes are clean too.'",w:["The text says the clothes 'are clean too'.","","The machine breaking is never mentioned.","It says the opposite: cold water is cheaper, so it uses less."]}],
work_B1:[
 {e:"Paragraph 1: he 'could sleep one hour more' and 'saved money' by having lunch at home.",w:["His salary isn't mentioned; he saved money on lunch.","","He works from home, not in a new office.","His hours aren't mentioned; in fact he worked later at night."]},
 {e:"Paragraph 2: 'it was difficult to stop working in the evening'.",w:["He still has the job; the text never says he lost it.","The train was a reason he was happy at first, not a problem.","","His kitchen is only mentioned as the place he had lunch."]},
 {e:"Paragraph 3: 'he closes the door at six'.",w:["He goes to the office on Tuesdays and Thursdays, not at six.","Answering emails late was his old problem.","Lunch is mentioned in paragraph 1, with no time given.",""]}],
daily_B1:[
 {e:"Paragraph 1: 'Last year Paul felt tired all the time.'",w:["His job isn't a problem; he went to work every day.","","He did no sport then; walking started in January.","It was the opposite: he got up late."]},
 {e:"Paragraph 2: he 'walks for thirty minutes before breakfast'.",w:["He watches series only at the weekend now.","Buying coffee on the way was his old habit.","","He walks before breakfast; going to work is later."]},
 {e:"Paragraph 3: 'Start with one small thing and continue.'",w:["He says the opposite: don't change everything in one day.","He still watches series, at the weekend.","One o'clock was when he used to go to bed.",""]}],
cook_B1:[
 {e:"Paragraph 1: 'I spent every Sunday at my grandmother's house.'",w:["Only on Sundays, at the grandmother's house.","","It was every week, not once a year.","Holidays are never mentioned."]},
 {e:"Paragraph 2: 'the soup cooked slowly for two hours'.",w:["The text says two hours.","The text says two hours.","","It cooked for two hours, not all day."]},
 {e:"Paragraph 3: 'it was only a little lemon juice at the end'.",w:["","Salt is a normal ingredient she put in the pot, not the secret.","Onions are listed as normal ingredients in paragraph 1.","Carrots are listed as normal ingredients in paragraph 1."]}],
foot_B1:[
 {e:"Paragraph 1: 'we lost three nil, and I was the happiest boy in the world'.",w:["They lost three nil.","It was raining.","","His father took him there; nothing says he was angry."]},
 {e:"Paragraph 2: 'The stadium is small and old.'",w:["","It is small and old.","It is old, and everybody knows everybody, so it isn't empty.","The team is from his town; the stadium isn't described as far."]},
 {e:"Paragraph 3: 'this team is from my town'.",w:["It has never won an important cup.","","His friends ask why he doesn't support a big club.","He contrasts it with 'a big, famous club'."]}],
eng_B1_2:[
 {e:"Paragraph 1: 'People came out of their houses to look at it.'",w:["Nothing suggests fear; the children even ran behind it.","","They clearly noticed: they came out to look.","Nobody else wanted to buy it; only the doctor had a car."]},
 {e:"Paragraph 2: 'The doctor did not know how to repair it, so he asked the village blacksmith.'",w:["The blacksmith had only worked with horses.","","They aren't described as relatives.","The blacksmith worked with horses, but the car didn't need them."]},
 {e:"Paragraph 3: 'Later he opened the first garage in the area.'",w:["The doctor was the car's owner; the blacksmith became a mechanic.","He stayed: his grandson still works there.","","Selling the car is never mentioned."]}],
elec_B1_2:[
 {e:"Paragraph 1: 'At eight o'clock in the evening, all the lights went out.'",w:["The storm was the cause; it didn't end at eight.","","Dinner isn't mentioned at that time.","The phones didn't ring; their batteries were almost empty."]},
 {e:"Paragraph 2: 'the batteries were almost empty'.",w:["The phones worked; the batteries were the problem.","Signal is never mentioned.","","The father found candles; he didn't take the phones."]},
 {e:"Paragraph 3: 'It was the best family evening of the year'; the power returning ended it.",w:["He is sad at midnight, after the storm, not because of danger.","","The candles running out is never mentioned.","Grandmother leaving is never mentioned."]}],
work_B1_2:[
 {e:"Paragraph 1: 'I worked there every Saturday.'",w:["Only on Saturdays.","","It was every Saturday for two years, not only in summer.","It was Saturday, not Sunday."]},
 {e:"Paragraph 2: 'I often gave people the wrong change.'",w:["Starting at six was difficult, but arriving late isn't mentioned.","The writer didn't bake; they cleaned and served customers.","","Washing the trays was a task, not a mistake."]},
 {e:"Paragraph 3: 'I learned to be on time, to work carefully and to talk to people.'",w:["The writer cleaned and served; baking isn't mentioned as a lesson.","","Opening a bakery is never mentioned.","The writer learned to be on time, the opposite of getting up late."]}],
daily_B1_2:[
 {e:"Paragraph 1: 'Farmers from the villages come to sell…'",w:["The supermarket is only mentioned to compare prices.","","Children are never mentioned.","Tourists are never mentioned."]},
 {e:"Paragraph 2: 'I like going early, when it is not crowded.'",w:["It isn't cheaper: prices are a little higher than at the supermarket.","The coffee comes after shopping, and its quality isn't mentioned.","","The woman's hours aren't mentioned."]},
 {e:"Paragraph 3: 'It is where I meet my neighbours and feel part of the town.'",w:["The writer says it is 'not only a place to buy food'.","The writer shops there; they don't work there.","The writer enjoys it, especially early when it is quiet.",""]}],
cook_B1_2:[
 {e:"Paragraph 1: 'because it needs two hours to rise'.",w:["His work is never mentioned.","","The oven takes only twelve minutes.","Everybody helps; he doesn't cook alone."]},
 {e:"Paragraph 2: 'My little sister puts the tomato sauce on the base.'",w:["The writer cuts the vegetables.","The mother chooses the cheese.","","Choosing the film isn't mentioned as her job."]},
 {e:"Paragraph 3: they are never round and sometimes burnt, but 'for us, they are the best pizzas in the world'.",w:["They are never round.","They make them at home; they don't order them.","Only 'sometimes' a little burnt, not always.",""]}],
foot_B1_2:[
 {e:"Paragraph 1: 'If we won, we would be champions.'",w:["It was the most important match of the season, not the first one.","","The rivals are never described as friends.","No famous coach is mentioned."]},
 {e:"Paragraph 2: 'Our coach told us to shoot from far away.'",w:["Passing isn't mentioned.","","The rain didn't stop, and the coach didn't say to wait.","Changing the goalkeeper isn't mentioned."]},
 {e:"Paragraph 3: 'The ball slipped through the goalkeeper's hands and went in.'",w:["The writer shot from outside the area; there was no penalty.","The goalkeeper couldn't hold the ball; he didn't kick it.","","The ball stopping in the mud was a general problem, not the goal."]}]
});
