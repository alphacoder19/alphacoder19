#Hello User ! I am making a Calculator with the help of tkinter.
#Import tkinter
from tkinter import *

#import messagebox in tkinter.
import tkinter.messagebox as msg

#import atexit for quit
import atexit

#Making GUI Window with the name of @interface
interface = Tk()
interface.geometry("325x500")
interface.title("Calculator")
#places the icon
interface.wm_iconbitmap("icon.ico")

#define functions,we call the function with the help of button
def ext():
    a = msg.askokcancel("Exit","Press 'Ok' for Exit")
    if a == ON :
        msg.showinfo("Bye","Visit Again!")
        interface.destroy()
    else:
        msg.showinfo("Use","Welcome Again")

def touch(event):
    write = event.widget.cget("text")
    if write == "=":
        if blank.get().isdigit():
            val =int(blank.get())
        else:
            val = eval(blank1.get())
        blank.set(val)
    elif write == "AC":
        blank.set("")
    else:
        blank.set(blank.get() + write)

#making a menu for exit or quit the Interface(there is no need of this but feels good)
mmenu = Menu(interface)
mmenu.add_command(label="Exit",command=ext)
interface.config(menu = mmenu)

#making a blank space named variable blank to display the calculations
blank = StringVar()
blank1 = Entry(interface,textvariable=blank,font="lucida 40",bg="white",fg="black",width=325,justify=RIGHT)
blank1.pack(padx=10,pady=10)

#now,Making a frame
f0 = Frame(interface,bg="white")
#put the buttons into the frame (In this using the bind widget for handling events)
btnAC = Button(f0,text="AC",width=10,height=2,relief=GROOVE,borderwidth=5,bg="red",fg="white",font="lucida 15")
btnAC.pack(side=LEFT,padx=7,pady=5)
btnAC.bind("<Button-1>",touch)
btnPer = Button(f0,text="%",width=4,height=2,relief=GROOVE,borderwidth=5,bg="orange",fg="white",font="lucida 15")
btnPer.pack(side=LEFT,padx=5,pady=5)
btnPer.bind("<Button-1>",touch)
btnD = Button(f0,text="/",width=4,height=2,relief=GROOVE,borderwidth=5,bg="orange",fg="white",font="lucida 15")
btnD.pack(side=LEFT,padx=5,pady=5)
btnD.bind("<Button-1>",touch)
f0.pack()

#making next frame named f1 (Further, As it is made above, so is it made below also.)
f1 = Frame(interface,bg="white")
btn7 = Button(f1,text="7",width=4,height=2,relief=GROOVE,borderwidth=5,bg="black",fg="white",font="lucida 15")
btn7.pack(side=LEFT,padx=5,pady=5)
btn7.bind("<Button-1>",touch)
btn8 = Button(f1,text="8",width=4,height=2,relief=GROOVE,borderwidth=5,bg="black",fg="white",font="lucida 15")
btn8.pack(side=LEFT,padx=5,pady=5)
btn8.bind("<Button-1>",touch)
btn9 = Button(f1,text="9",width=4,height=2,relief=GROOVE,borderwidth=5,bg="black",fg="white",font="lucida 15")
btn9.pack(side=LEFT,padx=5,pady=5)
btn9.bind("<Button-1>",touch)
btnM = Button(f1,text="*",width=4,height=2,relief=GROOVE,borderwidth=5,bg="orange",fg="white",font="lucida 15")
btnM.pack(side=LEFT,padx=5,pady=5)
btnM.bind("<Button-1>",touch)
f1.pack()

#making next frame named f2 (Further, As it is made above, so is it made below also.)
f2 = Frame(interface,bg="white")
btn4 = Button(f2,text="4",width=4,height=2,relief=GROOVE,borderwidth=5,bg="black",fg="white",font="lucida 15")
btn4.pack(side=LEFT,padx=5,pady=5)
btn4.bind("<Button-1>",touch)
btn5 = Button(f2,text="5",width=4,height=2,relief=GROOVE,borderwidth=5,bg="black",fg="white",font="lucida 15")
btn5.pack(side=LEFT,padx=5,pady=5)
btn5.bind("<Button-1>",touch)
btn6 = Button(f2,text="6",width=4,height=2,relief=GROOVE,borderwidth=5,bg="black",fg="white",font="lucida 15")
btn6.pack(side=LEFT,padx=5,pady=5)
btn6.bind("<Button-1>",touch)
btnS = Button(f2,text="-",width=4,height=2,relief=GROOVE,borderwidth=5,bg="orange",fg="white",font="lucida 15")
btnS.pack(side=LEFT,padx=5,pady=5)
btnS.bind("<Button-1>",touch)
f2.pack()

#making next frame named f3 (Further, As it is made above, so is it made below also.)
f3 = Frame(interface,bg="white")
btn1 = Button(f3,text="1",width=4,height=2,relief=GROOVE,borderwidth=5,bg="black",fg="white",font="lucida 15")
btn1.pack(side=LEFT,padx=5,pady=5)
btn1.bind("<Button-1>",touch)
btn2 = Button(f3,text="2",width=4,height=2,relief=GROOVE,borderwidth=5,bg="black",fg="white",font="lucida 15")
btn2.pack(side=LEFT,padx=5,pady=5)
btn2.bind("<Button-1>",touch)
btn3 = Button(f3,text="3",width=4,height=2,relief=GROOVE,borderwidth=5,bg="black",fg="white",font="lucida 15")
btn3.pack(side=LEFT,padx=5,pady=5)
btn3.bind("<Button-1>",touch)
btnA = Button(f3,text="+",width=4,height=2,relief=GROOVE,borderwidth=5,bg="orange",fg="white",font="lucida 15")
btnA.pack(side=LEFT,padx=5,pady=5)
btnA.bind("<Button-1>",touch)
f3.pack()

#making next frame named f1 (Further, As it is made above, so is it made below also.)
f4 = Frame(interface,bg="white")
btn0 = Button(f4,text="0",width=4,height=2,relief=GROOVE,borderwidth=5,bg="black",fg="white",font="lucida 15")
btn0.pack(side=LEFT,padx=5,pady=5)
btn0.bind("<Button-1>",touch)
btnDot = Button(f4,text=".",width=4,height=2,relief=GROOVE,borderwidth=5,bg="black",fg="white",font="lucida 15")
btnDot.pack(side=LEFT,padx=5,pady=5)
btnDot.bind("<Button-1>",touch)
Answer = Button(f4,text="=",width=4,height=2,relief=GROOVE,borderwidth=5,bg="dark orange",fg="white",font="lucida 15")
Answer.pack(side=LEFT,padx=5,pady=5)
Answer.bind("<Button-1>",touch)
f4.pack()

interface.config(bg="black")
interface.mainloop()