""" Questions for Quiz """


class Question:
    """
    The Class Question gets the questions and answers
    """
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


eng_questions = [
    "What year did England win their last Six-Nations grand slam?\n \
    (a) 2016\n \
    (b) 2017\n \
    (c) 2018\n",

    "How many grand slams have England won in total?\n \
    (a) 12\n \
    (b) 15\n \
    (c) 13\n",

    "What English player won 'Player of the Championship' in 2014?\n \
    (a) Mike Brown\n \
    (b) Chris Robshaw\n \
    (c) Dylan Hartley\n",

    "England hold the record for most scores in one match.  What was"
    "that score?\n \
    (a) 93 points\n \
    (b) 75 points\n \
    (c) 80 points\n"

    "Who is Englands most capped Six-Nations Player\n \
    (a) Ben Youngs\n \
    (b) Jason Leonard\n \
    (c) Mike Catt\n"

    "Who captained England to the 1991 Grand Slam?\n \
    (a) Will Carling\n \
    (b) Brian Moore\n \
    (c) Rob Andrew\n"

    "Who scored the most Six-Nations tries for England?\n \
    (a) Tony Underwood\n \
    (b) Jason Leonard\n \
    (c) Rory Underwood\n"

    "What English player has scored the most drop-goals in the tournament?\n \
    (a) Rob Andrew\n \
    (b) Johnny Wilkinson\n \
    (c) Owen Farrell\n"

    "What stadium do England play their home games?\n \
    (a) Wembly\n \
    (b) Millenium Statidum\n \
    (c) Twickenham\n"

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
    "Who scored the only try for Ireland when they beat England in "
    "Twickenham in 2004\n \
    (a) Girvan Dempsey\n \
    (b) Brian O'Driscoll\n \
    (c) Ronan O'Gara\n",

    "Who won player of the Six-Nations Championship in 2010?\n \
    (a) Brian O'Driscoll\n \
    (b) Paul O'Connell\n \
    (c) Tommy Bowe\n",

    "As of 2021 what irish player holds the record for the most points "
    "scored in the Six Nations Championship?\n \
    (a) David Humphreys\n \
    (b) Johnny Sexton\n \
    (c) Ronan O'Gara\n",

    "Ireland's biggest away winning margin of 63-10 was away to"
    " Italy in what year?\n \
    (a) 2015\n \
    (b) 2009\n \
    (c) 2017\n"

    "How many times has Ireland won a Six-Nations grand slam?\n \
    (a) 3\n \
    (b) 4\n \
    (c) 2\n"

    "What place did Ireland finish in the 2021 Six-nations Championship?\n \
    (a) Second\n \
    (b) First\n \
    (c) Third\n"

    "Rob Kearney has won two Grand Slams for Ireland.  Who is the"
    " only other Irish Player to do this?\n \
    (a) Brian O'Driscoll\n \
    (b) Rory Best\n \
    (c) Paul O'Connell\n"

    "Which Irish player holds the record for the most successive "
    "starts in the Six Nations?\n \
    (a) Keith Wood\n \
    (b) Brian O'Driscoll\n \
    (c) John Hayes\n"

    "Whoe has the most ball carries in a single Six Nations encounter\n \
    (a) Denis Leamy\n \
    (b) Peter O'Mahoney\n \
    (c) David Wallace\n"

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
    "Where do Wales play their home games?\n \
    (a) Cardiff Arms Park\n \
    (b) Sophia Gardens\n \
    (c) Principality Stadiyum\n",

    "Which Welsh player won Player of the Tournament in 2019?\n \
    (a) Alun Wyn Jones\n \
    (b) George North\n \
    (c) Dan Biggar\n",

    "Who has scored the most points for Wales in the Six-Nations\n \
    (a) Neil Jenkins\n \
    (b) Leigh Halfpenny\n \
    (c) Stephen Jones\n",

    "How many Grand Slams have Wales won?\n \
    (a) 10\n \
    (b) 11\n \
    (c) 12\n"

    "How many Triple Crowns have Wales won?\n \
    (a) 26\n \
    (b) 24\n \
    (c) 22\n"

    "When did Wales last win the Six Nations Championship?\n \
    (a) 2019\n \
    (b) 2020\n \
    (c) 2021\n"

    "Which Welsh player won Player of the Championship in 2013\n \
    (a) Dan Lydiate\n \
    (b) Leigh Halfpenny\n \
    (c) Shane Williams\n"

    "Wales hold the record for the longest time without conceding a "
    "try.  How many minutes?\n \
    (a) 220\n \
    (b) 150\n \
    (c) 358\n"

    "Who was the head coach for Wales when they won the Grand Slam in 2005?\n \
    (a) Mike Ruddock\n \
    (b) Steve Hansen\n \
    (c) Scott Johnson\n"

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
    "Scotland compete against which team in the Six-Nations for the "
    "Calcutta Cup?\n \
    (a) Ireland\n \
    (b) Wales\n \
    (c) England\n",

    "Who captained Scotland in the 2020 Six-Nations Championship?\n \
    (a) Stuart Hogg\n \
    (b) Finn Russell\n \
    (c) Ali Price\n",

    "Who is Scotland's top scorer in the Six Nations?\n \
    (a) Gavin Hastings\n \
    (b) Gregor Townsend\n \
    (c) Chris Paterson\n",

    "Who is Scotland's most capped player in the Six-Nations?\n \
    (a) Jonny  Gray\n \
    (b) Greig Lidlaw\n \
    (c) Ross Ford\n"

    "Who has scored the most tries for Scotland in the Six-Nations\n \
    (a) Ian Smith\n \
    (b) Stuart Hogg\n \
    (c) Gavin Hastings\n"

    "Where do Scotland play their home games?\n \
    (a) Ibrox Stadium\n \
    (b) Hampden Park\n \
    (c) Murrayfield\n"

    "What flower is the national emblem of Scotland?\n \
    (a) Daffodil\n \
    (b) Thistle\n \
    (c) Rose\n"

    "When did Scotland last win a Grand Slam\n \
    (a) 1982\n \
    (b) 1985\n \
    (c) 1990\n"

    "Who captianed Scotland when they won their last Grand Slam?\n \
    (a) David Sole\n \
    (b) Gavin Hastings\n \
    (c) Craig Chalmers\n"

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
    "Who is Italy's most capped player for the Six-Nations?\n \
    (a) Martin Castrogiovanni\n \
    (b) Alessandro Zanni\n \
    (c) Sergio Parisse\n",

    "Who was Italy's coach for the 2017 Six-Nations?\n \
    (a) Conor O'Shea\n \
    (b) Jacques Brunel\n \
    (c) Franco Smith\n",

    "What stadium do Italy play their home games in?\n \
    (a) Stadio Flaminio\n \
    (b) Stadio Marassi\n \
    (c) Stadio Olimpico\n",

    "Who did Italy defeat in their very first Six-Nations game?\n \
    (a) Wales\n \
    (b) Ireland\n \
    (c) Scotland\n"

    "What year did Italy and France start competing for the "
    "Giuseppe Garibaldi trophy?\n \
    (a) 2007\n \
    (b) 2008\n \
    (c) 2009\n"

    "What year was Italy added to the Six-Nations tournament?\n \
    (a) 2002\n \
    (b) 2001\n \
    (c) 2000\n"

    "What is the national rugby team color for Italy?\n \
    (a) Azure Blue\n \
    (b) Savoy Blue\n \
    (c) Royal Blue\n"

    "How many times have Italy taken home the Wooden Spoon trophy?\n \
    (a) 15\n \
    (b) 14\n \
    (c) 17\n"

    "How many times have Italy beaten France in the Six-Nations?\n \
    (a) Once\n \
    (b) Twice\n \
    (c) Three times\n"

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
    "Where do France play their home games?\n \
    (a) Stade Pierre-Mauroy\n \
    (b) Parc de France\n \
    (c) Stade de France\n",

    "Who is France's top scorer for the Six-Nations?\n \
    (a) Frederic Michalak\n \
    (b) Romain Ntamack\n \
    (c) Philippe Sella\n",

    "Which French player was Player of the Championship in 2020?\n \
    (a) Gael Fickou\n \
    (b) Charles Ollivon\n \
    (c) Antoine Dupont\n",

    "Who is France's most capped player in the Six-Nations?\n \
    (a) Serg Betsen\n \
    (b) Fabien Galthie\n \
    (c) Fabien Pelous\n"

    "Who is France's top try-scorer in the Six-Nations\n \
    (a) Serg Blanco\n \
    (b) Vincent Clerc\n \
    (c) Tomas Castaignede\n"

    "How many times have France won a Six-Nations Grand Slam?\n \
    (a) 10\n \
    (b) 8\n \
    (c) 9\n"

    "When did France last win a Six Nations Grand Slam?\n \
    (a) 2011\n \
    (b) 2022\n \
    (c) 2015\n"

    "The French mascot is a rooster but what is his name?\n \
    (a) Astrix\n \
    (b) Serge\n \
    (c) Footix\n"

    "Which game is commonly referred to as 'Le Crunch'?\n \
    (a) France v England\n \
    (b) France v Wales\n \
    (c) France v Ireland\n"

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
