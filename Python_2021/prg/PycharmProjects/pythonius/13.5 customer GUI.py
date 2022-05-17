import tkinter

"""
Make up an interface for a business offering 7-10 services or products with prices. Write a GUI program to allow the user to click buttons to add services or products and show total at the
bottom. Make sure all necessary labels and instructions to the user are included in your GUI.
"""

"""
PROGRAM IDEA: design a better smarter gui than samsclub that can tackle two Jobs at once. It will Handle 7 services, while also having a request help button, checkout button, and a call for cart attendant button(will not do logic, will insult user for asking for help)-REDACTED: provided nothing to program- 
Basic program- does not line up with actual pricings, but I still belive its an improvement over the current apps
-this would be for a buisness buying from sams, maybe-
7 items include: 
1: buy indoor furniture - $70
2: buy food - $70
3:buy fireplace - $600
4: buy outdoor stuff - $150
5: buy bulk meat - $25
6: request items outside - $25
7: TMA car help - $70



"""


class SmarterSams:

    def __init__(self):
        self.main_window = tkinter.Tk()

        # frames
        self.indoor_frame = tkinter.Frame(self.main_window)  # each frame needs label and button
        self.food_frame = tkinter.Frame(self.main_window)
        self.fireplace_frame = tkinter.Frame(self.main_window)
        self.outdoor_frame = tkinter.Frame(self.main_window)
        self.meat_frame = tkinter.Frame(self.main_window)
        self.outdoor_help_frame = tkinter.Frame(self.main_window)
        self.tMA_frame = tkinter.Frame(self.main_window)
        self.total_cost_frame = tkinter.Frame(self.main_window)

        # labels and buttons

        self.indoor_label = tkinter.Label(self.indoor_frame, text="Buy indoor Shelving: $70")
        self.food_label = tkinter.Label(self.food_frame, text="Buy bulk food: $70")
        self.fireplace_label = tkinter.Label(self.fireplace_frame, text="Buy fireplace: $600")
        self.outdoor_label = tkinter.Label(self.outdoor_frame, text="Buy outdoor accessories: $150")
        self.meat_label = tkinter.Label(self.meat_frame, text="Buy Bulk Meat: $25")
        self.request_items_label = tkinter.Label(self.outdoor_help_frame, text="request outdoor help: $50")
        self.tma_label = tkinter.Label(self.tMA_frame, text="Fix your car: $70")
        self.total = tkinter.Label(self.total_cost_frame, text="your total cost is: ")

        self.added = tkinter.StringVar()
        self.total_cost_display = tkinter.Label(self.total_cost_frame, textvariable=self.added)

        # pack
        self.indoor_label.pack(side="left")
        self.food_label.pack(side="left")
        self.fireplace_label.pack(side="left")
        self.outdoor_label.pack(side="left")
        self.meat_label.pack(side="left")
        self.request_items_label.pack(side="left")
        self.tma_label.pack(side="left")
        self.request_items_label.pack(side="left")
        self.total.pack()

        # values
        self.indoor_check = tkinter.IntVar()
        self.food_check = tkinter.IntVar()
        self.fireplace_check = tkinter.IntVar()
        self.outdoor_check = tkinter.IntVar()
        self.meat_check = tkinter.IntVar()
        self.outdoor_help_check = tkinter.IntVar()
        self.tMA_check = tkinter.IntVar()

        # buttons

        self.indoor_button = tkinter.Checkbutton(self.indoor_frame, text="add to cart", variable=self.indoor_check)

        self.food_button = tkinter.Checkbutton(self.food_frame, text="add to cart", variable=self.food_check)

        self.fireplace_button = tkinter.Checkbutton(self.fireplace_frame, text="add to cart",
                                                    variable=self.fireplace_check)

        self.outdoor_button = tkinter.Checkbutton(self.outdoor_frame, text="add to cart", variable=self.outdoor_check)

        self.meat_button = tkinter.Checkbutton(self.meat_frame, text="add to cart", variable=self.meat_check)

        self.request_items_button = tkinter.Checkbutton(self.outdoor_help_frame, text="add to cart",
                                                        variable=self.outdoor_help_check)

        self.tma_button = tkinter.Checkbutton(self.tMA_frame, text="add to cart", variable=self.tMA_check)

        self.total_button = tkinter.Button(self.total_cost_frame, text="Calculate Total", command=self.add_together)

        self.indoor_button.pack(side="left")

        self.food_button.pack(side="left")

        self.fireplace_button.pack(side="left")

        self.outdoor_button.pack(side="left")

        self.meat_button.pack(side="left")

        self.request_items_button.pack(side="left")

        self.request_items_button.pack(side="left")

        self.tma_button.pack(side="left")
        self.total_cost_display.pack(side="left")
        self.total_button.pack()

        # pack frames
        self.indoor_frame.pack()  # each frame needs label and button
        self.food_frame.pack()
        self.fireplace_frame.pack()
        self.outdoor_frame.pack()
        self.meat_frame.pack()
        self.outdoor_help_frame.pack()
        self.tMA_frame.pack()
        self.total_cost_frame.pack()

        tkinter.mainloop()

    def add_together(self):
        indoor = 70
        food = 70
        fireplace = 600
        outdoor = 150
        meat = 25
        outdoor_help = 50
        tma = 70
        total = 0
        if self.indoor_check.get() == 1:
            total += indoor
        if self.food_check.get() == 1:
            total += food
        if self.fireplace_check.get() == 1:
            total += fireplace
        if self.outdoor_check.get() == 1:
            total += outdoor
        if self.meat_check.get() == 1:
            total += meat
        if self.outdoor_help_check.get() == 1:
            total += outdoor_help
        if self.tMA_check.get() == 1:
            total += tma
        self.added.set(str(total))


start = SmarterSams()
