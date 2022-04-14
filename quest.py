"""
Questions for Quiz.

"""


class Question:
    """
    The Class Question holds the questions and answers
    for each country
    """
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


eng_questions = [
    "\tWhat year did England win their last Six-Nations "
    "\n\tgrand slam?\n \
    \t(a) 2016\n \
    \t(b) 2017\n \
    \t(c) 2018\n",

    "\tHow many grand slams have England won in total?\n \
    \t(a) 12\n \
    \t(b) 15\n \
    \t(c) 13\n",

    "\tWhat English player won 'Player of the Championship' "
    "\n\tin 2014?\n \
    \t(a) Mike Brown\n \
    \t(b) Chris Robshaw\n \
    \t(c) Dylan Hartley\n",

    "\tEngland hold the record for most scores in one "
    "\n\tmatch.\n\tWhat was that score?\n \
    \t(a) 93 points\n \
    \t(b) 75 points\n \
    \t(c) 80 points\n",

    "\tWho is Englands most capped Six-Nations Player\n \
    \t(a) Ben Youngs\n \
    \t(b) Jason Leonard\n \
    \t(c) Mike Catt\n",

    "\tWho captained England to the 1991 Grand Slam?\n \
    \t(a) Will Carling\n \
    \t(b) Brian Moore\n \
    \t(c) Rob Andrew\n",

    "\tWho scored the most Six-Nations tries for England?\n \
    \t(a) Tony Underwood\n \
    \t(b) Jason Leonard\n \
    \t(c) Rory Underwood\n",

    "\tWhat English player has scored the most drop-goals "
    "\n\tin the tournament?\n \
    \t(a) Rob Andrew\n \
    \t(b) Johnny Wilkinson\n \
    \t(c) Owen Farrell\n",

    "What stadium do England play their home games?\n \
    \t(a) Wembly\n \
    \t(b) Millenium Statidum\n \
    \t(c) Twickenham\n",

]

eng_question_list = [
    Question(eng_questions[0], "a"),
    Question(eng_questions[1], "c"),
    Question(eng_questions[2], "a"),
    Question(eng_questions[3], "c"),
    Question(eng_questions[4], "c"),
    Question(eng_questions[5], "a"),
    Question(eng_questions[6], "c"),
    Question(eng_questions[7], "b"),
    Question(eng_questions[8], "c"),

]


ire_questions = [
    "\tWho scored the only try for Ireland when they beat "
    "\n\tEngland in "
    "Twickenham in 2004\n \
    \t(a) Girvan Dempsey\n \
    \t(b) Brian O'Driscoll\n \
    \t(c) Ronan O'Gara\n",

    "\tWho won player of the Six-Nations Championship in "
    "\n\t2010?\n \
    \t(a) Brian O'Driscoll\n \
    \t(b) Paul O'Connell\n \
    \t(c) Tommy Bowe\n",

    "\tAs of 2021 what irish player holds the record for "
    "\n\tthe most points scored in the Six Nations Championship?\n \
    \t(a) David Humphreys\n \
    \t(b) Johnny Sexton\n \
    \t(c) Ronan O'Gara\n",

    "\tIreland's biggest away winning margin of 63-10 was "
    "\n\taway to Italy in what year?\n \
    \t(a) 2015\n \
    \t(b) 2009\n \
    \t(c) 2017\n",

    "\tHow many times has Ireland won a Six-Nations "
    "\n\tgrand slam?\n \
    \t(a) 3\n \
    \t(b) 4\n \
    \t(c) 2\n",

    "\tWhat place did Ireland finish in the 2021 "
    "\n\tSix-nations Championship?\n \
    \t(a) Second\n \
    \t(b) First\n \
    \t(c) Third\n",

    "\tRob Kearney has won two Grand Slams for Ireland.  Who "
    "\n\tis the only other Irish Player to do this?\n \
    \t(a) Brian O'Driscoll\n \
    \t(b) Rory Best\n \
    \t(c) Paul O'Connell\n",

    "\tWhich Irish player holds the record for the "
    "\n\tmost successive starts in the Six Nations?\n \
    \t(a) Keith Wood\n \
    \t(b) Brian O'Driscoll\n \
    \t(c) John Hayes\n",

    "\tWhoe has the most ball carries in a single Six "
    "\n\tNations encounter\n \
    \t(a) Denis Leamy\n \
    \t(b) Peter O'Mahoney\n \
    \t(c) David Wallace\n",

]

ire_question_list = [
    Question(ire_questions[0], "a"),
    Question(ire_questions[1], "a"),
    Question(ire_questions[2], "c"),
    Question(ire_questions[3], "c"),
    Question(ire_questions[4], "a"),
    Question(ire_questions[5], "c"),
    Question(ire_questions[6], "b"),
    Question(ire_questions[7], "c"),
    Question(ire_questions[8], "a"),

]

wales_questions = [
    "\tWhere do Wales play their home games?\n \
    \t(a) Cardiff Arms Park\n \
    \t(b) Sophia Gardens\n \
    \t(c) Principality Stadiyum\n",

    "\tWhich Welsh player won Player of the Tournament "
    "\n\tin 2019?\n \
    \t(a) Alun Wyn Jones\n \
    \t(b) George North\n \
    \t(c) Dan Biggar\n",

    "\tWho has scored the most points for Wales in the "
    "\n\tSix-Nations\n \
    \t(a) Neil Jenkins\n \
    \t(b) Leigh Halfpenny\n \
    \t(c) Stephen Jones\n",

    "\tHow many Grand Slams have Wales won?\n \
    \t(a) 10\n \
    \t(b) 11\n \
    \t(c) 12\n",

    "\tHow many Triple Crowns have Wales won?\n \
    \t(a) 26\n \
    \t(b) 24\n \
    \t(c) 22\n",

    "\tWhen did Wales last win the Six Nations Championship?\n \
    \t(a) 2019\n \
    \t(b) 2020\n \
    \t(c) 2021\n",

    "\tWhich Welsh player won Player of the Championship "
    "\n\tin 2013\n \
    \t(a) Dan Lydiate\n \
    \t(b) Leigh Halfpenny\n \
    \t(c) Shane Williams\n",

    "\tWales hold the record for the longest time without "
    "\n\tconceding a try.  How many minutes?\n \
    \t(a) 220\n \
    \t(b) 150\n \
    \t(c) 358\n",

    "\tWho was the head coach for Wales when they won "
    "\n\tthe Grand Slam in 2005?\n \
    \t(a) Mike Ruddock\n \
    \t(b) Steve Hansen\n \
    \t(c) Scott Johnson\n",

]

wales_question_list = [
    Question(wales_questions[0], "c"),
    Question(wales_questions[1], "a"),
    Question(wales_questions[2], "c"),
    Question(wales_questions[3], "c"),
    Question(wales_questions[4], "a"),
    Question(wales_questions[5], "c"),
    Question(wales_questions[6], "b"),
    Question(wales_questions[7], "c"),
    Question(wales_questions[8], "a"),

]

scot_questions = [
    "\tScotland compete against which team in the Six-Nations "
    "\n\tfor the Calcutta Cup?\n \
    \t(a) Ireland\n \
    \t(b) Wales\n \
    \t(c) England\n",

    "\tWho captained Scotland in the 2020 Six-Nations "
    "\n\tChampionship?\n \
    \t(a) Stuart Hogg\n \
    \t(b) Finn Russell\n \
    \t(c) Ali Price\n",

    "\tWho is Scotland's top scorer in the Six Nations?\n \
    \t(a) Gavin Hastings\n \
    \t(b) Gregor Townsend\n \
    \t(c) Chris Paterson\n",

    "\tWho is Scotland's most capped player in the Six-Nations?\n \
    \t(a) Jonny  Gray\n \
    \t(b) Greig Lidlaw\n \
    \t(c) Ross Ford\n",

    "\tWho has scored the most tries for Scotland in "
    "\n\tthe Six-Nations\n \
    \t(a) Ian Smith\n \
    \t(b) Stuart Hogg\n \
    \t(c) Gavin Hastings\n",

    "\tWhere do Scotland play their home games?\n \
    \t(a) Ibrox Stadium\n \
    \t(b) Hampden Park\n \
    \t(c) Murrayfield\n",

    "\tWhat flower is the national emblem of Scotland?\n \
    \t(a) Daffodil\n \
    \t(b) Thistle\n \
    \t(c) Rose\n",

    "\tWhen did Scotland last win a Grand Slam\n \
    \t(a) 1982\n \
    \t(b) 1985\n \
    \t(c) 1990\n",

    "\tWho captianed Scotland when they won their "
    "\n\tlast Grand Slam?\n \
    \t(a) David Sole\n \
    \t(b) Gavin Hastings\n \
    \t(c) Craig Chalmers\n",

]

scot_question_list = [
    Question(scot_questions[0], "c"),
    Question(scot_questions[1], "a"),
    Question(scot_questions[2], "c"),
    Question(scot_questions[3], "c"),
    Question(scot_questions[4], "a"),
    Question(scot_questions[5], "c"),
    Question(scot_questions[6], "b"),
    Question(scot_questions[7], "c"),
    Question(scot_questions[8], "a"),

]

italy_questions = [
    "\tWho is Italy's most capped player for the Six-Nations?\n \
    \t(a) Martin Castrogiovanni\n \
    \t(b) Alessandro Zanni\n \
    \t(c) Sergio Parisse\n",

    "\tWho was Italy's coach for the 2017 Six-Nations?\n \
    \t(a) Conor O'Shea\n \
    \t(b) Jacques Brunel\n \
    \t(c) Franco Smith\n",

    "\tWhat stadium do Italy play their home games in?\n \
    \t(a) Stadio Flaminio\n \
    \t(b) Stadio Marassi\n \
    \t(c) Stadio Olimpico\n",

    "\tWho did Italy defeat in their very first "
    "\n\tSix-Nations game?\n \
    \t(a) Wales\n \
    \t(b) Ireland\n \
    \t(c) Scotland\n",

    "\tWhat year did Italy and France start competing "
    "\n\tfor the Giuseppe Garibaldi trophy?\n \
    \t(a) 2007\n \
    \t(b) 2008\n \
    \t(c) 2009\n",

    "\tWhat year was Italy added to the Six-Nations "
    "\n\ttournament?\n \
    \t(a) 2002\n \
    \t(b) 2001\n \
    \t(c) 2000\n",

    "\tWhat is the national rugby team color for Italy?\n \
    \t(a) Azure Blue\n \
    \t(b) Savoy Blue\n \
    \t(c) Royal Blue\n",

    "\tHow many times have Italy taken home the Wooden "
    "\n\tSpoon trophy?\n \
    \t(a) 15\n \
    \t(b) 14\n \
    \t(c) 17\n",

    "\tHow many times have Italy beaten France in the "
    "\n\tSix-Nations?\n \
    \t(a) Once\n \
    \t(b) Twice\n \
    \t(c) Three times\n",

]

italy_question_list = [
    Question(italy_questions[0], "c"),
    Question(italy_questions[1], "a"),
    Question(italy_questions[2], "c"),
    Question(italy_questions[3], "c"),
    Question(italy_questions[4], "a"),
    Question(italy_questions[5], "c"),
    Question(italy_questions[6], "b"),
    Question(italy_questions[7], "c"),
    Question(italy_questions[8], "b"),

]

france_questions = [
    "\tWhere do France play their home games?\n \
    \t(a) Stade Pierre-Mauroy\n \
    \t(b) Parc de France\n \
    \t(c) Stade de France\n",

    "\tWho is France's top scorer for the Six-Nations?\n \
    \t(a) Frederic Michalak\n \
    \t(b) Romain Ntamack\n \
    \t(c) Philippe Sella\n",

    "\tWhich French player was Player of the Championship "
    "\n\tin 2020?\n \
    \t(a) Gael Fickou\n \
    \t(b) Charles Ollivon\n \
    \t(c) Antoine Dupont\n",

    "\tWho is France's most capped player in the "
    "\n\tSix-Nations?\n \
    \t(a) Serg Betsen\n \
    \t(b) Fabien Galthie\n \
    \t(c) Fabien Pelous\n",

    "\tWho is France's top try-scorer in the Six-Nations\n \
    \t(a) Serg Blanco\n \
    \t(b) Vincent Clerc\n \
    \t(c) Tomas Castaignede\n",

    "\tHow many times have France won a Six-Nations "
    "\n\tGrand Slam?\n \
    \t(a) 10\n \
    \t(b) 8\n \
    \t(c) 9\n",

    "\tWhen did France last win a Six Nations Grand Slam?\n \
    \t(a) 2011\n \
    \t(b) 2022\n \
    \t(c) 2015\n",

    "\tThe French mascot is a rooster but what is his name?\n \
    \t(a) Astrix\n \
    \t(b) Serge\n \
    \t(c) Footix\n",

    "\tWhich game is commonly referred to as 'Le Crunch'?\n \
    \t(a) France v England\n \
    \t(b) France v Wales\n \
    \t(c) France v Ireland\n",

]

france_question_list = [
    Question(france_questions[0], "c"),
    Question(france_questions[1], "a"),
    Question(france_questions[2], "c"),
    Question(france_questions[3], "c"),
    Question(france_questions[4], "a"),
    Question(france_questions[5], "a"),
    Question(france_questions[6], "b"),
    Question(france_questions[7], "c"),
    Question(france_questions[8], "a"),

]
