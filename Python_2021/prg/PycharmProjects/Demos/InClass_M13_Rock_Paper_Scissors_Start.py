from tkinter import *
import tkinter.font as tkfont
import random


class RockPaperScissors:
    # the following class-level attributes are for convenience and to provide readability to the code
    # class attributes are like global variables (or constants) for a class
    # by setting global constants, I can use the variable name in the code rather than a number
    __ROCK = 0
    __PAPER = 1
    __SCISSORS = 2

    # global constants indicating the winner of the round
    __PLAYER = 0
    __COMPUTER = 1
    __TIE = -1

    # create a class-level dictionary to translate the numeric choice to a word
    __translate_choice = {__ROCK: "rock", __PAPER: "paper", __SCISSORS: "scissors"}

    # create a class-level dictionary of game results based on the player choice
    # KEY is the player's choice
    # VALUE returned is winner based on the computer's choice of: [ROCK, PAPER, SCISSORS]
    __winner_by_player = {__ROCK: [__TIE, __COMPUTER, __PLAYER], __PAPER: [__PLAYER, __TIE, __COMPUTER],
                          __SCISSORS: [__COMPUTER, __PLAYER, __TIE]}

    # create a class-level dictionary to translate the numeric winner result to a phrase
    __translate_winner = {__PLAYER: "Player wins!", __COMPUTER: "Computer wins!", __TIE: "The game is a tie."}

    # the __init__(self) method instantiates and initializes an instance of the class
    def __init__(self):
        # instantiate Tkinker
        self.__main_window = Tk()
        self.__main_window.title("Rock, Paper, Scissors")
        # create instance variables to hold the current choices
        self.__player_choice = 0
        self.__computer_choice = 0
        # create instance variables to hold the current scores
        self.__player_score = 0
        self.__computer_score = 0
        # these statements tell Tkinter to use a larger size for the default font
        default_font = tkfont.nametofont("TkDefaultFont")
        default_font.configure(size=70)

        # set up the contents of the window
        # create a frame and three buttons to go in it
        # Tkinter uses named parameters to allow you to only specify the ones you need
        self.__button_frame = Frame(self.__main_window)
        self.__rock_button = Button(self.__button_frame, text="ROCK", command=self.chose_rock)
        self.__paper_button = Button(self.__button_frame, text="PAPER", command=self.chose_paper)
        self.__scissors_button = Button(self.__button_frame, text="SCISSORS", command=self.chose_scissors)

        # pack the buttons into their frame
        # like an HTML margin, the padx and pady parameters adds spacing around the widget
        #  -- if you want different spacing to left and right, you can provide a tuple: padx=(10,20)
        self.__rock_button.pack(side=LEFT, padx=10)
        self.__paper_button.pack(side=LEFT, padx=50)
        self.__scissors_button.pack(side=LEFT, padx=10)

        # create a label to hold a status message
        self.__status_frame = Frame(self.__main_window)
        self.__status_msg = StringVar()
        self.__status_label = Label(self.__status_frame, textvariable=self.__status_msg)
        self.__status_label.pack(side=TOP)

        # create a frame for the player scores on top
        self.__top_frame = Frame(self.__main_window)

        # make labels to display the player and computer scores
        # width 20 is given for labels to prevent auto-resizing as length of text changes
        self.__left_frame = Frame(self.__top_frame)
        self.__computer_msg = StringVar()
        self.__computer_label = Label(self.__left_frame, textvariable=self.__computer_msg, width=20)
        self.__computer_label.pack(side=TOP)

        self.__right_frame = Frame(self.__top_frame)
        self.__player_msg = StringVar()
        self.__player_label = Label(self.__right_frame, textvariable=self.__player_msg, width=20)
        self.__player_label.pack(side=TOP)

        # now pack the left and right frames into the top frame
        self.__left_frame.pack(side=LEFT)
        self.__right_frame.pack(side=RIGHT)
        # and pack the remaining frames into the main window
        self.__top_frame.pack(side=TOP)
        self.__status_frame.pack(side=TOP)
        self.__button_frame.pack(side=TOP)

        # now initialize starting messages and start the GUI loop
        self.__computer_msg.set("Computer :: " + format(self.__computer_score, "3d"))
        self.__player_msg.set("Player :: " + format(self.__player_score, "3d"))
        self.__status_msg.set("Ready to play!\n")
        mainloop()

    def chose_rock(self):
        self.__player_choice = RockPaperScissors.__ROCK
        self.process_choice()

    def chose_paper(self):
        self.__player_choice = RockPaperScissors.__PAPER
        self.process_choice()

    def chose_scissors(self):
        self.__player_choice = RockPaperScissors.__SCISSORS
        self.process_choice()

    def process_choice(self):
        # get a random choice for the computer (0, 1, or 2)
        self.__computer_choice = random.randint(0, 2)

        # get the winner based on player and computer choices
        winner = RockPaperScissors.__winner_by_player[self.__player_choice][self.__computer_choice]

        # update the scores and display them
        if winner == RockPaperScissors.__PLAYER:
            self.__player_score += 1
            self.__player_msg.set("Player :: " + format(self.__player_score, "3d"))
        elif winner == RockPaperScissors.__COMPUTER:
            self.__computer_score += 1
            self.__computer_msg.set("Computer :: " + format(self.__computer_score, "3d"))

        # update the status message
        new_message = "You chose " + RockPaperScissors.__translate_choice[self.__player_choice] + \
                      ". The computer chose " + RockPaperScissors.__translate_choice[self.__computer_choice] + \
                      ".\n" + RockPaperScissors.__translate_winner[winner]

        self.__status_msg.set(new_message)


game = RockPaperScissors()
