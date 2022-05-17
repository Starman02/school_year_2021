# this will demonstrate using simple buttons in a GUI
import tkinter
import tkinter.font as tkfont


# set up the class
class ButtonWars:
	# set up the GUI in the init
	def __init__(self):
		# first create an instance of Tk()
		#  -- to initialize access to the library of tkinter widgets (classes)
		#  -- and provide a master GUI window
		self.main_window = tkinter.Tk()
		# there are many options not included in your book, e.g. title
		self.main_window.title("Button Wars")
		# this sets a new size for the default font for better visibility
		# not required for your projects, but helpful in the classroom
		default_font = tkfont.nametofont("TkDefaultFont")
		default_font.configure(size=24)

		# add a couple of Frames to help organize the contents in the main_window
		# for those who know HTML, Frames are similar to divs
		self.frame_top = tkinter.Frame(self.main_window)
		self.frame_bottom = tkinter.Frame(self.main_window)

		# add a Label to the top frame. It will be used to display a message
		# so, we assign a string variable (StringVar) to the Label using textvariable
		#  -- the variable provides a getter and setter to get and set the text
		#  -- if no starting text is specified, it starts with an empty string
		self.message = tkinter.StringVar()
		self.message_area = tkinter.Label(self.frame_top, textvariable=self.message, width=20)

		# pack the label into its parent container (the top frame)
		self.message_area.pack()

		# add buttons to the bottom frame -- the text displays on the button itself
		# the command option assigns a method to be called when the button is pressed
		self.me_button = tkinter.Button(self.frame_bottom, text="Push Me!", command=self.push_me)
		self.no_me_button = tkinter.Button(self.frame_bottom, text="No! Push Me!", command=self.no_push_me)
		# this quit button calls a built-in method to destroy the window -- and end the mainloop()
		self.quit_button = tkinter.Button(self.frame_bottom, text="Give Up", command=self.main_window.destroy)


		# pack the buttons into their containers -- default side is TOP
		self.me_button.pack()
		self.no_me_button.pack()
		self.quit_button.pack()

		# pack the frames in order from top to bottom -- default side is TOP
		self.frame_top.pack()
		self.frame_bottom.pack()

		# initiate the listening loop
		# remember, this is essentially an infinite loop that "listens" for events to occur
		# it will not exit until the quit_button command calls destroy on the main_window
		tkinter.mainloop()

	# define a method to be called for the me_button
	def push_me(self):
		if self.message.get() == "":
			self.message.set("Wise choice!")
		else:
			self.message.set("That's what you think!")

	# define a method to be called for the no_me_button
	def no_push_me(self):
		self.message.set("Haha! I win!")


def main():
	# When I instantiate the ButtonWars class, all of the GUI objects in it will be instantiated
	#  -- and mainloop() will be called.
	# Once mainloop() is called, the program waits for an event
	#  -- (a button press, keystroke, mouse click, etc.)
	#  -- and the relevant object is notified to handle the event.
	# Most of the events are handled automatically by the built-in code associated with the tkinter
	#  -- library of objects. For example, you do not have to write the code that allows you to
	#  -- type text into an Entry box.
	# For this course, you will be providing code for actions like button clicks.

	# since the GUI does all the work, I just need to instantiate the GUI
	button_wars = ButtonWars()


main()
