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



# Variables globales
broker_address = "3.82.107.119"
client = mqtt.Client("CombinedClient")

# Callback para cuando recibes mensaje
client.on_message = on_message
# Establece conexion
client.connect(broker_address)
# Loop para siguiente funcion
client.loop_start()
