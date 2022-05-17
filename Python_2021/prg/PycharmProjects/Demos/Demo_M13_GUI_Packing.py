# this demonstrates using the pack method in a simple GUI
import tkinter
import tkinter.font as tkfont


# define a class for the GUI
class Example:
	# most of the GUI is defined in the init method
	def __init__(self):
		# first, instantiate a window object
		self.gui_window = tkinter.Tk()
		# set a larger size for the default font for better visibility
		default_font = tkfont.nametofont("TkDefaultFont")
		default_font.configure(size=24)

		# now instantiate frames to go in the window
		# the first parameter is the container object (self.gui_window)
		# it is possible to have multiple windows,
		#  -- so the Frame needs to know which window it belongs in
		self.frame0 = tkinter.Frame(self.gui_window)
		self.frame1 = tkinter.Frame(self.gui_window)
		self.frame2 = tkinter.Frame(self.gui_window)

		# ######## First Example ########
		# create four Labels that have frame0 as their container object
		self.label_left = tkinter.Label(self.frame0, text="Left")
		self.label_right = tkinter.Label(self.frame0, text="Right")
		self.label_top = tkinter.Label(self.frame0, text="Top")
		self.label_bottom = tkinter.Label(self.frame0, text="Bottom")

		# pack the frame0 labels in the four directions shown
		self.label_left.pack(side=tkinter.LEFT)
		self.label_right.pack(side=tkinter.RIGHT)
		self.label_top.pack(side=tkinter.TOP)
		self.label_bottom.pack(side=tkinter.BOTTOM)

		# This packs frame0 into the main window
		# if frames are not packed, their contents will not be displayed
		#  -- so, for the first test, show this frame only
		#  -- for the remaining tests, hide this frame and show the others
		#  -- i.e. comment out this line and uncomment the lines below that pack frames 1 and 2
		self.frame0.pack(side=tkinter.BOTTOM)

		# ######## Second Example ########
		# now give frame1 two labels
		self.label1 = tkinter.Label(self.frame1, text="Extra long label")
		self.label2 = tkinter.Label(self.frame1, text="Shorter label")

		# and give frame2 two labels
		self.label3 = tkinter.Label(self.frame2, text="Medium")
		self.label4 = tkinter.Label(self.frame2, text="Hi")

		# now we will see how the pack method works, pack the labels into their frames
		# each object already "knows" which container it belongs to
		# first pack all the labels into their frames on the left side
		self.label1.pack(side=tkinter.LEFT)
		self.label2.pack(side=tkinter.LEFT)
		self.label4.pack(side=tkinter.LEFT)
		self.label3.pack(side=tkinter.LEFT)
		# after changing the packing for frames, change 3 and 4 to TOP, or TOP and LEFT
		# then change all labels to TOP and frames back to LEFT
		# last swap labels 3 & 4 -- note the "column width" doesn't change

		# When ready to test the second example, uncomment the two pack statements below
		self.frame1.pack(side=tkinter.LEFT)
		self.frame2.pack(side=tkinter.LEFT)
		# first frame1 and frame2 are packed into the window on the left side
		# next, try packing frame 2 before frame 1
		# then, try packing them TOP to bottom
		# last, try the options listed above to change how the labels are packed in the frames

		# now that everything is defined and packed, start the mainloop to listen for events
		tkinter.mainloop()


def main():
	# Notice that since there are no widgets in Example that require you to write methods (like buttons)
	#  -- there is only an __init__() method

	# Since the GUI class does all the work,
	#  -- the variable created to instantiate the GUI will not be needed for anything else
	# So, Python provides a special name that can be used to avoid the "not used" warning
	_ = Example()
	print("Notice nothing happens in the console window until I close the GUI window...")


main()
