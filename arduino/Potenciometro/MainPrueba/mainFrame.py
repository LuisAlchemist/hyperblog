from cProfile import label
from tkinter import Frame, Label, Button, Checkbutton, Scale, StringVar, IntVar
import serial
import time
import threading



class MainFrame(Frame):

	def __init__(self, master = None):
		super().__init__(master, width=520, height=370)
		self.master = master
		#self.master.protocol('WN_DELETE_WINDOW',self.askQuit) #para de enviar y recibir datos cuando la ventana este cerrada
		self.pack()
		self.hilo1 = threading.Thread(target=self.getSensorValues, daemon=True)
		self.serialArduino = serial.Serial("COM4", 9600, timeout = 1.0)
		time.sleep(1)
		self.value_pot = StringVar()
		self.value_humedad = StringVar()
		self.value_temperatura = StringVar()
		self.value_led = IntVar()
		self.value_mot = StringVar()
		self.create_widgets()
		self.isRun = True #siempre ubicarla antes de iniciar el hilo
		self.hilo1.start()

	def askQuit(self):
		self.isRun = False
		self.serialArduino.close()
		self.hilo1.join(0.1)
		self.master.quit()
		self.master.destroy()
		print("***** finalizado...")



	def getSensorValues(self):
		global label
		while self.isRun:
			cad = self.serialArduino.readline().decode('ascii').strip()
			if cad:
				pos = cad.index(":")
				label = cad[:pos]
				value = cad[pos+1:]
			if label == 'HUM':
				self.value_humedad.set(value)
			if label == 'Temp':
				self.value_temperatura.set(value)
			if label == 'Pot':
				self.value_pot.set(value)



	def fnEnviaLed(self):
		cad = 'led:' + str(self.value_led.get())
		self.serialArduino.write(cad.encode('ascii'))
		print(cad)

	def fnEnviaMot(self):
		cad = "mot:" + self.value_mot.get()
		self.serialArduino.write(cad.encode('ascii'))
		print(cad)

	def create_widgets(self):
		Label(self, text="Potenciometro:").place(x=30, y =20)
		Label(self, width=6, textvariable= self.value_pot).place(x=120, y =20)

		Label(self, text="Humedad:").place(x=30, y =50)
		Label(self, width=6, textvariable= self.value_humedad).place(x=120, y =50)

		Label(self, text="Temperatura:").place(x=30, y =100)
		Label(self, width=6, textvariable= self.value_temperatura).place(x=120, y =100)

		Checkbutton(self, text="Encender/apagar Led", variable=self.value_led,onvalue=1, offvalue=0,
		command= self.fnEnviaLed).place(x=30, y=200)

		Label(self, text="Servo:").place(x=30, y =300)
		Button(self, text="Enviar", command=self.fnEnviaMot).place(x=330, y=300)

		Scale(self, from_=0, to=180, orient='horizontal', tickinterval=20,
		length=220, variable=self.value_mot).place(x=90, y=285)