from tkinter import *
from tkinter import Tk, Label
import time
import random
import os
from PIL import ImageTk, Image
import socket
import threading


window = None

height = 785
width = 620

def main_window():
    global window, height, width
    window = Tk()
    window.minsize(height=height, width=width)
    window.resizable(height=False, width=False)
    window.title("PINBALL CE")

    

    #importar background
    background = Image.open("PinballWizard.png")
    background = background.resize((620,785), Image.Resampling.LANCZOS)

    bgmenu = ImageTk.PhotoImage(background)
    label_bgmenu = Label(window, image=bgmenu)
    label_bgmenu.pack()

    #Se definen los botones
    button_game1 = Button(window, text="1 JUGADOR", height=2, width=10, bg="#dd64ed", command=one_player).place(x=310, y=200)
    button_game2 = Button(window, text="2 JUGADORES", height=2, width=10, bg="#dd64ed", command=two_players).place(x=310, y=250)
    button_game1 = Button(window, text="CONFIGURACIÓN", height=2, width=10, bg="#dd64ed", command=configuracion).place(x=310, y=300)
    button_about = Button(window, text="ABOUT", height=2, width=15, bg="#dd64ed", command=about).place(x=310, y=350)
    

    window.mainloop()

def one_player():
    global window, height, width, server_socket

    window.destroy()
    window = Tk()
    window.minsize(height=height, width=width)
    window.resizable(height=False, width=False)
    window.title("PINBALL CE")

    background = Image.open("PinballWizard.png")
    background = background.resize((620,785), Image.Resampling.LANCZOS)

    bgmenu = ImageTk.PhotoImage(background)
    label_bgmenu = Label(window, image=bgmenu)
    label_bgmenu.pack()


    texto_label = "ESPERANDO CONEXIÓN CON PINBALL..."

    # Configuración del servidor
    HOST = "0.0.0.0"  # Escucha en todas las interfaces de red
    PORT = 12345

    # Crear un socket y enlazarlo al puerto
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    # Crear el Label de estado de conexión
    label_conexion = Label(window, text=texto_label, font=("Arial", 16))
    label_conexion.pack()
    label_conexion.place(x=100, y=50)

    # Función para aceptar conexiones sin bloquear la interfaz gráfica
    def esperar_conexion():
        global server_socket, conn
        conn, addr = server_socket.accept()
        print("Conexión establecida con:", addr)
        label_conexion.config(text="CONEXIÓN ESTABLECIDA, INGRESE SU NOMBRE")
        conn.send(b"P")  # Mensaje de control para la Pi Pico

    # Ejecuta la función en un hilo separado
    window.after(100, esperar_conexion)

    jugador1_textvar = StringVar()
    jugador1 = Entry(window, textvariable=jugador1_textvar)
    jugador1.place(x=275, y=300)

    def guardar_nombre():
        nombre = jugador1_textvar.get()
        elegir_bandera()


    # Botón para guardar el nombre
    boton_guardar = Button(window, text="Guardar Nombre", command=guardar_nombre, bg="red")
    boton_guardar.place(x=300, y=320)

    
    window.mainloop()

def elegir_bandera():
    global window, height, width, flag_images, arrow_label

    # Inicializar la ventana de nuevo
    window.destroy()
    window = Tk()
    window.minsize(height=height, width=width)
    window.resizable(height=False, width=False)
    window.title("PINBALL CE")

    # Fondo de la ventana
    background = Image.open("PinballWizard.png").resize((620, 785), Image.Resampling.LANCZOS)
    bgmenu = ImageTk.PhotoImage(background)
    label_bgmenu = Label(window, image=bgmenu)
    label_bgmenu.image = bgmenu  # Mantener referencia
    label_bgmenu.pack()

    # Título
    texto_label = Label(window, text="ELIGE TU BANDERA", font=("Arial", 16))
    texto_label.place(x=200, y=100)

    # Cargar las imágenes de las banderas y mantenerlas en una lista para que no sean eliminadas
    flag_images = []  # Lista para mantener las referencias


    alemania = Image.open("alemania_flag.png").resize((100, 80), Image.Resampling.LANCZOS)
    brazil = Image.open("brazil_flag.png").resize((100, 80), Image.Resampling.LANCZOS)
    israel = Image.open("israel_flag.png").resize((100, 80), Image.Resampling.LANCZOS)
    tailandia = Image.open("tailandia_flag.png").resize((100, 80), Image.Resampling.LANCZOS)

    arrow = Image.open("flecha.png").resize((70, 80), Image.Resampling.LANCZOS)

    # Crear los objetos PhotoImage y guardarlos en la lista
    alemania_flag = ImageTk.PhotoImage(alemania)
    brazil_flag = ImageTk.PhotoImage(brazil)
    israel_flag = ImageTk.PhotoImage(israel)
    tailandia_flag = ImageTk.PhotoImage(tailandia)

    arrow_objeto = ImageTk.PhotoImage(arrow)

    flag_images.extend([alemania_flag, brazil_flag, israel_flag, tailandia_flag, arrow_objeto])

    

    # Mostrar las imágenes en la interfaz
    label_alemania = Label(window, image=alemania_flag)
    label_alemania.place(x=320, y=250)

    label_brazil = Label(window, image=brazil_flag)
    label_brazil.place(x=320, y=340)

    label_israel = Label(window, image=israel_flag)
    label_israel.place(x=320, y=430)

    label_tailandia = Label(window, image=tailandia_flag)
    label_tailandia.place(x=320, y=520)


    arrow_label = Label(window, image=arrow_objeto)
    arrow_label.place(x=270, y=250)


    bandera_jugador = None
    seleccion_actual = None  # Nueva variable para almacenar la última selección

    # Función para mover la flecha y detectar la selección de bandera
    def mover_arrow(voltaje, mensaje):
        global bandera_jugador, seleccion_actual

        # Verificar si el voltaje es válido para mover la flecha
        if voltaje is not None:
            if 600 <= voltaje <= 610:
                arrow_label.place(x=270, y=250)
                seleccion_actual = label_alemania
            elif 610 < voltaje <= 620:
                arrow_label.place(x=270, y=340)
                seleccion_actual = label_brazil
            elif 630 <= voltaje <= 640:
                arrow_label.place(x=270, y=430)
                seleccion_actual = label_israel
            elif 640 < voltaje <= 655:
                arrow_label.place(x=270, y=520)
                seleccion_actual = label_tailandia

        # Verificar si el mensaje indica que el botón fue presionado
        if mensaje == "B" and seleccion_actual is not None:
            bandera_jugador = seleccion_actual  # Asigna la última selección realizada
            print(f"Bandera seleccionada por el jugador: {bandera_jugador}")

    # Configuración del socket para recibir datos desde la Pico W
    def recibir_datos():
        global conn
        while True:
            try:
                data = conn.recv(1024).decode()
                if not data:
                    break

                # Verificar si los datos tienen el formato esperado
                if data.startswith("CORRIENTE:"):
                    try:
                        # Extraer el valor de voltaje
                        voltaje_str = data.split(":")[1]
                        voltaje = int(voltaje_str.strip())  # Convertir voltaje a entero

                        # Mover la flecha según los datos recibidos
                        mover_arrow(voltaje, "CORRIENTE")

                    except ValueError:
                        print("Error al procesar los datos: formato de voltaje no válido")
                        continue  # Ignora y continúa al siguiente dato

                elif data == "B:presionado":
                    mover_arrow(None, "B")  # Llama a la función para el botón presionado
                    print("Botón presionado. Movimiento finalizado.")
                    break  # Detiene la escucha al recibir "B:presionado"

                else:
                    print("Formato de datos incorrecto:", data)

            except ConnectionResetError:
                print("Conexión perdida.")
                break

    # Iniciar la recepción de datos en un hilo separado
    recepcion_thread = threading.Thread(target=recibir_datos)
    recepcion_thread.daemon = True  # Para que el hilo se cierre cuando la ventana se cierre
    recepcion_thread.start()



    window.mainloop()











def two_players():
    pass

def configuracion():
    pass

def about():
    pass



main_window()
