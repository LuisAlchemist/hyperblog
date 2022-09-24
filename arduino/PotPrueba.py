from cProfile import label
from dis import dis
import serial
import time

serialArduino = serial.Serial("COM4", 9600)
time.sleep(1)

while True:
    cad = serialArduino.readline().decode('ascii')

    pos = cad.index(":")
    labael1 = cad[:pos]
    value = cad[pos+1:]

    if labael1 == 'Temp':
        print("El valor de la Temperatura es: {}".format(value))

    if labael1 == 'Pot':
        print("El valor del potenciometro es: {}".format(value))  

    if labael1 == 'HUM':
        print("El valor de la humedad es: {}".format(value))



    #print(cad)
    print("***************")
