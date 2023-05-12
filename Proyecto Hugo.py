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


# Loop que se encarga de procesar la opcion escogida, topicos y mensajes
while True:
  choice = menu()

  if choice == '1':
    topic = input("Introduzca el topico al cual quiera suscribirse: ")
    client.subscribe(topic)
    print(f"Suscrito a {topic}")
  elif choice == '2':
    #topic = input("Introduzca el topico a donde quiera mandar su mensaje: ")
    message = input("Introduzca su mensaje: ")
    client.publish(topic, message)
  elif choice == '3':
    print("Saliendo...")
    client.loop_stop()
    break
  else:
    print("Comando invalido. Favor de intentarlo nuevamente")