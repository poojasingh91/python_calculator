from tkinter import *
import math

def click(value):
    ex=entryField.get()
    answer=''

    if value=="C":
        ex=ex[0:len(ex)-1]
        entryField.delete(0,END)
        entryField.insert(0,ex)

    elif value=="CE":
        entryField.delete(0,END)

    elif value=="√":
        answer=math.sqrt(eval(ex))

    elif value=="π":
        answer=math.pi

    elif value=="cosθ":
        answer=math.cos(math.radians(eval(ex)))

    elif value=="sinθ":
        answer=math.sin(math.radians(eval(ex)))

    elif value=="tanθ":
        answer=math.tan(math.radians(eval(ex)))

    elif value=="2π":
        answer=2*math.pi

    elif value=="cosh":
        answer=math.cosh(math.radians(eval(ex)))

    elif value=="sinh":
        answer=math.sinh(math.radians(eval(ex)))

    elif value=="tanh":
        answer=math.tanh(math.radians(eval(ex)))

    elif value==chr(8731):
        answer=eval(ex)**(1/3)

    elif value=="x\u02b8":
        entryField.insert(END,'**')

    elif value=="x\u00B3":
        answer=eval(ex)**3

    elif value=="x\u00B2":
        answer=eval(ex)**2

    elif value=="ln":
        answer=math.log2(eval(ex))

    elif value=="deg":
        answer=math.degrees(eval(ex))

    elif value=="rad":
        answer=math.radians(eval(ex))

    elif value=="e":
        answer=math.e

    elif value=="log10":
        answer=math.log10(eval(ex))

    elif value=="x!":
        answer=math.factorial(ex)

    elif value==chr(247):
        entryField.insert(END,"/")
        return

    elif value=="=":
        answer=eval(ex)

    else:
        entryField.insert(END,value)
        return

    entryField.delete(0,END)
    entryField.insert(0,answer)

root=Tk()
root.title('Smart Calculator')
root.config(bg='dodgerblue3')
root.geometry('680x486+100+100')

logoImage=PhotoImage(file='calculator1.png')
logoLabel=Label(root,image=logoImage,bg='dodgerblue3')
logoLabel.grid(row=0,column=0)

entryField=Entry(root,font=('arial', 20,'bold'),bg='dodgerblue3',fg='white',bd=10,relief='sunken',width=30)
entryField.grid(row=0,column=0,columnspan=8)

micImage=PhotoImage(file='mic.png')
micLabel=Label(root,image=micImage,bd=0, bg='dodgerblue3', activebackground='dodgerblue3')
micLabel.grid(row=0,column=7)

button_text_list = ["C","CE","√","+","π","cosθ","sinθ","tanθ","1","2","3","-","2π","cosh","tanh","sinh","4","5","6","*",chr(8731),"x\u02b8","x\u00B3","x\u00B2","7","8","9",chr(247),"ln","deg","rad","e","0",".","%","=","log10","x!"]
rowvalue=1
columnvalue=0
for i in button_text_list:
    button=Button(root,width=5,height=2,bd=2,relief='sunken',text=i,bg='dodgerblue3', fg='white',font=('arial',18,'bold'),activebackground='dodgerblue3', command=lambda button=i: click(button))
    button.grid(row=rowvalue,column=columnvalue,pady=1)
    columnvalue+=1
    if columnvalue>7:
        rowvalue+=1
        columnvalue=0




root.mainloop()