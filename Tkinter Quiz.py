from tkinter import *
from tkinter import ttk

#SETTING UP
root = Tk()
root.title("Taylens Quiz")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.configure(bg="PowderBlue")
lbl1 = Label(root, text="Taylens Quiz", bg="PowderBlue", fg="white", font="none 31 bold")
lbl1.config(anchor=CENTER)
lbl1.pack()



#LETS BEGIN TEXT
lbl2 = Label (root, text="Lets Begin!:", bg="PowderBlue", fg="white", font="none 18 bold")
lbl2.config(anchor=CENTER)
lbl2.pack()

#exit button
aaa = []
def clear():
    global root
    global aaa
    root.destroy()
    root=Frame(root)
    root.pack()
aaa.append(Button(root, text='Exit', width=10, command=clear))
aaa[0].pack()







#wrong text
ac = []
def wrong():
    global ac
    ac.append(Label (root, text="That is wrong :(", bg="red", fg="white", font="none 18 bold"))
    ac[0].config(anchor=CENTER)
    ac[0].pack()

#correct text
ab = []
def correct():
    global ab
    global temp
    ab.append(Label (root, text="That is right!", bg="blue", fg="white", font="none 18 bold"))
    ab[0].config(anchor=CENTER)
    ab[0].pack()

#question 1
temp = []
def question1():
    global temp
    framebutton.pack_forget()
    lbl2.pack_forget()
    temp.append(Label (root, text="Question 1! \n Is Taylen 17 or 18?", bg="blue", fg="white", font="none 18 bold"))
    temp[0].config(anchor=CENTER)
    temp[0].pack()
    temp.append( Button(root, text="17", width=10, command=correct, fg="blue"))
    temp.append( Button(root, text="18", width=10, command=wrong, fg="blue"))
    temp[1].pack()
    temp[2].pack()
    temp.append(Button(root, text="Next", width=10, command=question2))
    temp[3].pack()

#question 2 and deleting previos question
temp2 = []
def question2():
    global temp
    global temp2
    global ac
    global ab
    for a in temp:
      a.pack_forget()
    for a in ab:
        a.pack_forget()
    for a in ac:
        a.pack_forget()

    temp2.append(Label (root, text="Question 2! \n Can Taylen Drive?", bg="blue", fg="white", font="none 18 bold"))
    temp2[0].config(anchor=CENTER)
    temp2[0].pack()
    temp2.append( Button(root, text="Yes", width=10, command=correct, fg="blue"))
    temp2.append( Button(root, text="No", width=10, command=wrong, fg="blue"))
    temp2[1].pack()
    temp2[2].pack()
    temp2.append(Button(root, text="Next", width=10, command=question3))
    temp2[3].pack()

#question 3 and deleting previos question
temp3 = []
def question3():
    global temp2
    global temp3
    global ac
    global ab
    for a in temp2:
      a.pack_forget()
    for a in ab:
        a.pack_forget()
    for a in ac:
        a.pack_forget()

    temp3.append(Label (root, text="Question 3! \n Who is Taylens Best friend?", bg="blue", fg="white", font="none 18 bold"))
    temp3[0].config(anchor=CENTER)
    temp3[0].pack()
    temp3.append( Button(root, text="Lachlan", width=10, command=correct, fg="blue"))
    temp3.append( Button(root, text="Sabina", width=10, command=correct, fg="blue"))
    temp3.append( Button(root, text="Shay", width=10, command=correct, fg="blue"))
    temp3[1].pack()
    temp3[2].pack()
    temp3[3].pack()
    temp3.append(Button(root, text="Next", width=10, command=question4))
    temp3[4].pack()

#question 4 and deleting previos question
temp4 = []
def question4():
    global temp4
    global temp3
    global ac
    global ab
    for a in temp3:
      a.pack_forget()
    for a in ab:
        a.pack_forget()
    for a in ac:
        a.pack_forget()

    temp4.append(Label (root, text="Question 4! \n Is Taylen Male or Female?", bg="blue", fg="white", font="none 18 bold"))
    temp4[0].config(anchor=CENTER)
    temp4[0].pack()
    temp4.append( Button(root, text="Female", width=10, command=wrong, fg="blue"))
    temp4.append( Button(root, text="Male", width=10, command=correct, fg="blue"))
    temp4[1].pack()
    temp4[2].pack()
    temp4.append(Button(root, text="Next", width=10, command=question5))
    temp4[3].pack()

#question 5 and deleting previos question
temp5 = []
def question5():
        global temp5
        global temp4
        global ac
        global ab
        for a in temp4:
          a.pack_forget()
        for a in ab:
            a.pack_forget()
        for a in ac:
            a.pack_forget()
        temp5.append(Label (root, text="Question 5! \n Who is Taylens Favourite Artist?", bg="blue", fg="white", font="none 18 bold"))
        temp5[0].config(anchor=CENTER)
        temp5[0].pack()
        temp5.append( Button(root, text="NF", width=10, command=wrong, fg="blue"))
        temp5.append( Button(root, text="Josh A", width=10, command=correct, fg="blue"))
        temp5[1].pack()
        temp5[2].pack()
        temp5.append(Button(root, text="Next", width=10, command=question6))
        temp5[3].pack()


#question 6 and deleting previos question
temp6 = []
def question6():
        global temp6
        global temp5
        global ac
        global ab
        for a in temp5:
          a.pack_forget()
        for a in ab:
            a.pack_forget()
        for a in ac:
            a.pack_forget()
        temp6.append(Label (root, text="Question 6! \n What is Taylens Favourite Song?", bg="blue", fg="white", font="none 18 bold"))
        temp6[0].config(anchor=CENTER)
        temp6[0].pack()
        temp6.append( Button(root, text="Revenge", width=10, command=correct, fg="blue"))
        temp6.append( Button(root, text="Revolution", width=10, command=wrong, fg="blue"))
        temp6[1].pack()
        temp6[2].pack()
        temp6.append(Button(root, text="Next", width=10, command=question7))
        temp6[3].pack()


#exit message
temp7 = []
def question7():
        global temp6
        global tamp7
        global ac
        global ab
        global aaa
        for a in temp6:
          a.pack_forget()
        for a in ab:
            a.pack_forget()
        for a in ac:
            a.pack_forget()
        for a in aaa:
            a.pack_forget()
        temp7.append(Label (root, text="Good Job! \n Hope you had fun playing :)", bg="blue", fg="white", font="none 18 bold"))
        temp7[0].config(anchor=CENTER)
        temp7[0].pack()
        temp7.append( Button(root, text="exit", width=10, command=clear, fg="blue"))
        temp7[1].pack()



#start button
framebutton = Button(root, text="Start", width=10, command=question1)
framebutton.pack()



root.mainloop()
