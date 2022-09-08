from struct import pack
from tkinter import Tk, Label, Button


def mensaje() :
    print("Mensaje del buton")


ventana = Tk()
ventana.geometry("650x350")
ventana.title("Monitoreo de monlee garden")
ventana.resizable(0,0)
ventana.config(bg="green")

lbl = Label (ventana, text='HOME', bg="yellow", fg="blue" )
lbl.pack()

btn = Button(ventana, text='Presione', fg="blue", bg="yellow", command= mensaje)
btn.place(relx=0.1, rely=0.1, relwidth=0.1, relheight=0.1)

ventana.mainloop()