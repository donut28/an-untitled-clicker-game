# this is an untitled clicker game

# Due to hacking concerns, the anti-cheat system has been removed from the Github file. This is to prevent hackers from modifying key variables to gain an advantage.
# The anti-cheat is available on the release version, located on the Releases section.

# important commands / must be run
from tkinter import *
from tkinter import ttk
import time

print("Please do not close this window!")
print("Doing so will stop the entire program, and you will lose your progress.")
print("You have been warned.")

global thingcount
global multiplier
thingcount = 0
upgrade1 = 49
upgrade2 = 99
upgrade3 = 149
upgrade4 = 249
upgrade1count = 0
upgrade2count = 0
upgrade3count = 0
upgrade4count = 0
multiplier = 1
loop = 0


def upgrade1Function():
   global thingcount
   global upgrade1count
   print("Attempted upgrade. Stage 1") 
   if upgrade1 < thingcount:
     print("Attempted upgrade. Stage 2")
     global multiplier
     thingcount = thingcount - 50
     multiplier = multiplier + 1
     upgrade1count = upgrade1count + 1
     updateFunction()
     print("Upgrade successful")
   else:
       print("Error: insufficient things to buy")

def upgrade2Function():
   global thingcount
   global upgrade2count
   print("Attempted upgrade. Stage 1") 
   if upgrade2 < thingcount:
     print("Attempted upgrade. Stage 2")
     global multiplier
     thingcount = thingcount - 100
     multiplier = multiplier + 4
     upgrade2count = upgrade2count + 1
     updateFunction()
     print("Upgrade successful")
   else:
       print("Error: insufficient things to buy")

def upgrade3Function():
   global thingcount
   global upgrade3count
   print("Attempted upgrade. Stage 1") 
   if upgrade3 < thingcount:
     print("Attempted upgrade. Stage 2")
     global multiplier
     thingcount = thingcount - 150
     multiplier = multiplier + 8
     upgrade3count = upgrade3count + 1
     updateFunction()
     print("Upgrade successful")
   else:
       print("Error: insufficient things to buy")

def upgrade4Function():
   global thingcount
   global upgrade4count
   print("Attempted upgrade. Stage 1") 
   if upgrade4 < thingcount:
     print("Attempted upgrade. Stage 2")
     global multiplier
     thingcount = thingcount - 250
     multiplier = multiplier + 16
     upgrade4count = upgrade4count + 1
     updateFunction()
     print("Upgrade successful")
   else:
       print("Error: insufficient things to buy")


def debugFunction():
   print("DEBUG INFORMATION")
   print("thingcount = ")
   print(thingcount)
   print("upgrade1 = ")
   print(upgrade1)
   print("upgrade2 = ")
   print(upgrade2)
   print("upgrade3 = ")
   print(upgrade3)
   print("upgrade1count = ")
   print(upgrade1count)
   print("upgrade2count = ")
   print(upgrade2count)
   print("upgrade3count = ")
   print(upgrade3count)
   print("multiplier = ")
   print(multiplier)



# main code

         
window = Tk()

window.title("untitled clicker game - version 1.0")
window.geometry("450x200+10+20")
window.mainloop
window.resizable(False, False)

lbl=Label(window, text=f'You have: {thingcount} scoops', fg='black', font=("Comic Sans MS", 18))
lbl.place(x=20, y=30)
print("Updated text scoop count. This message should be shown when press the 'click to scoop' button or make a purchase. If it is not, please contact us.")

def updateFunction():
   lbl.config(font=("Comic Sans MS", 18),fg='black',text=f'You have: {thingcount} scoops')
   lbl.place(x=20, y=30)
   print("Updated text scoop count. This message should be shown when press the 'click to scoop' button or make a purchase. If it is not, please contact us.")
   
def addthingFunction():
   global thingcount
   thingcount = thingcount + multiplier
   updateFunction()

btn=Button(window, text="click to scoop", fg='black', height=5, width=20, command=addthingFunction)
btn.place(x=20, y=80)


btn=Button(window, text="bubblegum scoops (50 scoops)", fg='DarkOrchid1', height=1, width=29, command=upgrade1Function)
btn.place(x=200, y=80)

btn=Button(window, text="cookie-dough scoops (100 scoops)", fg='goldenrod1', height=1, width=29, command=upgrade2Function)
btn.place(x=200, y=110)

btn=Button(window, text="rocky road scoops (150 scoops)", fg='orange', height=1, width=29, command=upgrade3Function)
btn.place(x=200, y=140)

btn=Button(window, text="chocolate scoops (250 scoops)", fg='brown', height=1, width=29, command=upgrade4Function)
btn.place(x=200, y=170)

lbll=Label(window, text="scoop upgrades", fg='cyan4', font=("Comic Sans MS", 12))
lbll.place(x=300, y=40)
