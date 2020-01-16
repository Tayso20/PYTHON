from tkinter import*
import random

#setup of tkinter
root = Tk()
#this is the state of the window type
root.state("zoomed")
#this is the background colour
root.configure(background='black')


#This is the main title for the game
Label(root, text="Phonetic Alphabet Game", fg = "green", bg = "black", font = "Helvetica 90 bold underline italic").pack()

def type():
    global question
    question.insert(END, Quest2)

    

#random question generator
#this is question 1
Questions1 = ["Hello"]
#this is the range for my random  word
randlett = random.randint(0, 0)
Quest = Questions1[randlett]
#this prints out the question
print(Quest)

Questions2 = ["Tank"]
#this is the range for my random  word
randlett = random.randint(0, 0)
Quest2 = str(Questions2[randlett])
#this prints out the question
print(Quest2)



#answer for question 1
answer1 = ['hotel echo lima lima alpha']
#this is the range for the answer lsit
randlett = random.randint(0, 0)
answ1 = answer1[randlett]
#this prints answer
print(answ1)

answer2 = ['tango alpha november kilo']
#this is the range for the answer lsit
randlett = random.randint(0, 0)
answ2 = answer2[randlett]
#this prints answer
print(answ2)




#these are frames
#this is the word list frame
phonetic_word_box = Frame(root, background = 'black', highlightbackground="green", highlightcolor="green", highlightthickness=10, width=200, height=730, bd= 0)
phonetic_word_box.place(x=0, y=150)

#this is question box frame
question_box = Frame(root, background = 'black', highlightbackground="green", highlightcolor="green", highlightthickness=10, width=1125, height=100, bd= 0)
question_box.place(x=300, y=300)
#
# this is answer box frame
answer_box = Frame(root, background = 'black', highlightbackground="green", highlightcolor="green", highlightthickness=10, width=1125, height=100, bd= 0)
answer_box.place(x=300, y=600)

#TEXT
question = Text(question_box, height=2, width=30)
question.pack()
question.place(x=1, y = 1)
question.config(state=NORMAL)
question.insert(END, Quest)

#this is my command for the button used to check the answer
def codetorun():
    user_answer = w.get()
    print(user_answer)
    if user_answer == answ1:
        print ('Well Done NEXT LEVEL')
        question.config(state=DISABLED)
        question.delete(1.0, END)
        type()
        question.config(state=NORMAL)

    else:
        print('Incorrect')


#this is my button to check the answer
b1 = Button(root, text="Test", fg = "black", background="#6AE7FE", bd=0, font=('Verdana', 17), width=34, command=codetorun)
b1.place(x=300, y=700)

#this is entry box
w = Entry(answer_box, fg='green', bg='white')
w.pack()
w.place(x=50, y=2)

#all code is in the mainloop
root.mainloop()