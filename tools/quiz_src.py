# General knowledge quiz source → data/quiz.js. Each: (level, cat, question, [options, correct first], explanation)
import json, os

Q = []
def add(l, c, rows):
    for q, opts, e in rows:
        Q.append([l, c, q, opts, e])

# ================= B1 =================
add("B1", "geo", [
 ("What is the capital of Australia?", ["Canberra", "Sydney", "Melbourne", "Perth"], "Canberra was built as a compromise, because both Sydney and Melbourne wanted to be the capital."),
 ("Which is the longest river in South America?", ["The Amazon", "The Paraná", "The Orinoco", "The Magdalena"], "The Amazon is about 6,400 km long and carries more water than any other river."),
 ("How many continents are there in the model usually taught in English-speaking countries?", ["Seven", "Five", "Six", "Eight"], "In English the usual list is seven: Africa, Antarctica, Asia, Australia (Oceania), Europe, North America and South America. Spanish schools often teach five or six."),
 ("Which ocean is the largest?", ["The Pacific", "The Atlantic", "The Indian", "The Arctic"], "The Pacific covers about a third of the Earth's surface."),
 ("In which country is Machu Picchu?", ["Peru", "Bolivia", "Chile", "Ecuador"], "Machu Picchu is a 15th-century Inca city high in the Andes of Peru."),
 ("What is the highest mountain in the world above sea level?", ["Everest", "K2", "Kilimanjaro", "Aconcagua"], "Everest is about 8,849 metres high. Aconcagua is the highest outside Asia."),
 ("Which is the largest hot desert in the world?", ["The Sahara", "The Gobi", "The Atacama", "The Kalahari"], "The Sahara is the largest HOT desert. Antarctica, a cold desert, is even bigger."),
 ("Which city is known as 'the Big Apple'?", ["New York", "Los Angeles", "Chicago", "Boston"], "'The Big Apple' is a popular nickname for New York City."),
])
add("B1", "hist", [
 ("Who was the first person to walk on the Moon?", ["Neil Armstrong", "Yuri Gagarin", "Buzz Aldrin", "Michael Collins"], "Armstrong stepped onto the Moon in July 1969. Gagarin was the first person in space, in 1961."),
 ("In which year did the Berlin Wall fall?", ["1989", "1979", "1985", "1991"], "The Wall fell in November 1989, and Germany was reunified in 1990."),
 ("Which ancient civilisation built the pyramids of Giza?", ["The Egyptians", "The Romans", "The Greeks", "The Aztecs"], "They were built about 4,500 years ago as tombs for Egyptian pharaohs."),
 ("In which year did Christopher Columbus first reach the Americas?", ["1492", "1512", "1453", "1588"], "Columbus landed in the Caribbean in October 1492."),
 ("Which ship sank in 1912 after hitting an iceberg?", ["The Titanic", "The Lusitania", "The Britannic", "The Mayflower"], "The Titanic sank on its first voyage, from Southampton to New York."),
 ("Which empire built the Colosseum in Rome?", ["The Roman Empire", "The Greek Empire", "The Ottoman Empire", "The Persian Empire"], "The Colosseum was completed in 80 AD and could hold around 50,000 people."),
 ("Who is usually credited with inventing the telephone?", ["Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "Guglielmo Marconi"], "Bell received the patent in 1876, although the Italian Antonio Meucci had developed a similar device earlier."),
 ("In which country did the Industrial Revolution begin?", ["Britain", "France", "Germany", "The United States"], "It began in Britain in the second half of the 18th century, with steam engines and textile factories."),
])
add("B1", "sci", [
 ("Which gas do plants take in from the air to make their food?", ["Carbon dioxide", "Oxygen", "Nitrogen", "Hydrogen"], "In photosynthesis, plants use sunlight, water and carbon dioxide, and release oxygen."),
 ("What is the closest star to the Earth?", ["The Sun", "Sirius", "Polaris", "Proxima Centauri"], "The Sun is a star! After the Sun, the closest one is Proxima Centauri."),
 ("How many bones does an adult human have?", ["206", "106", "306", "186"], "Babies are born with around 300, but some of them join together as we grow."),
 ("What is H₂O?", ["Water", "Salt", "Sugar", "Oxygen"], "Each water molecule has two hydrogen atoms and one oxygen atom."),
 ("Which planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter", "Mercury"], "Mars looks red because its surface contains a lot of iron oxide, or rust."),
 ("What is the largest animal that has ever lived?", ["The blue whale", "The African elephant", "The giraffe", "The orca"], "Blue whales can be about 30 metres long, bigger than any dinosaur we know of."),
 ("At what temperature does water boil at sea level?", ["100 °C", "90 °C", "110 °C", "120 °C"], "At higher altitudes the air pressure is lower, so water boils at a lower temperature."),
 ("Which organ pumps blood around the body?", ["The heart", "The lungs", "The liver", "The brain"], "An adult heart beats around 100,000 times a day."),
])
add("B1", "arts", [
 ("Who painted the Mona Lisa?", ["Leonardo da Vinci", "Michelangelo", "Raphael", "Pablo Picasso"], "Leonardo painted it in the early 1500s. Today it is in the Louvre, in Paris."),
 ("Who wrote Romeo and Juliet?", ["William Shakespeare", "Charles Dickens", "Jane Austen", "Oscar Wilde"], "Shakespeare wrote it in the 1590s. It is set in Verona, in Italy."),
 ("Who wrote Don Quixote?", ["Miguel de Cervantes", "Lope de Vega", "Federico García Lorca", "Gabriel García Márquez"], "It was published in two parts, in 1605 and 1615, and is often called the first modern novel."),
 ("Which instrument usually has 88 keys?", ["The piano", "The guitar", "The violin", "The harp"], "A standard piano has 52 white keys and 36 black keys."),
 ("Which famous band came from Liverpool?", ["The Beatles", "The Rolling Stones", "Queen", "U2"], "John, Paul, George and Ringo formed The Beatles in Liverpool in the early 1960s."),
 ("In which city is the Louvre Museum?", ["Paris", "Rome", "Madrid", "London"], "The Louvre is the most visited museum in the world."),
 ("What is the name of Salvador Dalí's famous painting with melting clocks?", ["The Persistence of Memory", "The Scream", "Guernica", "The Starry Night"], "Dalí painted it in 1931. 'The Scream' is by Munch and 'The Starry Night' by Van Gogh."),
 ("Where does the tango come from?", ["Argentina and Uruguay", "Spain", "Brazil", "Cuba"], "The tango was born in the Río de la Plata region at the end of the 19th century."),
])

# ================= B2 =================
add("B2", "geo", [
 ("Which country has the most time zones, if you include its overseas territories?", ["France", "Russia", "The United States", "China"], "Thanks to territories such as French Polynesia and Réunion, France uses twelve time zones."),
 ("What is the smallest country in the world?", ["Vatican City", "Monaco", "San Marino", "Malta"], "Vatican City covers less than half a square kilometre."),
 ("Which river flows through Vienna, Bratislava and Budapest?", ["The Danube", "The Rhine", "The Elbe", "The Vistula"], "The Danube crosses or borders ten countries before reaching the Black Sea."),
 ("The Strait of Gibraltar separates Europe from which continent?", ["Africa", "Asia", "The Middle East", "Oceania"], "At its narrowest point, Africa is only about 14 km from Spain."),
 ("Which is the driest non-polar desert in the world?", ["The Atacama", "The Sahara", "The Gobi", "The Namib"], "Some weather stations in Chile's Atacama have hardly ever recorded rain."),
 ("Which country has the longest coastline in the world?", ["Canada", "Russia", "Australia", "Norway"], "Canada's thousands of islands give it a coastline of over 200,000 km."),
 ("Lake Titicaca lies on the border between which two countries?", ["Peru and Bolivia", "Chile and Argentina", "Ecuador and Colombia", "Bolivia and Paraguay"], "At about 3,800 metres, it is one of the highest navigable lakes in the world."),
 ("Which European capital is built on fourteen islands?", ["Stockholm", "Amsterdam", "Copenhagen", "Helsinki"], "Stockholm lies where Lake Mälaren meets the Baltic Sea."),
])
add("B2", "hist", [
 ("Who was the first woman to win a Nobel Prize?", ["Marie Curie", "Mother Teresa", "Rosalind Franklin", "Ada Lovelace"], "Marie Curie won the Physics prize in 1903 and the Chemistry prize in 1911."),
 ("In which year did the Second World War end?", ["1945", "1943", "1944", "1946"], "The war ended in Europe in May 1945 and in Asia in September 1945."),
 ("The Magna Carta, signed in 1215, limited the power of whom?", ["The English king", "The Pope", "The French nobility", "Parliament"], "Barons forced King John to accept that even the king was subject to the law."),
 ("Which city was the capital of the Byzantine Empire?", ["Constantinople", "Rome", "Athens", "Alexandria"], "Constantinople, today's Istanbul, fell to the Ottomans in 1453."),
 ("Who led India's non-violent movement for independence?", ["Mahatma Gandhi", "Jawaharlal Nehru", "Indira Gandhi", "Winston Churchill"], "Gandhi's campaigns of peaceful resistance helped India gain independence in 1947."),
 ("What did the Wright brothers achieve in 1903?", ["The first powered aeroplane flight", "The first car journey", "The first transatlantic phone call", "The first hot-air balloon flight"], "Their first flight, in North Carolina, lasted just 12 seconds."),
 ("Which country gave the Statue of Liberty to the United States?", ["France", "Britain", "Spain", "Italy"], "It was a gift from the people of France, completed in 1886."),
 ("In which year did Spain's current Constitution come into force?", ["1978", "1975", "1982", "1986"], "It was approved in a referendum in December 1978, three years after Franco's death."),
])
add("B2", "sci", [
 ("Approximately how fast does light travel?", ["300,000 km per second", "30,000 km per second", "3,000,000 km per second", "300 km per second"], "Light from the Sun takes about eight minutes to reach us."),
 ("Where is most of a cell's DNA found?", ["In the nucleus", "In the cell membrane", "In the ribosomes", "In the cytoplasm"], "Most DNA is in the nucleus, although mitochondria also contain a small amount."),
 ("Which element has the chemical symbol Fe?", ["Iron", "Fluorine", "Lead", "Francium"], "Fe comes from 'ferrum', the Latin word for iron."),
 ("Why do we have seasons?", ["Because the Earth's axis is tilted", "Because the distance to the Sun changes a lot", "Because the Sun's activity changes", "Because of the Moon"], "The tilt means each hemisphere receives more direct sunlight for part of the year."),
 ("Which blood type is known as the universal donor?", ["O negative", "AB positive", "A positive", "B negative"], "O-negative red blood cells can usually be given to patients of any blood type."),
 ("What does a seismograph measure?", ["Earthquakes", "Wind speed", "Rainfall", "Air pressure"], "It records the vibrations of the ground."),
 ("Which vitamin does your skin produce when it is exposed to sunlight?", ["Vitamin D", "Vitamin A", "Vitamin C", "Vitamin K"], "Vitamin D helps the body absorb calcium for healthy bones."),
 ("Through which of these does sound travel fastest?", ["Steel", "Air", "Water", "A vacuum"], "Sound travels faster in solids. In a vacuum it can't travel at all."),
])
add("B2", "arts", [
 ("Who wrote One Hundred Years of Solitude?", ["Gabriel García Márquez", "Jorge Luis Borges", "Mario Vargas Llosa", "Julio Cortázar"], "The Colombian writer published it in 1967 and won the Nobel Prize in 1982."),
 ("Which composer kept writing music after becoming deaf?", ["Ludwig van Beethoven", "Wolfgang Amadeus Mozart", "Johann Sebastian Bach", "Frédéric Chopin"], "Beethoven composed his Ninth Symphony when he was almost completely deaf."),
 ("Who painted Guernica?", ["Pablo Picasso", "Salvador Dalí", "Joan Miró", "Francisco de Goya"], "Picasso painted it in 1937 after the bombing of the Basque town. It is in the Reina Sofía museum."),
 ("The line 'To be, or not to be' comes from which play?", ["Hamlet", "Macbeth", "Othello", "King Lear"], "Prince Hamlet says it while thinking about life and death."),
 ("Which architect designed the Sagrada Família?", ["Antoni Gaudí", "Santiago Calatrava", "Le Corbusier", "Frank Gehry"], "Construction began in 1882 and is still going on today."),
 ("Who directed the films Jaws and E.T.?", ["Steven Spielberg", "George Lucas", "Martin Scorsese", "Stanley Kubrick"], "Jaws (1975) is often called the first summer blockbuster."),
 ("Claude Monet is associated with which art movement?", ["Impressionism", "Cubism", "Surrealism", "Baroque"], "The movement's name comes from his painting 'Impression, Sunrise'."),
 ("Which expression comes from George Orwell's novel 1984?", ["Big Brother", "The Iron Curtain", "The American Dream", "Brave New World"], "Today 'Big Brother' means a government that watches everything people do. 'Brave New World' is Aldous Huxley's novel."),
])

# ================= C1 =================
add("C1", "geo", [
 ("Which country has the largest number of natural lakes?", ["Canada", "Finland", "Russia", "The United States"], "Canada has more lakes than the rest of the world combined, largely as a result of glaciers."),
 ("The 'Ring of Fire', with its many volcanoes and earthquakes, surrounds which ocean?", ["The Pacific", "The Atlantic", "The Indian", "The Arctic"], "It follows the edges of several tectonic plates around the Pacific."),
 ("Which line divides the Earth into the Northern and Southern Hemispheres?", ["The Equator", "The Prime Meridian", "The Tropic of Cancer", "The International Date Line"], "The Prime Meridian, through Greenwich, divides east from west."),
 ("Which country is completely surrounded by South Africa?", ["Lesotho", "Eswatini", "Botswana", "Namibia"], "Lesotho is an enclave; Eswatini also borders Mozambique."),
 ("What do we call an area of sea partly enclosed by land, with a wide opening?", ["A bay", "A strait", "A peninsula", "A delta"], "A strait is a narrow channel, a peninsula is land almost surrounded by water, and a delta forms at a river mouth."),
 ("Which of these countries is NOT crossed by the Andes?", ["Paraguay", "Chile", "Colombia", "Venezuela"], "The Andes run through seven countries, from Venezuela to Argentina, but not Paraguay."),
 ("Iceland's volcanic activity is largely due to its position on what?", ["The Mid-Atlantic Ridge", "The Ring of Fire", "The Tropic of Cancer", "The Gulf Stream"], "Iceland sits where the North American and Eurasian plates are moving apart, above a hotspot."),
 ("Which major city straddles two continents?", ["Istanbul", "Cairo", "Moscow", "Athens"], "The Bosphorus strait divides Istanbul between Europe and Asia."),
])
add("C1", "hist", [
 ("The Treaty of Tordesillas (1494) divided newly discovered lands between which two powers?", ["Spain and Portugal", "Spain and England", "France and Portugal", "England and the Netherlands"], "The line explains why Brazil speaks Portuguese while most of Latin America speaks Spanish."),
 ("The economic crisis that followed the 1929 Wall Street Crash is known as…", ["the Great Depression", "the Dust Bowl", "the Gilded Age", "the New Deal"], "The New Deal was President Roosevelt's response to the Depression."),
 ("The Rosetta Stone was crucial for deciphering what?", ["Egyptian hieroglyphs", "Cuneiform", "Mayan glyphs", "Linear B"], "It contains the same text in three scripts, including Ancient Greek, which scholars could already read."),
 ("Which event is generally seen as the trigger of the First World War?", ["The assassination of Archduke Franz Ferdinand", "The invasion of Poland", "The sinking of the Lusitania", "The Russian Revolution"], "He was shot in Sarajevo in June 1914. The invasion of Poland started the Second World War."),
 ("Who was the first emperor of a unified China?", ["Qin Shi Huang", "Kublai Khan", "Confucius", "Sun Yat-sen"], "He is also known for the Terracotta Army buried with him."),
 ("The Cold War was primarily a rivalry between which two powers?", ["The USA and the USSR", "The USA and China", "Britain and Germany", "France and the USSR"], "It lasted from the late 1940s until the collapse of the Soviet Union in 1991."),
 ("Which founding document begins with the words 'We the People'?", ["The US Constitution", "The US Declaration of Independence", "The Magna Carta", "The English Bill of Rights"], "The Constitution was signed in 1787; the Declaration of Independence dates from 1776."),
 ("Who developed the printing press with movable type in Europe around 1440?", ["Johannes Gutenberg", "William Caxton", "Leonardo da Vinci", "Galileo Galilei"], "Movable type had existed earlier in China and Korea, but Gutenberg's press transformed Europe."),
])
add("C1", "sci", [
 ("What does DNA stand for?", ["Deoxyribonucleic acid", "Dinitrogen acid", "Dynamic nuclear array", "Deoxyribose nitrate"], "DNA carries the genetic instructions of almost all living organisms."),
 ("Who developed the theory of evolution by natural selection, alongside Alfred Russel Wallace?", ["Charles Darwin", "Gregor Mendel", "Jean-Baptiste Lamarck", "Isaac Newton"], "Darwin published 'On the Origin of Species' in 1859."),
 ("What is the most abundant gas in the Earth's atmosphere?", ["Nitrogen", "Oxygen", "Carbon dioxide", "Argon"], "Nitrogen makes up about 78% of the air; oxygen about 21%."),
 ("Antibiotics are effective against which of the following?", ["Bacteria", "Viruses", "Allergies", "All kinds of infection"], "They don't work against viruses, which is why they are useless for a cold or the flu."),
 ("Why does a spoon look bent in a glass of water?", ["Because of refraction", "Because of reflection", "Because of diffraction", "Because of absorption"], "Refraction is the bending of light as it passes from one medium into another."),
 ("What does a light-year measure?", ["Distance", "Time", "Brightness", "Speed"], "It is the distance light travels in a year: about 9.5 trillion kilometres."),
 ("Which particle carries a negative charge?", ["The electron", "The proton", "The neutron", "The photon"], "Protons are positive, neutrons have no charge, and photons are particles of light."),
 ("Which organ produces insulin?", ["The pancreas", "The liver", "The kidneys", "The stomach"], "Insulin regulates the level of sugar in the blood."),
])
add("C1", "arts", [
 ("Which novel opens with the line 'Call me Ishmael'?", ["Moby-Dick", "Treasure Island", "The Old Man and the Sea", "Robinson Crusoe"], "Herman Melville's novel (1851) tells the story of Captain Ahab's obsession with a white whale."),
 ("Who composed The Four Seasons?", ["Antonio Vivaldi", "George Frideric Handel", "Joseph Haydn", "Johann Sebastian Bach"], "Vivaldi's four violin concertos date from the 1720s."),
 ("Which writer created the detective Hercule Poirot?", ["Agatha Christie", "Arthur Conan Doyle", "Raymond Chandler", "Georges Simenon"], "Conan Doyle created Sherlock Holmes; Simenon created Inspector Maigret."),
 ("Frida Kahlo is best known for what kind of painting?", ["Self-portraits", "Landscapes", "Abstract art", "Religious frescoes"], "Around a third of her paintings are self-portraits."),
 ("Who painted Las Meninas?", ["Diego Velázquez", "Francisco de Goya", "El Greco", "Bartolomé Esteban Murillo"], "Velázquez painted it in 1656, and even included himself at work in the picture."),
 ("Which film won the first Academy Award for Best Picture?", ["Wings", "Casablanca", "Gone with the Wind", "Citizen Kane"], "Wings, a silent film about First World War pilots, won at the first ceremony in 1929."),
 ("Who wrote Pride and Prejudice?", ["Jane Austen", "Charlotte Brontë", "Virginia Woolf", "Mary Shelley"], "It was published in 1813. Mary Shelley wrote Frankenstein."),
 ("Which Argentine writer wrote Ficciones and The Aleph?", ["Jorge Luis Borges", "Julio Cortázar", "Ernesto Sabato", "Adolfo Bioy Casares"], "Borges is famous for short stories about labyrinths, mirrors and infinite libraries."),
])

# ================= C2 =================
add("C2", "geo", [
 ("The point on land farthest from any ocean lies in which country?", ["China", "Mongolia", "Kazakhstan", "Russia"], "The so-called Eurasian pole of inaccessibility is in north-western China, more than 2,500 km from the sea."),
 ("What is a fjord?", ["A long, narrow sea inlet between steep cliffs, carved by glaciers", "A lake inside a volcanic crater", "A ring-shaped coral reef", "The fan-shaped mouth of a river"], "Norway, Chile and New Zealand are famous for them. A crater lake, an atoll and a delta are the other three."),
 ("What makes the Dead Sea geographically remarkable?", ["Its shores are the lowest land on Earth's surface", "It is the deepest lake in the world", "It is the largest lake in Asia", "It is made of fresh water"], "Its shores lie over 400 metres below sea level. The deepest lake is Baikal."),
 ("Which river discharges the largest volume of water?", ["The Amazon", "The Nile", "The Yangtze", "The Congo"], "The Amazon carries roughly a fifth of all the river water that flows into the oceans."),
 ("Which two countries share the world's longest international border?", ["Canada and the USA", "Russia and Kazakhstan", "Argentina and Chile", "China and Mongolia"], "It runs for nearly 9,000 km, including the border with Alaska."),
 ("What does the term 'rain shadow' describe?", ["A dry area on the sheltered side of a mountain range", "The shadow cast by a storm cloud", "A region where it rains almost every day", "The gap between two weather fronts"], "Air loses its moisture as it rises over the mountains, so the far side stays dry, as in Patagonia."),
 ("Which is the largest country in Africa by area?", ["Algeria", "Sudan", "The Democratic Republic of the Congo", "Libya"], "Algeria became the largest after South Sudan's independence in 2011."),
 ("Which of these cities lies furthest south?", ["Buenos Aires", "Cape Town", "Sydney", "Santiago de Chile"], "Buenos Aires is at about 34.6° S, slightly further south than Cape Town and Sydney (about 33.9° S)."),
])
add("C2", "hist", [
 ("The Peace of Westphalia (1648) is often regarded as the origin of what?", ["The modern principle of state sovereignty", "The European Union", "NATO", "The United Nations"], "It ended the Thirty Years' War and established the idea that states control their own territory."),
 ("What does the 'Scramble for Africa' refer to?", ["The rapid colonisation of Africa by European powers in the late 19th century", "A series of independence movements in the 1960s", "The Atlantic slave trade", "The construction of the Suez Canal"], "By 1914, almost the whole continent was under European control."),
 ("Which civilisation built the vast road network known as the Qhapaq Ñan?", ["The Inca", "The Maya", "The Aztecs", "The Olmecs"], "It covered around 30,000 km across the Andes and is now a UNESCO World Heritage Site."),
 ("The expression 'Pyrrhic victory' comes from a king who defeated which power at a ruinous cost?", ["Rome", "Carthage", "Persia", "Sparta"], "King Pyrrhus of Epirus beat the Romans but lost so many men that victory was almost a defeat."),
 ("What was the Marshall Plan?", ["A US programme to help rebuild Western Europe after the Second World War", "A plan for the D-Day landings", "A Soviet five-year plan", "An agreement to divide Berlin"], "Between 1948 and 1952, the USA provided over 13 billion dollars in aid."),
 ("Which dynasty ruled Spain during much of its Golden Age, including the reign of Philip II?", ["The Habsburgs", "The Bourbons", "The Tudors", "The Trastámaras"], "The Spanish Habsburgs ruled from 1516 to 1700; the Bourbons came afterwards."),
 ("The Protestant Reformation is usually dated from 1517, when who published his Ninety-five Theses?", ["Martin Luther", "John Calvin", "Huldrych Zwingli", "Erasmus of Rotterdam"], "Luther criticised the sale of indulgences by the Catholic Church."),
 ("Who 'crossed the Rubicon' in 49 BC, giving us the expression for a point of no return?", ["Julius Caesar", "Augustus", "Pompey", "Mark Antony"], "By leading his army across the river into Italy, Caesar started a civil war."),
])
add("C2", "sci", [
 ("What does Heisenberg's uncertainty principle state?", ["The position and momentum of a particle cannot both be known exactly at the same time", "All measurements contain human error", "Electrons orbit the nucleus in fixed paths", "Energy cannot be created or destroyed"], "The more precisely you know one, the less precisely you can know the other."),
 ("Which effect allows a superconductor to make a magnet float above it?", ["The Meissner effect", "The Doppler effect", "The photoelectric effect", "The Hall effect"], "A superconductor expels magnetic fields from its interior, which can cause levitation."),
 ("What is CRISPR mainly used for?", ["Editing genes", "Dating fossils", "Imaging the brain", "Detecting gravitational waves"], "Its developers, Emmanuelle Charpentier and Jennifer Doudna, won the Nobel Prize in Chemistry in 2020."),
 ("Informally, what does entropy measure?", ["The degree of disorder in a system", "The speed of a chemical reaction", "The total mass of a system", "The temperature of an object"], "The second law of thermodynamics says the entropy of an isolated system tends to increase."),
 ("Why does an ambulance siren seem to change pitch as it passes you?", ["Because of the Doppler effect", "Because of the Coriolis effect", "Because of the Meissner effect", "Because of the Tyndall effect"], "Sound waves are compressed as the source approaches and stretched as it moves away."),
 ("What did the LIGO detectors confirm in 2015?", ["The existence of gravitational waves", "The existence of the Higgs boson", "The nature of dark matter", "The first planet outside our solar system"], "Einstein had predicted them a century earlier. The Higgs boson was found at CERN in 2012."),
 ("What is an enzyme?", ["A protein that speeds up chemical reactions in living things", "A hormone that controls growth", "A type of white blood cell", "A molecule that stores genetic information"], "Digestive enzymes, for example, break food down into smaller molecules."),
 ("What are tardigrades, or 'water bears', famous for?", ["Surviving extreme conditions, even in space", "Living for over a thousand years", "Producing their own light", "Being the largest insects on Earth"], "They can survive freezing, boiling, radiation and the vacuum of space in a dried-out state."),
])
add("C2", "arts", [
 ("The 'stream of consciousness' technique is most closely associated with which writer?", ["James Joyce", "Ernest Hemingway", "Charles Dickens", "Leo Tolstoy"], "Joyce's 'Ulysses' (1922) follows the uninterrupted flow of its characters' thoughts."),
 ("Who wrote the poem The Waste Land?", ["T. S. Eliot", "W. B. Yeats", "Ezra Pound", "W. H. Auden"], "Published in 1922, it is one of the key works of modernist poetry."),
 ("Magical realism is closely associated with which literary phenomenon?", ["The Latin American Boom", "Romanticism", "The Beat Generation", "The Lost Generation"], "Writers like García Márquez and Cortázar reached a worldwide audience in the 1960s and 70s."),
 ("In music, what is a leitmotif?", ["A recurring theme linked to a character, place or idea", "A short piece for solo piano", "The final section of a symphony", "A sudden change of key"], "Wagner used them extensively, and film composers like John Williams still do."),
 ("Which architect is famous for the maxim 'less is more'?", ["Ludwig Mies van der Rohe", "Le Corbusier", "Frank Lloyd Wright", "Walter Gropius"], "The phrase sums up the minimalist approach of modernist architecture."),
 ("What does 'chiaroscuro' refer to in painting?", ["A strong contrast between light and dark", "A technique of painting on wet plaster", "The use of small dots of colour", "A way of creating perspective with lines"], "Caravaggio and Rembrandt were masters of it. The other options describe fresco, pointillism and linear perspective."),
 ("At the start of Kafka's The Metamorphosis, Gregor Samsa wakes up transformed into what?", ["A huge insect", "A statue", "A bird", "A dog"], "The adjective 'Kafkaesque' now describes absurd, nightmarish situations, often involving bureaucracy."),
 ("Which director made All About My Mother?", ["Pedro Almodóvar", "Luis Buñuel", "Alejandro Amenábar", "Carlos Saura"], "The film won the Oscar for Best Foreign Language Film in 2000."),
])

if __name__ == "__main__":
    from collections import Counter
    c = Counter((q[0], q[1]) for q in Q)
    assert all(v == 8 for v in c.values()) and len(c) == 16, c
    for q in Q:
        assert len(q[3]) == 4 and len(set(q[3])) == 4, q[2]
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    open(os.path.join(root, "data", "quiz.js"), "w").write(
        "// General knowledge quiz: [level, category, question, options (correct first; shuffled in the app), explanation]\nDATA.quiz = "
        + json.dumps(Q, ensure_ascii=False, separators=(",", ":")).replace("],[", "],\n[") + ";\n")
    print("questions", len(Q))
