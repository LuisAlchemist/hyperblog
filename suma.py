from ast import Delete
from tkinter import Tk, Label, Button, Entry

def suma ():
   a = box1.get()
   b = box2.get()
   c = float(a) + float(b)
   box3.delete(0, 'end')
   box3.insert(0,c)
   

vent = Tk()

vent.geometry("650x350")
vent.title("Practica de suma")
vent.resizable(0,0)
vent.config(bg="green")

lbl1 = Label (vent, text='Primer numero', bg="yellow", fg="blue" )
lbl1.place(x=10, y=0, width=100, height=75)
box1 = Entry(vent, bg="pink")
box1.place(x=150, y=0, width=100, height=75)

lbl2 = Label (vent, text='Segundo numero', bg="yellow", fg="blue" )
lbl2.place(x=10, y=100, width=100, height=75)
box2 = Entry(vent, bg="pink")
box2.place(x=150, y=100, width=100, height=75)

lbl3 = Label (vent, text='Resultado', bg="red", fg="black" )
lbl3.place(x=10, y=200, width=100, height=75)
box3 = Entry(vent, bg="pink")
box3.place(x=150, y=200, width=100, height=75)


btn = Button(vent, text='suma', fg="black", bg="gray", command= suma)
btn.place(x=500, y=100, width=100, height=75)

vent.mainloop()