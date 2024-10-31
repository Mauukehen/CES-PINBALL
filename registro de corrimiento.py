import machine
from time import sleep

#num=int(input("Agregue un número en hexadecimal: "))

pin11 = machine.Pin(0, machine.Pin.OUT)
pin12 = machine.Pin(1, machine.Pin.OUT)



entradaAB = machine.Pin(11, machine.Pin.OUT)
        
pinclock = machine.Pin(10, machine.Pin.OUT)


        
entradaAB.value(1)
pinclock.value(1)
sleep(1)
pinclock.value(0)

entradaAB.value(1)
pinclock.value(1)
sleep(1)
pinclock.value(0)

entradaAB.value(1)
pinclock.value(1)
sleep(1)
pinclock.value(0)

entradaAB.value(1)
pinclock.value(1)
sleep(1)
pinclock.value(0)

#########################

entradaAB.value(1)
pinclock.value(1)
sleep(1)
pinclock.value(0)

entradaAB.value(1)
pinclock.value(1)
sleep(1)
pinclock.value(0)

entradaAB.value(1)
pinclock.value(1)
sleep(1)
pinclock.value(0)

entradaAB.value(1)
pinclock.value(1)
sleep(1)
pinclock.value(0)

entradaAB.value(0)
pinclock.value(1)
sleep(1)
pinclock.value(0)

entradaAB.value(0)
pinclock.value(1)
sleep(1)
pinclock.value(0)

entradaAB.value(0)
pinclock.value(1)
sleep(1)
pinclock.value(0)

entradaAB.value(0)
pinclock.value(1)
sleep(1)
pinclock.value(0)

#########################

entradaAB.value(0)
pinclock.value(1)
sleep(1)
pinclock.value(0)

entradaAB.value(0)
pinclock.value(1)
sleep(1)
pinclock.value(0)

entradaAB.value(0)
pinclock.value(1)
sleep(1)
pinclock.value(0)

entradaAB.value(0)
pinclock.value(1)
sleep(1)
pinclock.value(0)

sleep(1)

pin11.value(0)
pin12.value(0)

sleep(1)

pin11.value(1)
pin12.value(1)