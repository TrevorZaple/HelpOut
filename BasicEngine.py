class Chore:
    def __init__(self, name, value, setting, classif):
        self.name = name
        self.value = value
        self.setting = setting
        self.classif = classif
        
####################
## GLOBALS        ##
####################

#Chore List: Tier One

chore1 = Chore("Water the Garden", 15, "outdoor", 1)
chore2 = Chore("Feed Pets", 15, "indoor", 1)
chore3 = Chore("Clean the Kitchen Counter", 15, "indoor", 1)
chore4 = Chore("Clean the Dining Table", 15, "indoor", 1)
chore5 = Chore("Sweep the Kitchen", 15, "indoor", 1)
chore6 = Chore("Sweep the Floors", 15, "indoor", 1)
chore7 = Chore("Vaccuum Rugs", 15, "indoor", 1)
chore8 = Chore("Clean Your Bedroom (incl. making bed)", 15, "indoor", 1)
chore9 = Chore("Empty All Your Trash Cans", 15, "indoor", 1)
chore10 = Chore("Clean Out The Car", 30, "outdoor", 1)
chore11 = Chore("Tidy Up Baskets in the Front Hall and Shoes", 15, "indoor", 1)
chore12 = Chore("Pick Up All The Floor Laundry", 15, "indoor", 1)
chore13 = Chore("Put Away Toys and Electronics", 15, "indoor", 1)
chore14 = Chore("Put Away Blankets and Pillows", 15, "indoor", 1)
chore15 = Chore("Unload the Dishwasher", 30, "indoor", 1)
chore16 = Chore("Clean the Bathroom", 30, "indoor", 1)
chore17 = Chore("Fold a Load of Laundry", 15, "indoor", 1)
chore18 = Chore("Clean Up Backyard", 30, "outdoor", 1)

#Chore List: Tier Two

chore19 = Chore("Read a Book for 30 Minutes", 30, "indoor", 2)
chore20 = Chore("Do Something Creative", 30, "indoor", 2)
chore21 = Chore("Play a Sport", 30, "outdoor", 2)
chore22 = Chore("Play a Board Game (basic level)", 30, "indoor", 2)
chore23 = Chore("Play a Board Game (advanced level)", 60, "indoor", 2)
chore24 = Chore("Do Extra Credit School Work", 30, "indoor", 2)
chore25 = Chore("Play With Your Sister", 60, "indoor", 2)
chore26 = Chore("Go Get Some Exercise", 30, "outdoor", 2)

def chore(chorenumber):
    incr = chorenumber.value
    if chorenumber.classif == 1:
        TierOneBank += incr
    elif chorenumber.classif == 2:
        TierTwoBank += incr
        


TierOneBank = 15

TierTwoBank = 0

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("HelpOut 0.01")

mainframe = ttk.Frame(root, padding ="3 3 12 12")
mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

minutes_remaining = StringVar()

def refresh(*args):
    try:
        value = float(TierOneBank + TierTwoBank)
        minutes_remaining.set(value)
    except ValueError:
        pass

ttk.Button(mainframe, text = "Refresh", command = refresh).grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, text = "You have ").grid(column = 3, row = 1, sticky = W)
ttk.Label(mainframe, textvariable = minutes_remaining).grid(column = 2, row = 2, sticky = (W, E))
ttk.Label(mainframe, text = "Minutes Remaining.").grid(column = 3, row = 2, sticky = W)

ttk.Label(mainframe, text = "Chore List").grid(column = 3, row = 4, sticky = W)
ttk.Label(mainframe, text = "Click When Completed").grid(column = 3, row = 5, sticky = W)


for child in mainframe.winfo_children(): child.grid_configure(padx = 5, pady = 5)

root.mainloop()



