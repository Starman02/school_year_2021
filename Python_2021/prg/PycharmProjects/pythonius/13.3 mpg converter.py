import tkinter

"""
Write a GUI program that calculates a car’s gas mileage. The program’s window should have Entry widgets that let
the user enter the number of gallons of gas the car holds, and the number of miles it can be driven on a full tank.
When a Calculate MPG button is clicked, the program should display the number of miles that the car may be
driven per gallon of gas. Use the following formula to calculate miles per gallon:

MPG = miles / gallons

Make sure you label Entry widgets and results appropriately and document with comments.
"""


class MPGcalc:

    def __init__(self):

        self.main_window = tkinter.Tk()

        # frames
        self.frame_top = tkinter.Frame(self.main_window)
        self.frame_middle = tkinter.Frame(self.main_window)
        self.frame_bottom = tkinter.Frame(self.main_window)

        # label for top frames
        self.galons_label = tkinter.Label(self.frame_top, text="Enter how many gallons your car can hold")
        self.miles_label = tkinter.Label(self.frame_middle, text="Enter how many miles you have traveled")
        self.convert_label = tkinter.Label(self.frame_bottom, text="Converted to Miles per gallons: ")

        # displays string var for display
        self.converted = tkinter.StringVar()
        self.converted_display = tkinter.Label(self.frame_bottom, textvariable=self.converted)

        # pack labels
        self.galons_label.pack(anchor=tkinter.CENTER)
        self.miles_label.pack(anchor=tkinter.CENTER)
        self.convert_label.pack(side="left")
        self.converted_display.pack(side="left")

        # text entry
        self.galons_entry = tkinter.Entry(self.frame_top)

        self.miles_entry = tkinter.Entry(self.frame_middle)

        # pack entrys
        self.galons_entry.pack()
        self.miles_entry.pack()

        # buttons
        self.convert_button = tkinter.Button(self.frame_bottom, text="Convert", command=self.galontompg)
        self.quit_button = tkinter.Button(self.frame_bottom, text="Quit?", command=self.main_window.destroy)

        # pack buttons and frames
        self.convert_button.pack(side="left")
        self.quit_button.pack(side="left")
        self.frame_top.pack()
        self.frame_middle.pack()
        self.frame_bottom.pack()

        tkinter.mainloop()

    def galontompg(self):
        try:
            galon_entry = float(self.galons_entry.get())
            miles_entry = float(self.miles_entry.get())

            if galon_entry == "" or miles_entry == "":
                self.converted.set("invalid entry")

            else:
                # hidden variables to store galons and miles
                __galonstorage = float(self.galons_entry.get())
                __milesstorage = float(self.miles_entry.get())
                milesPgalon = __milesstorage / __galonstorage
                self.converted.set(str(milesPgalon))
        except ValueError:
            self.converted.set("Data is invalid")


start = MPGcalc()
