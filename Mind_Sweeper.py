from tkinter import *
import random


class Buttons:  # defines the properties and methods of a row of buttons used by user to input their guesses.

    def __init__(self, clickx, clicky, cl, guesscount):  # pass coordinates, selected colour of selected button
        self.lastclickx = clickx  # the horizontal position of the button last clicked
        self.lastclicky = clicky  # the vertical position of the button last clicked
        self.col = cl  # the colour selected for the button by the user
        self.guesscount = guesscount  # current guess number, which is needed to correctly position the scoring pegs.

    def callback(self, event):  # this code gets executed every time a new button is clicked on the grid
        if newcol != "#DDDDDD":  # the button is default colour and has not been clicked yet by the user
            button1 = Button(newframe, text="", width=3, bg=newcol)
            button1.place(x=31 * (self.lastclicky - 1), y=26 * (self.lastclickx - 1))
            # the button needs to be placed at the correct location depending on where the user last clicked
            # a new coloured version of the button is placed over the old default one
            del yourguess[self.lastclicky - 1]
            yourguess.insert((self.lastclicky - 1), newcol)
            # update and record in a list the colours selected as each button is clicked on a row
            if None not in yourguess:  # The user has entered all their colours and is prompted to confirm
                global button3
                button3 = Button(root, text="Confirm Guess", width=11, bg="#DDDDDD", command=self.checkscore)
                button3.place(x=163, y=5 + (self.lastclickx-1) * 26)

    def checkscore(self):  # function that checks the black and white pegs for a guess, and displays them to the canvas
        button3.destroy()
        self.guesscount += 1

        # this code displays the correct number of black and white pegs on screen
        for i in range(calcblackpegs()):
            canvas.place(x=250, y=0)
            canvas.create_oval(20 * (i + 1), ((self.guesscount * 25) - 15), 20 * (i + 1) + 10,
                               ((self.guesscount * 25) - 5), fill='black', width=1)
        # put black and white pegs at the correct positions
        for j in range(calcwhitepegs()):
            lastpos = 20 * (calcblackpegs())
            canvas.create_oval(lastpos + (20 * (j + 1)), ((self.guesscount * 25) - 15),
                               lastpos + (20 * (j + 1)) + 10, ((self.guesscount * 25) - 5), fill='white',
                               width=1)
        startproc(self.guesscount)


# function that calculates the number of black pegs for a user guess
def calcblackpegs():
    blackpegs = 0
    for x1 in range(5):
        if pegcolour[x1] == yourguess[x1]:
            blackpegs += 1

            # if a black peg is scored, mark it off as 'counted' so that it is not counted again
            compcounted[x1] = True
            usercounted[x1] = True
    if blackpegs == 5:
        revealcode()

    return blackpegs


def calcwhitepegs():
    whitepegs = 0
    for x1 in range(5):
        for y1 in range(5):
            # colour must match but be in a different position. also, it cannot have been already counted as a black
            # peg. once it is counted, we mark it off so it is not counted twice.
            if (yourguess[y1] == pegcolour[x1]) and (x1 != y1) and (not (usercounted[y1])) and (not (compcounted[x1])):
                whitepegs += 1
                compcounted[x1] = True
                usercounted[y1] = True
    return whitepegs


def recordguess(rg):
    return rg


# this function reveals the computer code at the request of the user from the menu
def revealcode():
    for z in range(5):
        button2 = Button(newframe2, width=3, bg=pegcolour[z])
        button2.grid(column=z * 30, row=0)

        # remove the widgets from the canvas as the game is now over
        for widget in newframe.winfo_children():
            widget.grid_forget()
        mymenu.destroy()


# initialise the display. create the button grid, and set initial variables.
def startproc(guess):
    global usercounted
    global compcounted
    global currentguess
    buttonobj = []
    compcounted = [False, False, False, False, False]
    usercounted = [False, False, False, False, False]

    # create a grid of buttons on the screen to show where user guesses will be placed
    for r in range(guess, guess + 1):
        for c in range(0, 5):
            # initialise the list that records the users current guess
            yourguess.insert(c, None)
            buttonobj.append(Buttons(r + 1, c + 1, col, r))
            button1 = Button(newframe, text="", width=3, bg=col)
            button1.grid(row=r, column=c, sticky="ew")

            # ensure the user can only select the row that represents their current guess number
            if r == guess:
                for z in range(0, c + 1):
                    #  If user clicks a button in the current guess row, call the callback function above
                    button1.bind('<Button-1>', buttonobj[z].callback)
            currentguess = recordguess(guess)


# function that updates the colour selected for a button by the user every time they click a colour on the menu
def changecol(n1):
    global newcol
    newcol = n1


# function that allows the user to clear a current row of colours if they change their mind
def resetwindow():
    button3.destroy()
    for z in range(0, len(yourguess)):
        yourguess.pop()
    startproc(currentguess)


# initialise variables and lists used in the program
buttonID = []
buttonCol = []
lastclickx = 0
lastclicky = 0
colour = ["red", "green", "blue", "yellow", "white", "#8B4513", "orange", "black"]
pegcolour = []

for x in range(5):
    pegcolour.append(colour[random.randint(0, 7)])
yourguess = []

# Tkinter interface
root = Tk()
root.geometry('1366x768')
col = "#DDDDDD"
newcol = col
newframe = Frame(root, width=600, height=600, background="#DDDDDD")
newframe.place(x=5, y=5)
newframe2 = Frame(root, width=150, height=30, background="#CCCCCC")
newframe2.place(x=5, y=500)
canvas = Canvas(root, width=150, height=600, background="#CCCCCC")
canvas.place(x=250, y=5)
mymenu = Menu(root)
root.config(menu=mymenu)
submenu1 = Menu(mymenu)
submenu2 = Menu(mymenu)
submenu3 = Menu(mymenu)
mymenu.add_cascade(label="Colour", menu=submenu1)
mymenu.add_cascade(label="Reset", menu=submenu2)
mymenu.add_cascade(label="Reveal", menu=submenu3)
for i in range(0, 8):
    if i != 5:
        submenu1.add_radiobutton(label=colour[i], command=lambda n1=colour[i]: changecol(n1))
    else:
        submenu1.add_radiobutton(label="brown", command=lambda n1=colour[i]: changecol(n1))

submenu2.add_command(label="All", command=resetwindow)
submenu3.add_command(label="Code", command=revealcode)
startproc(0)

root.mainloop()