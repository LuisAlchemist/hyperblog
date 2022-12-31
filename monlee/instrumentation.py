from tkinter import Entry, Frame, Tk, Label, Button, Toplevel, Wm, messagebox
import serial
import time


    
def window_measurements():
     ventana_home = Toplevel()
     ventana_home.title("MEASUREMENTS")
     ventana_home.geometry("500x400")
     

def window_configuration():

    ventana_configuration = Toplevel()
    ventana_configuration.title("CONFIGURATION")
    ventana_configuration.geometry("700x600")
    #pH
    textoPh = Label(ventana_configuration, text = "pH")
    textoPh.place(relx=0.10, rely=0.1, relwidth=0.3, relheight=0.08)
    caja_pH = Entry(ventana_configuration)
    caja_pH.place(relx=0.5, rely=0.1, relwidth=0.1, relheight=0.06)
    boton_set_pH = Button(ventana_configuration, text='Guardar pH', fg="black", bg="gray")
    boton_set_pH.place(relx=0.7, rely=0.1, relwidth=0.16, relheight=0.06)

    #Temperatura del agua
    textoTempagua = Label(ventana_configuration, text = "Temperatura del agua")
    textoTempagua.place(relx=0.10, rely=0.2, relwidth=0.3, relheight=0.08)
    caja_Tempagua = Entry(ventana_configuration)
    caja_Tempagua.place(relx=0.5, rely=0.2, relwidth=0.1, relheight=0.06)
    boton_set_Temagua = Button(ventana_configuration, text='Guardar T.Agua', fg="black", bg="gray")
    boton_set_Temagua.place(relx=0.7, rely=0.2, relwidth=0.16, relheight=0.06)

    #Conductividad eléctrica
    textoConduc = Label(ventana_configuration, text = "Conductividad")
    textoConduc.place(relx=0.10, rely=0.3, relwidth=0.3, relheight=0.08)
    caja_Conduc = Entry(ventana_configuration)
    caja_Conduc.place(relx=0.5, rely=0.3, relwidth=0.1, relheight=0.06)
    boton_set_Conduc = Button(ventana_configuration, text='Guardar Conduct', fg="black", bg="gray")
    boton_set_Conduc.place(relx=0.7, rely=0.3, relwidth=0.16, relheight=0.06)

    #Caudal de laa bomba
    textoCaudal = Label(ventana_configuration, text = "Caudal")
    textoCaudal.place(relx=0.10, rely=0.4, relwidth=0.3, relheight=0.08)
    caja_Coaudal = Entry(ventana_configuration)
    caja_Coaudal.place(relx=0.5, rely=0.4, relwidth=0.1, relheight=0.06)
    boton_set_Caudal = Button(ventana_configuration, text='Guardar Caudal', fg="black", bg="gray")
    boton_set_Caudal.place(relx=0.7, rely=0.4, relwidth=0.16, relheight=0.06)

    #Temperatura del ambiente
    textoTempambiente = Label(ventana_configuration, text = "Temperatura ambiente")
    textoTempambiente.place(relx=0.10, rely=0.5, relwidth=0.3, relheight=0.08)
    caja_Temambiente = Entry(ventana_configuration)
    caja_Temambiente.place(relx=0.5, rely=0.5, relwidth=0.1, relheight=0.06)
    boton_set_Teambiente = Button(ventana_configuration, text='Guardar T.Ambiente', fg="black", bg="gray")
    boton_set_Teambiente.place(relx=0.7, rely=0.5, relwidth=0.16, relheight=0.06)

    #Humedad del ambiente
    textohumedad = Label(ventana_configuration, text = "Humedad relativa")
    textohumedad.place(relx=0.10, rely=0.6, relwidth=0.3, relheight=0.08)
    caja_humedad = Entry(ventana_configuration)
    caja_humedad.place(relx=0.5, rely=0.6, relwidth=0.1, relheight=0.06)
    boton_set_humedad = Button(ventana_configuration, text='Guardar humedad', fg="black", bg="gray")
    boton_set_humedad.place(relx=0.7, rely=0.6, relwidth=0.16, relheight=0.06)

     #Nivels de C02 dentro del cultivo
    textoC02 = Label(ventana_configuration, text = "Niveles de Co2")
    textoC02.place(relx=0.10, rely=0.7, relwidth=0.3, relheight=0.08)
    caja_CO2 = Entry(ventana_configuration)
    caja_CO2.place(relx=0.5, rely=0.7, relwidth=0.1, relheight=0.06)
    boton_set_C02 = Button(ventana_configuration, text='Guardar Co2', fg="black", bg="gray")
    boton_set_C02.place(relx=0.7, rely=0.7, relwidth=0.16, relheight=0.06)

def fn_light_red_Control():
    cad = 'F720DF'
    arduino.write(cad.encode('ascii'))
    print(cad)

def fn_light_green_Control():
    cad = 'F7A05F'
    print(cad)

def fn_light_blue_Control():
    cad = 'F7609F'
    print(cad)

def window_light():
    ventana_light = Toplevel()
    ventana_light.title("LIGHT CONTROL")
    ventana_light.geometry("500x400")
    boton_red = Button(ventana_light, text='RED', fg="black", bg="red", command=fn_light_red_Control)
    boton_red.place(relx=0.10, rely=0.1, relwidth=0.15, relheight=0.08)
    boton_green = Button(ventana_light, text='GREEN', fg="black", bg="green", command=fn_light_green_Control)
    boton_green.place(relx=0.1, rely=0.2, relwidth=0.15, relheight=0.08)
    boton_blue = Button(ventana_light, text='BLUE', fg="black", bg="blue", command=fn_light_blue_Control)
    boton_blue.place(relx=0.1, rely=0.3, relwidth=0.15, relheight=0.08)


def window_robotArm():
    ventana_robotArm = Toplevel()
    ventana_robotArm.title("ROBOT ARM")
    ventana_robotArm.geometry("500x400")
    boton_in_mesurements = Button(ventana_robotArm, text='XXXX', fg="black", bg="gray")
    boton_in_mesurements.place(relx=0.10, rely=0.1, relwidth=0.15, relheight=0.08)

def window_scara():
    ventana_scara = Toplevel()
    ventana_scara.title("SCARA")
    ventana_scara.geometry("500x400")
    boton_in_mesurements = Button(ventana_scara, text='XXX', fg="black", bg="gray")
    boton_in_mesurements.place(relx=0.10, rely=0.1, relwidth=0.15, relheight=0.08)

def window_cnc():
    ventana_cnc = Toplevel()
    ventana_cnc.title("CNC")
    ventana_cnc.geometry("500x400")
    boton_in_mesurements = Button(ventana_cnc, text='PRUEBA', fg="black", bg="gray")
    boton_in_mesurements.place(relx=0.10, rely=0.1, relwidth=0.15, relheight=0.08)


class FrameManu(Frame):

        def __init__(self, master=None):
            super().__init__(master,width=650, height=350,bg='green')
            self.master = master
            self.pack()
            self.arduino = serial.Serial("COM3", 9600, timeout = 1.0)
            time.sleep(1)
            self.create_widgets()

    
        def create_widgets(self):
            """self.frame1 = Frame(ventana, bg="blue")
            self.frame1.pack(expand=True, fill='both')

            self.frame2 = Frame(ventana, bg="green")
            self.frame2.pack(expand=True, fill='both')
            self.frame2.config(cursor='heart')"""

            self.btn1 = Button(self, text='MEASUREMENTS', fg="black", bg="gray", command= window_measurements)
            self.btn1.place(relx=0.10, rely=0.1, relwidth=0.15, relheight=0.08)
        
            self.btn2 = Button(self, text='CONFIGURATION', fg="black", bg="gray", command= window_configuration)
            self.btn2.place(relx=0.26, rely=0.1, relwidth=0.15, relheight=0.08)

            self.btn3 = Button(self, text='ROBOT ARM', fg="black", bg="gray", command= window_robotArm)
            self.btn3.place(relx=0.42, rely=0.1, relwidth=0.15, relheight=0.08)

            self.btn4 = Button(self, text='SCARA', fg="black", bg="gray", command= window_scara)
            self.btn4.place(relx=0.58, rely=0.1, relwidth=0.15, relheight=0.08)

            self.btn5 = Button(self, text='CNC', fg="black", bg="gray", command= window_cnc)
            self.btn5.place(relx=0.74, rely=0.1, relwidth=0.15, relheight=0.08)

            self.btn5 = Button(self, text='CONTROL LIGHT', fg="black", bg="gray", command= window_light)
            self.btn5.place(relx=0.74, rely=0.1, relwidth=0.15, relheight=0.08)

ventana = Tk()
ventana.wm_title("Monlee Garden")
app = FrameManu(ventana)
app.mainloop()