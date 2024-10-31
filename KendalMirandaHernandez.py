import network
import socket
import machine
import time

# Configuración de pines
adc_pin = machine.ADC(28)  # Usando el pin ADC (GPIO26 en la Pico W)
button_pin = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_DOWN)  # Botón en GPIO15
pin11 = machine.Pin(0, machine.Pin.OUT)
pin12 = machine.Pin(1, machine.Pin.OUT)

# Configuración de red WiFi
SSID = "Del 1 al 8"
PASSWORD = "12345678"
COMPUTER_IP = "192.168.0.10"  # IP de la computadora
PORT = 12345

# Conectar a la red WiFi
def conectar_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    print("Conectando a la red WiFi...")
    while not wlan.isconnected():
        print(".", end="")
        time.sleep(1)
    print("\nConectado a WiFi")
    print("Configuración de red:", wlan.ifconfig())

# Función para enviar datos al servidor
# Función para enviar datos al servidor
def enviar_datos(sock):
    while True:
        # Leer valor del potenciómetro
        valor_analogico = adc_pin.read_u16()  # Valor entre 0 y 65535
        voltaje = valor_analogico // 100  # Escalar valor a voltaje aproximado
        
        # Construir el mensaje con el formato "CORRIENTE:<valor>"
        mensaje = f"CORRIENTE:{voltaje}"
        
        # Verificar si el botón está presionado
        if button_pin.value() == 1:
            mensaje = "B:presionado"  # Cambia el mensaje si se presiona el botón

        try:
            # Enviar el mensaje
            sock.send(mensaje.encode())
            print("Mensaje enviado:", mensaje)
            
            # Espera 0.5 segundos antes del próximo envío
            time.sleep(0.5)
        except Exception as e:
            print("Error al enviar datos:", e)
            break  # Rompe el bucle si falla el envío

# Función principal que intenta conectar al servidor y enviar datos
def conectar_servidor():
    addr = (COMPUTER_IP, PORT)
    while True:
        try:
            sock = socket.socket()
            sock.connect(addr)
            print("Conectado al servidor en", COMPUTER_IP)
            enviar_datos(sock)  # Envía datos continuamente
        except Exception as e:
            print("Error de conexión:", e)
        finally:
            sock.close()
            print("Intentando reconectar en 5 segundos...")
            time.sleep(5)  # Espera antes de intentar reconectar

# Ejecutar la conexión WiFi y luego conectar al servidor
conectar_wifi(SSID, PASSWORD)
if network.WLAN(network.STA_IF).isconnected():
    conectar_servidor()
