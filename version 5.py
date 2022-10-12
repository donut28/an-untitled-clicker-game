# welcome to an untitled clicker game
# this is a game about clicking a button.
# thats it.

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
employeelock = 1
upgrade2 = 99
upgrade3 = 149
upgrade4 = 499
upgrade5 = 999
upgrade6 = 4999
employee1 = 9999
employee2 = 19999
rebirth = 4999
rebirth_unlock = 0
upgrade1count = 0
upgrade2count = 0
employee1count = 0
upgrade3count = 0
upgrade4count = 0
upgrade5count = 0
upgrade6count = 0
multiplier = 1
loop = 0
cps = 0  # clicks per second


# nice


def upgrade1Function():
    global thingcount
    global upgrade1count
    global checksum
    global checksum_multiplier
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
    global checksum
    global checksum_multiplier
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
        thingcount = thingcount - 500
        multiplier = multiplier + 16
        upgrade4count = upgrade4count + 1

        updateFunction()
        print("Upgrade successful")
    else:
        print("Error: insufficient things to buy")


def upgrade5Function():
    global thingcount
    global upgrade5count
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


def employee1Function():
    global thingcount
    global checksum
    global employeelock
    print("Attempted upgrade. Stage 1")
    if employee1 < thingcount:
        print("Attempted upgrade. Stage 2")
        if rebirth_unlock == 1:
            global employee1count
            thingcount = thingcount - 10000
            employee1count = employee1count + 1
            employeelock = 0

            updateFunction()
            print("Upgrade successful")

    else:
        print("Error: insufficient things to buy")


def upgrade6Function():
    global thingcount
    global upgrade6count
    print("Attempted upgrade. Stage 1")
    if upgrade6 < thingcount:
        print("Attempted upgrade. Stage 2")
        global multiplier
        thingcount = thingcount - 5000
        multiplier = multiplier + 146
        upgrade6count = upgrade6count + 1

        updateFunction()
        print("Upgrade successful")
    else:
        print("Error: insufficient things to buy")


def rebirthFunction():
    global thingcount
    global rebirth_unlock
    global checksum
    print("Attempted upgrade. Stage 1")
    if upgrade6count > 0:
        print("Attempted upgrade. Stage 2")
        global multiplier
        thingcount = thingcount = 1
        multiplier = multiplier = 1
        rebirth_unlock = 1

        updateFunction()
        print("Upgrade successful")
    else:
        print("Error: insufficient things to buy")


def placeholderFunction():
    print("")


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

window.title("untitled clicker game - version 1.4")
window.geometry("700x300+10+20")
window.mainloop
window.resizable(False, False)

lbl = Label(window, text=f'You have: {thingcount} scoops', fg='black', font=(
    "Comic Sans MS", 18))
lbl.place(x=20, y=30)
print("Updated text scoop count. This message should be shown when press the 'click to scoop' button or make a purchase. If it is not, please contact us.")


def updateFunction():
    global thingcount
    lbl.config(font=("Comic Sans MS", 18), fg='black',
               text=f'You have: {thingcount} scoops')
    lbl.place(x=20, y=30)
    print("Updated text scoop count. This message should be shown when press the 'click to scoop' button or make a purchase. If it is not, please contact us.")


def employeeTick():
    global thingcount
    if employee1count > 0:
        thingcount = thingcount + 250
        updateFunction()
    window.after(2000, employeeTick)


employeeTick()


def anticheatFunction():
    if cps >= 8:
        print("Error: CPS too high")
        print("You have been warned.")
        print("Exiting...")
        time.sleep(5)
        exit()
    window.after(10, anticheatFunction)


anticheatFunction()


def resetCps():
    global cps
    cps = 0
    window.after(1000, resetCps)


def cpsCounter(event):
    global cps
    cps += 1


def addthingFunction():
    global thingcount
    thingcount = thingcount + multiplier
    updateFunction()


resetCps()

window.bind_all('<1>', cpsCounter)

btn = Button(window, text="click to scoop", fg='black',
             height=5, width=20, command=addthingFunction)
btn.place(x=20, y=80)


btn = Button(window, text="bubblegum scoops (50 scoops)",
             fg='DarkOrchid1', height=1, width=29, command=upgrade1Function)
btn.place(x=200, y=80)

btn = Button(window, text="cookie-dough scoops (100 scoops)",
             fg='goldenrod1', height=1, width=29, command=upgrade2Function)
btn.place(x=200, y=110)

btn = Button(window, text="rocky road scoops (150 scoops)",
             fg='orange', height=1, width=29, command=upgrade3Function)
btn.place(x=200, y=140)

btn = Button(window, text="chocolate scoops (500 scoops)",
             fg='brown', height=1, width=29, command=upgrade4Function)
btn.place(x=200, y=170)

btn = Button(window, text="strawberry scoops (1000 scoops)",
             fg='pink2', height=1, width=29, command=upgrade5Function)
btn.place(x=200, y=200)

btn = Button(window, text="neapolitan scoops (5000 scoops)",
             fg='blue', height=1, width=29, command=upgrade6Function)
btn.place(x=200, y=230)

lbll = Label(window, text="scoop upgrades",
             fg='cyan4', font=("Comic Sans MS", 12))
lbll.place(x=300, y=40)

lbl3 = Label(window, text="anti-cheat deactivated",
             fg='cyan4', font=("Comic Sans MS", 10, 'bold'))
lbl3.place(x=20, y=170)

lbl4 = Label(window, text="use releases version to activate",
             fg='cyan4', font=("Comic Sans MS", 7, 'bold'))
lbl4.place(x=20, y=190)

lbl6 = Label(window, text="any runs with this disclaimer should",
             fg='cyan4', font=("Comic Sans MS", 7))
lbl6.place(x=20, y=210)

lbl6 = Label(window, text="be disqualified",
             fg='cyan4', font=("Comic Sans MS", 7))
lbl6.place(x=20, y=225)

btn = Button(window, text="rebirth (must have neapolitan)",
             fg='blue', height=1, width=23, command=rebirthFunction)
btn.place(x=20, y=255)


#lbl4=Label(window, text=f'multiplier x{multiplier}', fg='cyan4', font=("Comic Sans MS", 7))
#lbl4.place(x=20, y=190)


lbl4 = Label(window, text="employees", fg='magenta',
             font=("Comic Sans MS", 10))
lbl4.place(x=450, y=40)

lbl5 = Label(window, text="must rebirth to buy",
             fg='blue', font=("Comic Sans MS", 7))
lbl5.place(x=450, y=60)

btn = Button(window, text="junior employee (10000 scoops)",
             fg='red2', height=1, width=29, command=employee1Function)
btn.place(x=450, y=80)

# btn=Button(window, text="senior employee (100000 scoops)", fg='red2', height=1, width=29, command=employee2Function)

window.mainloop()
