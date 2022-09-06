# this is an untitled clicker game

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
upgrade5 = 499
upgrade6 = 1999
upgrade1count = 0
upgrade2count = 0
upgrade3count = 0
upgrade4count = 0
upgrade5count = 0
upgrade6count = 0
multiplier = 1
loop = 0











































# For security reasons, the anti-cheat system has been redacted.
# This is to prevent hackers from looking at the system to circumvent it.
# You can download the version with anti-cheat via the Releases tab.
# Apologies.

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

def upgrade5Function():
   global thingcount
   global upgrade5count
   global checksum
   print("Attempted upgrade. Stage 1") 
   if upgrade5 < thingcount:
     print("Attempted upgrade. Stage 2")
     global multiplier
     thingcount = thingcount - 1000
     multiplier = multiplier + 50
     upgrade5count = upgrade5count + 1
     updateFunction()
     print("Upgrade successful")
   else:
       print("Error: insufficient things to buy")

def upgrade6Function():
   global thingcount
   global upgrade6count
   print("Attempted upgrade. Stage 1") 
   if upgrade5 < thingcount:
     print("Attempted upgrade. Stage 2")
     global multiplier
     thingcount = thingcount - 2000
     multiplier = multiplier + 146
     upgrade6count = upgrade6count + 1
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
   print("upgrade4 = ")
   print(upgrade4)
   print("upgrade5 = ")
   print(upgrade5)
   print("upgrade6 = ")
   print(upgrade6)
   print("upgrade1count = ")
   print(upgrade1count)
   print("upgrade2count = ")
   print(upgrade2count)
   print("upgrade3count = ")
   print(upgrade3count)
   print("upgrade4count = ")
   print(upgrade4count)
   print("upgrade5count = ")
   print(upgrade5count)
   print("upgrade6count = ")
   print(upgrade6count)
   print("multiplier = ")
   print(multiplier)



# main code

         
window = Tk()

window.title("untitled clicker game - version 1.3")
window.geometry("440x300+10+20")
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
   global checksum
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

btn=Button(window, text="strawberry scoops (1000 scoops)", fg='pink2', height=1, width=29, command=upgrade5Function)
btn.place(x=200, y=200)

btn=Button(window, text="neapolitan scoops (2000 scoops)", fg='blue', height=1, width=29, command=upgrade6Function)
btn.place(x=200, y=230)

lbll=Label(window, text="scoop upgrades", fg='cyan4', font=("Comic Sans MS", 12))
lbll.place(x=300, y=40)

lbl3=Label(window, text="anti-cheat deactivated", fg='cyan4', font=("Comic Sans MS", 10, 'bold'))
lbl3.place(x=20, y=170)

lbl4=Label(window, text="use releases version to activate", fg='cyan4', font=("Comic Sans MS", 7))
lbl4.place(x=20, y=190)

