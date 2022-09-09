from struct import pack
from tkinter import Frame, Tk, Label, Button, Wm




class FrameManu(Frame):

    def __init__(self, master=None):
        super().__init__(master,width=650, height=350,bg='green')
        self.master = master
        self.pack()
        self.create_widgets()

    def mensaje(self) :
        print("Mensaje del buton")

    def create_widgets(self):
        """self.frame1 = Frame(ventana, bg="blue")
        self.frame1.pack(expand=True, fill='both')

        self.frame2 = Frame(ventana, bg="green")
        self.frame2.pack(expand=True, fill='both')
        self.frame2.config(cursor='heart')"""

        self.btn1 = Button(self, text='HOME', fg="black", bg="gray", command= self.mensaje)
        self.btn1.place(relx=0.10, rely=0.1, relwidth=0.15, relheight=0.08)

        self.btn2 = Button(self, text='CONFIGURATION', fg="black", bg="gray", command= self.mensaje)
        self.btn2.place(relx=0.26, rely=0.1, relwidth=0.15, relheight=0.08)

        self.btn3 = Button(self, text='ROBOT ARM', fg="black", bg="gray", command= self.mensaje)
        self.btn3.place(relx=0.42, rely=0.1, relwidth=0.15, relheight=0.08)

        self.btn4 = Button(self, text='SCARA', fg="black", bg="gray", command= self.mensaje)
        self.btn4.place(relx=0.58, rely=0.1, relwidth=0.15, relheight=0.08)

        self.btn5 = Button(self, text='CNC', fg="black", bg="gray", command= self.mensaje)
        self.btn5.place(relx=0.74, rely=0.1, relwidth=0.15, relheight=0.08)



ventana = Tk()
ventana.wm_title("Monlee Garden")
app = FrameManu(ventana)
app.mainloop()

#ventana.geometry("650x350")
# ventana.title("Monitoreo de monlee garden")
#ventana.resizable(0,0)
#ventana.config(bg="green")

#lbl = Label (ventana, text='HOME', bg="yellow", fg="blue" )
#lbl.pack()

#ventana.mainloop()