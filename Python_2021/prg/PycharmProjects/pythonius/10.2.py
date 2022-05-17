"""
Starting with player 1, each player gets a turn at answering 5 trivia questions.
(There should be a total of 10 questions so each player gets different
questions.) When a question is displayed, 4 possible answers are also displayed.
Only one of the answers is correct, and if the player selects the correct answer,
he or she earns a point.
After answers have been selected for all the questions, the program displays the number of points earned by each player and declares the player with the highest number of points the winner.
To create this program, write a Question class to hold the data for the trivia question. The question class should have attributes for the following data:
A trivia question
Possible answer 1
Possible answer 2
Possible answer 3
Possible answer 4
The number of the correct answer (1, 2, 3, or 4)
The Question class should also have an appropriate __init__ method, accessors, and mutators.
______________________________________________________
CLASS DIAGRAM:
Question:
—init
-trivia question
-possible answer 1
-possible answer 2
-possible answer 3
-possible answer 4
-Correct answer
_________________
+set question
+set possible answer 1
+set possible answer 2
+set possible answer 3
+set possible answer 4
+set correct answer
+get question
+get possible answer 1
+get possible answer 2
+get possible answer 3
+get possible answer 4
+get correct answer
"""


class Question:
    # main constructor
    def __init__(self, trivia, possible1, possible2, possible3, possible4, correctA):
        self.__trivia = trivia
        self.__possible1 = possible1
        self.__possible2 = possible2
        self.__possible3 = possible3
        self.__possible4 = possible4
        self.__correctA = correctA

    # mutators and definers
    def set_trivia(self, trivia):
        self.__trivia = trivia

    def set_possible1(self, possible1):
        self.__trivia = possible1

    def set_possible2(self, possible2):
        self.__trivia = possible2

    def set_possible3(self, possible3):
        self.__trivia = possible3

    def set_possible4(self, possible4):
        self.__trivia = possible4

    def set_correctA(self, correctA):
        self.__correctA = correctA

    def get_trivia(self):
        return self.__trivia

    def get_possible1(self):
        return self.__possible1

    def get_possible2(self):
        return self.__possible2

    def get_possible3(self):
        return self.__possible3

    def get_possible4(self):
        return self.__possible4

    def get_correctA(self):
        return self.__correctA

    def __str__(self):
        fullQuestion = self.__trivia + self.__possible1 + self.__possible2 + self.__possible3 + self.__possible4
        return fullQuestion


def main():
    print("TIME FOR THE MOST THRILLING AND ACTION PACKED TRIVIA IN YOUR ENTIRE LIFE")
    question1 = Question("\nWhen was Grevious betrayed by the banking clan?", "\n1) At the start second Huk War",
                         "\n2) At the start of the Clone Wars", "\n3) Before Count Dooku Fell to the dark side",
                         "\n4) During the night Sidious betrayed Plagueis", "1")
    question2 = Question("\nWhen did Darth Maul Die?", "\n1) During the fight against Palpatine on Mandalor",
                         "\n2) From Old Age", "\n3) During his fight on Tatooine with Kenobi",
                         "\n4) During his fight against Kenobi and Qui Gon Jinn", "3")

    question3 = Question("\nHow many Younglings did Anakin Face during Order 66?", "\n1) 18", "\n2) 6", "\n3) 11",
                         "\n4) 20", "4")

    question4 = Question("\nWhich Clone Division Served Under Yoda?", "\n1) The 501st Legion",
                         "\n2) The 104th Battalion", "\n3) The 41st Stormtrooper Legion",
                         "\n4) The 212th Attack Battalion", "3")

    question5 = Question("\n What was the Most Powerful Droid in the CIS Army?", "\n1) Scorpenek Annihlator",
                         "\n2) HailFire Droid", "\n3) Droideka", "\n4) B1 Battle droid", "1")

    question6 = Question("\n What was the home planet of the Clone army?", "\n1) Tatooine", "\n2) Kamino",
                         "\n3) Tython", "\n4) Skippio", "2")

    question7 = Question("\n How Long Did the Empire Last?", "\n1) 4 Years", "\n2) 300 Years", "\n3) 19 Years",
                         "\n4)600 Years", "3")

    question8 = Question("\n How many Jedis Did Palpatine Kill During his Sick Flip?",
                         "\n1) One Knight and two masters", "\n2) One Master One Knight and two Padawan",
                         "\n3) Three Masters and a Knight", "\n4) Three Masters", "4")

    question9 = Question("\n Have You Heard The Tragedy Of Darth Plagueis The Wise?", "\n1) I thought Not",
                         "\n2) Its not a story the Jedi Would tell You", "\n3) Its a Sith Legend",
                         "\n4) The Darkside of the force is a pathway to many abilities some may consider to be un-natural",
                         "4")

    question10 = Question("\nWhat Planet Did the Madalorian Find Grogu on in BobaFett?", "\n1) Nevarro", "\n2) Ahch-to",
                          "\n3) Tython", "\n4) Dathomir", "2")

    p1Q = {question10, question7, question6, question1, question8}
    p2Q = {question5, question4, question3, question9, question2}  # The questions each player will have to answer

    # gameplay loop
    main_score = 0
    player1Score = 0
    player2Score = 0
    while main_score != 10:
        # player 1's turn
        print("Player ones turn")
        for questions in p1Q:
            print(questions)
            guess = input("Enter your guess (Please use numeric values as instructed)")
            for answers in questions.get_correctA():
                if answers == guess:
                    print("Correct Player one")
                    player1Score += 1
                    main_score += 1
                else:
                    main_score += 1
                    print("WRONG")

        # Player 2's turn
        print("Player two's Turn")
        for questions in p2Q:
            print(questions)
            guess = input("Enter your guess (Please use numeric values as instructed)")
            for answers in questions.get_correctA():
                if answers == guess:
                    print("Correct Player 2")
                    player2Score += 1
                    main_score += 1
                else:
                    main_score += 1
                    print("WRONG")

        # determines winner

        if player1Score > player2Score:
            print("THE WINNER IS PLAYER ONE")
        elif player2Score > player1Score:
            print("THE WINNER IS PLAYER TWO")
        else:
            print("ITS A TIE")


main()
