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
thingcount = 1
upgrade1 = 49
upgrade2 = 99
upgrade1count = 0
upgrade2count = 0
multiplier = 1
loop = 0


def upgrade1Function():
   global thingcount
   global upgrade1count
   print("Attempted upgrade. Stage 1") 
   if upgrade1 < thingcount:
     print("Attempted upgrade. Stage 2")
     global upgradelock1
     global multiplier
     thingcount = thingcount - 50
     multiplier = multiplier + 1
     upgrade1count = upgrade1count + 1
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
   print("upgradelock1 = ")
   print(upgradelock1)
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


btn=Button(window, text="bubblegum scoop upgrade (50 scoops)", fg='DarkOrchid1', height=1, width=30, command=upgrade1Function)
btn.place(x=175, y=110)

lbll=Label(window, text="scoop upgrades", fg='cyan4', font=("Comic Sans MS", 12))
lbll.place(x=175, y=80)
