from distutils.cmd import Command
from struct import pack
from tkinter import Frame, Tk, Label, Button, Toplevel, Wm, messagebox
from unicodedata import name


class create_windows :

    def __init__(self, name):
        self.name = name

    def windows (self, window_name):
        self.ventana_home = Toplevel()
        self.ventana_home.title(self.window_name)
        self.ventana_home.geometry("500x400")
        """boton_in_mesurements = Button(ventana_home, text='NADA AÚN', fg="black", bg="gray")
        boton_in_mesurements.place(relx=0.10, rely=0.1, relwidth=0.15, relheight=0.08)"""
        


class FrameManu(Frame):

    def __init__(self, master=None):
        super().__init__(master,width=650, height=350,bg='green')
        self.master = master
        self.pack()
        self.create_widgets()

    """def window_measurements() :
        ventana_home = Toplevel()
        ventana_home.title("MEASUREMENTS")
        ventana_home.geometry("500x400")
        boton_in_mesurements = Button(ventana_home, text='MEASUREMENTS', fg="black", bg="gray")
        boton_in_mesurements.place(relx=0.10, rely=0.1, relwidth=0.15, relheight=0.08)
    
    def window_configuration(self):
        ventana_configuration = Toplevel()
        ventana_configuration.title("CONFIGURATION")
        ventana_configuration.geometry("500x400")

    
    def window_robotArm(self):
        ventana_robotArm = Toplevel()
        ventana_robotArm.title("ROBOT ARM")
        ventana_robotArm.geometry("500x400")

    def window_scara(self):
        ventana_scara = Toplevel()
        ventana_scara.title("SCARA")
        ventana_scara.geometry("500x400")

    def window_cnc(self):
        ventana_cnc = Toplevel()
        ventana_cnc.title("CNC")
        ventana_cnc.geometry("500x400") """

    def create_widgets(self):
        """self.frame1 = Frame(ventana, bg="blue")
        self.frame1.pack(expand=True, fill='both')

        self.frame2 = Frame(ventana, bg="green")
        self.frame2.pack(expand=True, fill='both')
        self.frame2.config(cursor='heart')"""

        self.btn1 = Button(self, text='MEASUREMENTS', fg="black", bg="gray", command= create_windows)
        self.btn1.place(relx=0.10, rely=0.1, relwidth=0.15, relheight=0.08)
    

    """
        self.btn2 = Button(self, text='CONFIGURATION', fg="black", bg="gray", command= self.window_configuration)
        self.btn2.place(relx=0.26, rely=0.1, relwidth=0.15, relheight=0.08)

        self.btn3 = Button(self, text='ROBOT ARM', fg="black", bg="gray", command= self.window_robotArm)
        self.btn3.place(relx=0.42, rely=0.1, relwidth=0.15, relheight=0.08)

        self.btn4 = Button(self, text='SCARA', fg="black", bg="gray", command= self.window_scara)
        self.btn4.place(relx=0.58, rely=0.1, relwidth=0.15, relheight=0.08)

        self.btn5 = Button(self, text='CNC', fg="black", bg="gray", command= self.window_cnc)
        self.btn5.place(relx=0.74, rely=0.1, relwidth=0.15, relheight=0.08)"""



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