import tkinter
import tkinter.messagebox
import tkinter.font as tkfont
import pickle

"""



"""


# main (root) GUI menu
class CrudGUI:
    def __init__(self, master):
        # the primary window (master) was initialized in the main() program
        #  -- save the master parameter in an instance variable to make it available throughout the class
        self.master = master
        self.master.title('Welcome Menu')

        # these statements tell Tkinter what font size to use for the default font
        default_font = tkfont.nametofont("TkDefaultFont")
        # use a larger size value for better visibility
        default_font.configure(size=13)

        # create two frames -- one for the menu, one for the buttons
        self.top_frame = tkinter.Frame(self.master)
        self.bottom_frame = tkinter.Frame(self.master)

        # the menu uses Radiobuttons so that only one option is selected at any time -- start by selecting option 1
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        # create the radio buttons
        self.look = tkinter.Radiobutton(self.top_frame, text='Look up customer',
                                        variable=self.radio_var, value=1)
        self.add = tkinter.Radiobutton(self.top_frame, text='Add Customer',
                                       variable=self.radio_var, value=2)
        self.change = tkinter.Radiobutton(self.top_frame, text='Change customer email',
                                          variable=self.radio_var, value=3)
        self.delete = tkinter.Radiobutton(self.top_frame, text='Delete customer',
                                          variable=self.radio_var, value=4)

        # for visibility at a larger scale, you can turn off the radiobutton indicator (icon)
        #  -- resulting in a push-button look
        #  -- (Tkinter also provides the option to provide your own images for the icons)
        self.look.configure(indicatoron=0)
        self.add.configure(indicatoron=0)
        self.change.configure(indicatoron=0)
        self.delete.configure(indicatoron=0)

        # pack the radio buttons
        self.look.pack(anchor='w', padx=20)
        self.add.pack(anchor='w', padx=20)
        self.change.pack(anchor='w', padx=20)
        self.delete.pack(anchor='w', padx=20)

        # create ok and quit buttons
        self.ok_button = tkinter.Button(self.bottom_frame, text='OK', command=self.open_menu, width=10)
        self.quit_button = tkinter.Button(self.bottom_frame, text='QUIT', command=self.master.destroy, width=10)

        # pack the buttons
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

    # this method is called to process the menu choice when the OK button is pressed
    # you will need to modify this method to process the other menu options based on the radio button selection
    #  -- each menu item should be instantiated as an appropriate class similar to the example provided
    def open_menu(self):
        if self.radio_var.get() == 1:
            _ = LookGUI(self.master)
        elif self.radio_var.get() == 2:
            _ = Add_customer(self.master)
        elif self.radio_var.get() == 3:
            _ = Change_customer_entry(self.master)
        else:
            tkinter.messagebox.showinfo('Function', 'still under construction')


# This example class processes the first user choice -- to look for a name
class LookGUI:
    def __init__(self, master):

        # open the file, load to customers, close file. Do this in each class
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.customers = {}

        # tkinter.Toplevel() is like tkinter.Frame() but it opens in a new window
        # when the Toplevel window is closed, it returns focus to the master window
        self.look = tkinter.Toplevel(master)
        self.look.title('Search for customer')

        # create Frames for this Toplevel window
        self.top_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        # widgets for top frame - label and entry box for name
        self.search_label = tkinter.Label(self.top_frame, text='Enter customer name to look for: ')
        # Entry box uses its own font settings, so tell it to use the TkDefaultFont we set for the primary window
        self.__search_entry = tkinter.Entry(self.top_frame, width=15, font="TkDefaultFont")

        # pack top frame
        self.search_label.pack(side='left')
        self.__search_entry.pack(side='left')

        # middle frame - label for results
        self.info_string = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='Results: ')
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.info_string)

        # pack Middle frame
        self.info.pack(side='left')
        self.result_label.pack(side='left')

        # buttons for bottom frame
        self.search_button = tkinter.Button(self.bottom_frame, text='Search', command=self.search, width=10)
        self.back_button = tkinter.Button(self.bottom_frame, text='Return To Menu', command=self.go_back, width=10)

        # pack bottom frame
        self.search_button.pack(side='left')
        self.back_button.pack(side='left')

        # pack frames into the Toplevel window
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    # this method is called by the Search button
    def search(self):
        # get the data from the entry box
        name = self.__search_entry.get()
        # look for the name in the dictionary
        if name in self.customers:
            result = self.customers.get(name)
        else:
            result = self.customers.get(name, 'Not Found')
        # display the result in the info label by setting its associated StringVar
        self.info_string.set(result)

    # this method is called by the Main Menu button to destroy the current window and return to the primary
    def go_back(self):
        self.look.destroy()





class Add_customer:
    def __init__(self, master):

        # open the file, load to customers, close file. Do this in each class
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.customers = {}

        # tkinter.Toplevel() is like tkinter.Frame() but it opens in a new window
        # when the Toplevel window is closed, it returns focus to the master window
        self.look = tkinter.Toplevel(master)
        self.look.title('Add name to database')

        # create Frames for this Toplevel window
        self.top_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        # widgets for top frame - label and entry box for name
        self.name_addition_label = tkinter.Label(self.top_frame, text='Enter your name: ')
        self.email_addition_label = tkinter.Label(self.top_frame, text='Enter your Email: ')
        # Entry box uses its own font settings, so tell it to use the TkDefaultFont we set for the primary window
        self.add_name_entry = tkinter.Entry(self.top_frame, width=15, font="TkDefaultFont")
        self.__add_email_entry = tkinter.Entry(self.top_frame, width=15, font="TkDefaultFont")

        # pack top frame
        self.name_addition_label.pack(side='left')
        self.add_name_entry.pack(side='left')
        self.email_addition_label.pack(side="left")
        self.__add_email_entry.pack(side="left")

        # middle frame - label for results
        self.info_string = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='Status: ')
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.info_string)

        # pack Middle frame
        self.info.pack(side='left')
        self.result_label.pack(side='left')

        # buttons for bottom frame
        self.search_button = tkinter.Button(self.bottom_frame, text='Add and Save', command=self.addition, width=10)
        self.back_button = tkinter.Button(self.bottom_frame, text='Return To Menu', command=self.go_back, width=10)

        # pack bottom frame
        self.search_button.pack(side='left')
        self.back_button.pack(side='left')

        # pack frames into the Toplevel window
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    # this method is called by the addition button
    def addition(self):
        # get the data from the entry box
        name = self.add_name_entry.get()
        email = self.__add_email_entry.get()
        mainmail = {name : email} # stores the dictionary
        #Save items to file
        save_file = open("customer_file.dat", "wb")
        pickle.dump(mainmail, save_file)
        save_file.close()
        self.info_string.set("data saved and added to database")

        # display the result in the info label by setting its associated StringVar
        # self.info_string.set(result)

    # this method is called by the Main Menu button to destroy the current window and return to the primary
    def go_back(self):
        self.look.destroy()




class Change_customer_entry:
    def __init__(self, master):

        # open the file, load to customers, close file. Do this in each class
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.customers = {}

        # tkinter.Toplevel() is like tkinter.Frame() but it opens in a new window
        # when the Toplevel window is closed, it returns focus to the master window
        self.look = tkinter.Toplevel(master)
        self.look.title('Change Customer Entry')

        # create Frames for this Toplevel window
        self.top_frame = tkinter.Frame(self.look) # search frame
        self.result_frame = tkinter.Frame(self.look) # result frame for email and status
        self.button_frame = tkinter.Frame(self.look) # search button, save/replace button, quit button
        self.email_frame = tkinter.Frame(self.look) # new email name

        # widgets for top frame - label and entry box for name


        # search for original name (TODO: idea: input name you wish to change and then underneath have the new name and email, to finish program press one button, so the first frame would be a spot for the og name, underneath would be the new name and new email entry boxes)

        self.search_label = tkinter.Label(self.top_frame, text='Enter customer name to look for: ')
        # search entry
        self.__search_entry = tkinter.Entry(self.top_frame, width=15, font="TkDefaultFont")
        # enter ***NEW EMAIL****

        # Entry box uses its own font settings, so tell it to use the TkDefaultFont we set for the primary window
        # pack top frame
        self.search_label.pack(side='left')
        self.__search_entry.pack(side='left')


        # result frame - label for results
        self.info_string = tkinter.StringVar()
        self.info = tkinter.Label(self.result_frame, text='Status: ')
        self.result_label = tkinter.Label(self.result_frame, textvariable=self.info_string)

        # pack result frame
        self.info.pack(side='left')
        self.result_label.pack(side="left")

        # buttons for buttom frame
        self.search_button = tkinter.Button(self.button_frame, text='Search', command=self.search, width=10)
        self.add_button = tkinter.Button(self.button_frame, text='Add and Save', command=self.addition, width=10)
        self.back_button = tkinter.Button(self.button_frame, text='Return To Menu', command=self.go_back, width=10)

        # pack bottom frame
        self.search_button.pack(side='left')
        self.add_button.pack(side='left')
        self.back_button.pack(side='left')

        # new email label and entry
        self.email_addition_label = tkinter.Label(self.email_frame, text='Enter your NEW Email: ')
        self.__add_email_entry = tkinter.Entry(self.email_frame, width=15, font="TkDefaultFont")

        # pack email and label
        self.email_addition_label.pack(side="left")
        self.__add_email_entry.pack(side="left")

        # pack frames into the Toplevel window
        self.top_frame.pack()
        self.result_frame.pack()
        self.button_frame.pack()
        self.email_frame.pack()

    # this method is called by the addition button
    def addition(self):
        name = self.__search_entry.get()
        email = self.__add_email_entry
        # get the data from the entry box
        # get the data from the entry box
        try:
            if email == "":
                self.info_string.set("Entry Failed to save")
            else:
                mainmail = {name : email} # stores the dictionary
                #Save items to file
                save_file = open("customer_file.dat", "wb")
                pickle.dump(mainmail, save_file)
                save_file.close()
                self.info_string.set("data saved and added to database")
        except:
            self.info_string.set("file failed to save")

    def search(self):
        # get the data from the entry box
        name = self.__search_entry.get()
        # look for the name in the dictionary
        if name in self.customers:
            result = self.customers.get(name)
        else:
            result = self.customers.get(name, 'Not Found')
        # display the result in the info label by setting its associated StringVar
        self.info_string.set(result)

        # display the result in the info label by setting its associated StringVar
        # self.info_string.set(result)

    # this method is called by the Main Menu button to destroy the current window and return to the primary
    def go_back(self):
        self.look.destroy()


# you need to create classes similar to the LookGUI class for the other tasks: Create, Update, Delete
# the logic to process each choice for the OK button should be
#  -- similar to your logic used in your 9.1 Name and Email Address program
# Remember to pickle your data file after each change to the dictionary as you did in 9.1


def main():
    # create a window and initialize the Tk library
    root = tkinter.Tk()
    # call the GUI and send it the root window
    # use _ as variable name because the variable will not be needed after instantiating GUI
    # the GUI itself will handle the remaining program logic
    _ = CrudGUI(root)
    # because the root window was initialized here, we control the mainloop from main instead of the class
    root.mainloop()


main()
