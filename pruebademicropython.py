import machine
import time

# Configura los pines GPIO como entradas
pines = [
    machine.Pin(2, machine.Pin.IN),
    machine.Pin(3, machine.Pin.IN),
    machine.Pin(5, machine.Pin.IN),
    machine.Pin(6, machine.Pin.IN),
    machine.Pin(7, machine.Pin.IN)
]
# Bucle infinito para revisar los pines

    # Revisa si alguno de los pines recibe 3.3V (estado alto)
def verificar_pines():
    while True:
        for i, pin in enumerate(pines):
            if pin.value() == 1:
                print(f"El pin {i+2} ha detectado corriente.")
        time.sleep(0.5)

verificar_pines()
