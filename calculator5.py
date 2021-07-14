from tkinter import*


#Creating a window
window= Tk()

#Giving tilte of the project
window.title("My Calculator")

#Inserting image in the project
window.iconbitmap('C:/Users/user/Downloads/calculator.ico')


s=Entry(window,width=40, borderwidth=40,fg="white",bg="black")
s.grid(row=0, column=0, columnspan=3,padx=10,pady=10)
counter=0

#Defining functions
def buttonclick(number):
    current= s.get()
    s.delete(0, END)
    s.insert(0, str(current)+str(number))

def buttonclear():
    s.delete(0, END)

def buttonequal():
    secondnumber= s.get()
    s.delete(0,END)


    if counter == 1:
        s.insert(0, fnum + float(secondnumber))
    elif counter == 2:
       s.insert(0, fnum - float(secondnumber))
    elif counter ==3:
        s.insert(0, fnum * float(secondnumber))
    elif counter == 4:
        s.insert(0, fnum / float(secondnumber))

def buttonclick_allclear():
    global counter
    counter =0
    s.delete(0, END)

def buttonadd():
    global counter
    counter +=1
    firstnumber= s.get()
    global fnum
    fnum= float(firstnumber)
    s.delete(0,END)


def buttonsub():
    global counter
    counter += 2
    firstnumber= s.get()
    global fnum
    fnum= float(firstnumber)
    s.delete(0,END)


def buttonmul():
    global counter
    counter += 3
    firstnumber= s.get()
    global fnum
    fnum= float(firstnumber)
    s.delete(0,END)

def buttondiv():
    global counter
    counter += 4
    firstnumber = s.get()
    global fnum
    fnum = float(firstnumber)
    s.delete(0, END)



#Defining buttons
button1= Button(window, text="1", padx=50, pady=25,fg="black",bg="sky blue",command=lambda: buttonclick(1))
button2= Button(window, text="2", padx=50, pady=25,fg="black",bg="sky blue",command=lambda: buttonclick(2))
button3= Button(window, text="3", padx=50, pady=25,fg="black",bg="sky blue",command=lambda: buttonclick(3))

button4= Button(window, text="4", padx=50, pady=25,fg="black",bg="sky blue",command=lambda: buttonclick(4))
button5= Button(window, text="5", padx=50, pady=25,fg="black",bg="sky blue",command=lambda: buttonclick(5))
button6= Button(window, text="6", padx=50, pady=25,fg="black",bg="sky blue",command=lambda: buttonclick(6))

button7= Button(window, text="7", padx=50, pady=25,fg="black",bg="sky blue",command=lambda: buttonclick(7))
button8= Button(window, text="8", padx=50, pady=25,fg="black",bg="sky blue",command=lambda: buttonclick(8))
button9= Button(window, text="9", padx=50, pady=25,fg="black",bg="sky blue",command=lambda: buttonclick(9))

button0= Button(window, text="0", padx=50, pady=25,fg="black",bg="sky blue",command=lambda: buttonclick(0))
buttonclear= Button(window, text="Clear", padx=95, pady=25,fg="black",bg="silver",command=buttonclear)
buttonequal= Button(window, text="=", padx=105, pady=25,fg="black",bg="purple",command=buttonequal)

buttonclick_allclear= Button(window, text="AC", padx=45,fg="black",bg="orange", pady=25,command=buttonclick_allclear)
buttonadd= Button(window, text="+", padx=50, pady=25,fg="black",bg="green",command= buttonadd)
buttonsub= Button(window, text="-", padx=50, pady=25,fg="black",bg="green",command=buttonsub)

buttonmul= Button(window, text="*", padx=50, pady=25,fg="black",bg="green",command=buttonmul)
buttondiv= Button(window, text="/", padx=50, pady=25,fg="black",bg="green",command= buttondiv)
buttonpoint= Button(window, text=".", padx=50, pady=25,fg="black",bg="brown",command=lambda: buttonclick("."))




#Putting buttons on the screen
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0)
buttonclear.grid(row=4,column=1,columnspan=2)
buttonequal.grid(row=5,column=1,columnspan=2)

buttonclick_allclear.grid(row=5,column=0)
buttonadd.grid(row=1,column=4)
buttonsub.grid(row=2,column=4)

buttonpoint.grid(row=5,column=4)
buttonmul.grid(row=3,column=4)
buttondiv.grid(row=4,column=4)





mainloop()