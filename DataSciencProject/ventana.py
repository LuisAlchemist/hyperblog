import hesop
import ipaddress
import tkinter

#hesop.open_fille_zilla()
def ejecutar_filla():
    return hesop.open_fille_zilla()

def cambiar_IP_4():
    return ipaddress.change_ip_4_address()



ventana = tkinter.Tk()
ventana.geometry("400x300")

#Selección de la estación en la que vas a descargar LOGS:
estacion = tkinter.StringVar(ventana)
estacion.set('')

#Cambiar dirección IP4
etiqueta_1 = tkinter.Label(ventana, text="Cambia la dirección IP_4")
etiqueta_1.pack()
boton_1 = tkinter.Button(ventana,text="Cambiar dirección IP", command=cambiar_IP_4)
boton_1.pack()

#Descargar LOGS del TCS
etiqueta_2 = tkinter.Label(ventana, text="Aqui puedes descargar los LOGS")
etiqueta_2.pack()
boton_2 = tkinter.Button(ventana,text="Descargar LOGS", command=ejecutar_filla)
boton_2.pack()


ventana.mainloop()