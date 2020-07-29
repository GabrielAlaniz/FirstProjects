from tkinter import *
import random

root = Tk()
root.title("Number Guessing Game")
root.resizable(False,False)

myFrame = Frame(root, width=600, height=350)
myFrame.config(bd=25, cursor="hand2", bg="lightblue")
myFrame.pack()


label = Label(myFrame, text="Hit Your Best Shot!")
label.config(font=("Verdana",20),bg="lightblue")
label.grid(row=0,column=0,columnspan=5)

lblGuesses = Label(myFrame, text="Chances left: 3")
lblGuesses.config(font=("Verdana",11))
lblGuesses.grid(row=1,column=3,columnspan=2,pady=20)

lblLine1 = Label(myFrame, text="Guess a number from 0 to 9")
lblLine1.config(font=("Verdana",14),bg="lightblue")
lblLine1.grid(row=2,column=1,columnspan=3,pady=20)

lblmsj = Label(myFrame, text="")
lblmsj.config(font=("Verdana",13))
lblmsj.grid(row=7,column=1,pady=5,columnspan=3)

lblresult = Label(myFrame, text="")
lblresult.config(font=("Verdana",8), bg="lightblue")
lblresult.grid(row=11,column=1,pady=5,columnspan=3)


# === BUTTONS ===

buttons = []
for index in range(0,10):
	btn = Button(myFrame, font=12, text=index, width=6,command=lambda index=index: process(index), state=DISABLED)
	buttons.append(btn)

# === START BUTTON ===
btnStartGameList = []
for index in range(0, 1):
    btnStartGame = Button(myFrame, font=8, text="Start Game", command=lambda: startgame(index))
    btnStartGameList.append(btnStartGame)

btnStartGameList[0].grid(row=6,column=2,pady=10)


ind = 0
r = 3
for row in range(0, 2):
    for col in range(0, 5):
    	buttons[ind].grid(row=row+r, column=col,padx=15,pady=6)
    	ind+=1
    r+=1

# === LOGIC ===
number = random.randint(0,9) # numero a adivinar
print(number)
chances = 3 # vidas
guess = 0
guess_row = 7
lblmsj = []
lblresult = []

# Reset everything
def init():
	global buttons, guess, chances, number, lblmsj, guess_row, lblresult
	guess = 0
	chances = 3
	number = random.randint(0,9)
	print(number)
	lblGuesses["text"] = "Chances left: "+str(chances)
	guess_row = 7


	# Clean label list
	for msj in lblmsj:
		msj.grid_forget()
	lblmsj = []

	for msj in lblresult:
		msj.grid_forget()
	lblresult = []


def process(i):
	global chances, buttons, guess_row
	guess = i

	chances-=1
	lblGuesses["text"] = "Chances left: "+str(chances)

	if guess==number:
		lbl = Label(myFrame, text="Congratulations!! YOU WON!!", bg="lightgreen")
		lbl.grid(row=guess_row,column=1,columnspan=3)
		lblmsj.append(lbl)
		guess_row-=1

		for b in buttons:
			b["state"] = DISABLED

	elif chances>0:
		lbl = Label(myFrame, text="Noup!! Try Again...", bg="lightblue")
		lbl.grid(row=guess_row,column=1,columnspan=3)
		lblmsj.append(lbl)
		guess_row+=1

	if chances==0:
		if guess!=number:
			lbl = Label(myFrame, text="Strike 3!! YOU LOSE!! ", bg="red", fg="white")
			lbl.grid(row=guess_row,column=1,columnspan=3)
			lblmsj.append(lbl)
			#guess_row+=1
			lbl2 = Label(myFrame)
			lbl2.config(bg="lightblue")
			lbl2.grid(row=guess_row+1,column=1,columnspan=3)
			lbl2["text"] = "The number was: "+str(number)
			lblresult.append(lbl2)

		for b in buttons:
			b["state"] = DISABLED

	buttons[i]["state"] = DISABLED


status = "none"

def startgame(i):
    global status
    for b in buttons:
    	b["state"] = NORMAL

    if status=="none":
    	status = "started"
    	btnStartGameList[i]["text"] = "Restart Game"
    else:
    	status = "restarted"
    	init()
    print("Game Started")


root.mainloop()