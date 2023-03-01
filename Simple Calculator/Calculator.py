from tkinter import *
import time
import tkinter.messagebox

op=''
kill=Tk() # creating window & its geometry
kill.geometry('400x650+0+0')
kill.title('Simple Calculator')


# creating Frame
ta=Frame(kill,width=300,height=50,relief=SUNKEN) 
ta.pack(side=TOP)

ra=Frame(kill,width=300,height=700,relief=SUNKEN)
ra.pack(side=TOP)


# Time & Title
label_in=Label(ta,font="Times 40 bold",text='Calculator',fg='black',anchor='w')
label_in.grid(row=0,column=0)

local_time=time.asctime(time.localtime(time.time()))

label_info=Label(ta,font="Times 20 bold",text=local_time,fg='black', bd = 10, anchor = 'w')
label_info.grid(row = 1, column = 0)

# calculator

ip = StringVar()
op=""

def san(num):
    global op
    op=op+str(num)
    ip.set(op)

    
def cle():
    global op
    op=''
    ip.set(op)
    
    
def calculate():
    global op
    try:
        sun = str(eval(op))
        ip.set(sun)
    except Exception as e:
        tkinter.messagebox.showinfo("ERROR","Incorrect Input")
        sun=0
        cle()
    
    op=''



text=Entry(ra,font="Times 20 bold",textvariable=ip,bd=30,insertwidth=4,bg='blue',justify='right')
text.grid(columnspan=4)



#=========first row button=========

btn7=Button(ra,padx=16,pady=16,bd=8,fg="black",font="Times 20 bold",text="7",bg="white",command=lambda:san(7))
btn7.grid(row=2,column=0)

btn8=Button(ra,padx=16,pady=16,bd=8,fg="black",font="Times 20 bold",text="8",bg="white",command=lambda:san(8))
btn8.grid(row=2,column=1)

btn9=Button(ra,padx=16,pady=16,bd=8,fg="black",font="Times 20 bold",text="9",bg="white",command=lambda:san(9))
btn9.grid(row=2,column=2)

plus=Button(ra,padx=16,pady=16,bd=8,fg="black",font="Times 20 bold",text="+",bg="white",command=lambda:san("+"))
plus.grid(row= 2, column= 3)


#=========second row button=========

btn4=Button(ra,padx=16,pady=16,bd=8,fg="black",font="Times 20 bold",text="4",bg="white",command=lambda:san(4))
btn4.grid(row=3,column=0)

btn5=Button(ra,padx=16,pady=16,bd=8,fg="black",font="Times 20 bold",text="5",bg="white",command=lambda:san(5))
btn5.grid(row=3,column=1)

btn6=Button(ra,padx=16,pady=16,bd=8,fg="black",font="Times 20 bold",text="6",bg="white",command=lambda:san(6))
btn6.grid(row=3,column=2)

minus=Button(ra,padx=16,pady=16,bd=8,fg="black",font="Times 20 bold",text="-",bg="white",command=lambda:san("-"))
minus.grid(row=3,column=3)


#=========third row button=========

btn1=Button(ra,padx=16,pady=16,bd=8,fg="black",font="Times 20 bold",text="1",bg="white",command=lambda:san(1))
btn1.grid(row=4,column=0)

btn2=Button(ra,padx=16,pady=16,bd=8,fg="black",font="Times 20 bold",text="2",bg="white",command=lambda:san(2))
btn2.grid(row=4,column=1)

btn3=Button(ra,padx=16,pady=16,bd=8,fg="black",font="Times 20 bold",text="3",bg="white",command=lambda:san(3))
btn3.grid(row=4,column=2)

mul=Button(ra,padx=16,pady=16,bd=8,fg="black",font="Times 20 bold",text="*",bg="white",command=lambda:san("*"))
mul.grid(row=4,column=3)


#=========fourth row button=========

btn0=Button(ra,padx=16,pady=16,bd=8,fg="black",font="Times 20 bold",text="0",bg="white",command=lambda:san(0))
btn0.grid(row=5,column=0)

btn_clear=Button(ra,padx=16,pady=16,bd=8,fg="black",font="Times 20 bold",text="C",bg="white",command=cle)
btn_clear.grid(row=5,column=1)

btn_equal=Button(ra,padx=16,pady=16,bd=8,fg="black",font="Times 20 bold",text="=",bg="white",command=calculate)
btn_equal.grid(row=5,column=2)

div=Button(ra,padx=16,pady=16,bd=8,fg="black",font="Times 20 bold",text="/",bg="white",command=lambda:san("/"))
div.grid(row=5,column=3)


#########################################


kill.mainloop()
















































    
    
