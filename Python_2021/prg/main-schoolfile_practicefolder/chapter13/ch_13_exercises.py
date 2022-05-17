"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""
import tkinter

# TODO 13.2 Using the tkinter Module
print("=" * 10, "Section 13.2 using tkinter", "=" * 10)


# Write the code from program 13-2 to display an empty window, no need
# to re-import tkinter. Use the class name MyGUI2


class MyGUI2:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.label = tkinter.Label(self.main_window, text='Devin Grischow')

        self.label.pack()

        tkinter.mainloop()


# TODO 13.3 Adding a label widget
print("=" * 10, "Section 13.3 adding a label widget", "=" * 10)
# Add a label to MyGUI2 (above) that prints your first and last name; pack the label
# Create an instance of MyGUI2
# my_gui = MyGUI2()

# TODO 13.4 Organizing Widgets with Frames
print("=" * 10, "Section 13.4 using frames", "=" * 10)


# Create a MyGUI3 class that creates a window with two frames
# In the top Frame add labels with your name and major
# In the bottom frame add labels with the classes you are taking this semester
# Create an instance of MyGUI3
class MyGUI3:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.frame_one = tkinter.Frame(self.main_window)
        self.frame_two = tkinter.Frame(self.main_window)
        self.major = tkinter.Label(self.frame_one, text="Majoring in science")
        self.minor = tkinter.Label(self.frame_two, text="English, Math, Programming, Web")
        self.major.pack()
        self.minor.pack()
        self.frame_one.pack(side=tkinter.TOP)
        self.frame_two.pack(side=tkinter.BOTTOM)

        tkinter.mainloop()


# mygui = MyGUI3()

# TODO 13.5 Button Widgets and info Dialog Boxes
print("=" * 10, "Section 13.5 button widgets and info dialogs", "=" * 10)


# Create a GUI that will tell a joke
# Use a button to show the punch line, which should appear in a dialog box
# Create an instance of the GUI
class FunnyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.frame_one = tkinter.Frame(self.main_window)
        self.frame_two = tkinter.Frame(self.main_window)
        self.message = tkinter.StringVar()
        self.joke_reveal = tkinter.Label(self.frame_one, textvariable=self.message, width=50, height=30)
        self.joke_reveal.pack()

        self.joke_button = tkinter.Button(self.frame_two, text="wanna hear the greatest joke ever?",
                                          command=self.commedy)
        self.joke_button.pack()
        self.frame_one.pack()
        self.frame_two.pack()
        tkinter.mainloop()

    def commedy(self):
        if self.message.get() == "":
            self.message.set("Why did the chicken cross the road? To get to the bank to take out a loan")


# myfunnygui = FunnyGUI()
# TODO 13.6 getting input / 13.7 Using Labels as output fields
print("=" * 10, "Section 13.6-13.7 input and output using Entry and Label", "=" * 10)


# Using the program in 13.10 kilo converter as a sample,
# create a program to convert inches to centimeters
class InchesConverterGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # Frame group
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # top frame widgets
        self.prompt_label = tkinter.Label(self.top_frame, text="Enter the number you wish to convert in inches: ")
        self.inches_entry = tkinter.Entry(self.top_frame, width=10)

        # pack topframes
        self.prompt_label.pack(side="left")
        self.inches_entry.pack(side="left")

        # middle frame widgets
        self.descr_label = tkinter.Label(self.mid_frame, text="Converted to Centimeters")

        self.value = tkinter.StringVar()

        self.centi_label = tkinter.Label(self.mid_frame, textvariable=self.value)

        # middle frame pack
        self.descr_label.pack(side="left")
        self.centi_label.pack(side="left")

        # bottom button widgets
        self.calculate = tkinter.Button(self.bottom_frame, text="Convert", command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)

        # pack buttons
        self.calculate.pack(side="left")
        self.quit_button.pack(side="left")
        # frames pack
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def convert(self):
        inches = float(self.inches_entry.get())

        centi = inches * 2.54
        self.value.set(str(centi))


converter = InchesConverterGUI()
