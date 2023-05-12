# Libreria
import paho.mqtt.client as mqtt

# Funcion cuando recibes mensajes
def on_message(client, userdata, message):
    print(f"Mensaje recibido: {message.payload.decode()}")

# Menu de opciones
def menu():
    print("Hola! Por favor escoja una de las siguientes opciones:")
    print("1) Suscribirse a topico")
    print("2) Mandar mensaje")
    print("3) Salir")
    return input("Favor de introducir el numero de su eleccion: ")
