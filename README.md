# ProyectoHugo
## Proyecto Semana Tec Herramientas computacionales: el arte de la programación (Mayo 2023)

#### Equipo:
#### Daniel De Luna Díaz - A01423940
#### Iker Landeros De La O - A01423214
#### Sergio Alfonso Casillas Santoyo - A01424863


#**Procedimiento:**

_1._ Inicializar servidor MQTT desde terminal de AWS. Para esto, se debe crear una instancia desde la consola de administrador, conectarse a esa instancia, y una vez tenga instalado el paquete Mosquitto, debemos encenderla con el comando **sudo systemctl start mosquitto**. Este servidor deberá tener encendido el puerto 1883, o si no, no podrá funcionar el programa.

_2._ Conectar el servidor al tópico que deseamos. Esto se realiza desde la terminal del servidor de AWS bajo el comando de **mosquitto_sub -h _[dirección IP]_ -t _topico_ -p 1883** . Para realizar eso, es importante conocer la dirección IP del servidor inicializado en el punto anterior.

_3._ Una vez conectado el servidor al tópico deseado, se corre el código de Python llamado **"ProyectoHugo.py"** en cualquier consola. Este código, una vez en funcionamiento, indicará el menú para poder enviar mensajes desde el IDE por el cual se esté corriendo. 
**NOTA:** _Para que este código funcione correctamente, es necesario modificar la dirección de IP que viene señalada en la línea 19._

_4._ Cada vez que se envíe un mensaje, será reflejado en la terminal de AWS. Si no se puede visualizar, uno de los posibles problemas sea que el tópico al que se suscribió el servidor de AWS sea distinto al que se escoge en el IDE donde corre el código de Python.

###### _El código dentro de **"ProyectoHugo.py"** está comentado bajo convenciones del lenguaje de programación_
