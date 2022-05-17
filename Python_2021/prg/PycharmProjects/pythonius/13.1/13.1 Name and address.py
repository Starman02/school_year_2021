import tkinter

"""
Write a GUI program that displays your name and address when a button is clicked (you can use the address of the school). The
program’s window should resemble the sketch on the far left side of figure 13-26 when it runs. When the user clicks the Show Info
button, the program should display your name and address as shown in the sketch on the right of the figure.
"""


class NameNaddress:
    def __init__(self):
        # main window
        self.main_window = tkinter.Tk()

        # two frames for the different areas, top frame will display address, bottom buttons
        self.frame_top = tkinter.Frame(self.main_window)
        self.frame_bottom = tkinter.Frame(self.main_window)

        # name and address label + variables

        self.name = tkinter.StringVar()
        self.address = tkinter.StringVar()
        self.name_label = tkinter.Label(self.frame_top, textvariable=self.name, width=30)
        self.address_label = tkinter.Label(self.frame_top, textvariable=self.address, width=30)

        # pack label areas
        self.name_label.pack()
        self.address_label.pack()

        # singular button
        self.reveal_info = tkinter.Button(self.frame_bottom, text="Reveal Name and Adress", command=self.activate)
        # quit button
        self.quit_button = tkinter.Button(self.frame_bottom, text="Quit?", command=self.main_window.destroy)

        # pack buttons and frames
        self.reveal_info.pack(side=tkinter.LEFT)
        self.quit_button.pack(side=tkinter.RIGHT)
        self.frame_top.pack()
        self.frame_bottom.pack()

        # start gui
        tkinter.mainloop()

    def activate(self):
        self.name.set("Devin Grischow")
        self.address.set("8900 US-14, Crystal Lake, IL 60012")


gui = NameNaddress()
