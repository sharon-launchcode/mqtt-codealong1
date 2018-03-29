#!python3
import paho.mqtt.client as mqtt #import the client1
import time
#time imported to be able to put in delays
def on_log(client, userdata, level, buf):
        print("log:  "+buf)
def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("Connected OK")
    else:
        print("Bad connection Returned code=",rc)
#Start Add disconnect message part one used by part two below
def on_disconnect(client, userdata, flags, rc=0):
        print(Disconnected result code " +str(rc))
#End add disconnect message part one
              
#broker="test.mosquitto.org"
#broker="broker.heivemq.com"
#broker="iot.eclipse.org"

broker="192.168.1.206"
#ATTENTION IP address
#There is a publically accessible sandbox server for the Eclipse IoT projects available at iot.eclipse.org, port 1883
#https://eclipse.org/paho/
#iot.eclipse.org > 198.41.30.241

client = mqtt.Client("python1")  #create new instance
client.on_connect=on_connect #blind call back function
#Start Add disconnect message part two
client.on_disconnect=on_disconnect
#End Add disconnect message part two             
client.on_log=on_log

print("Connecting to broker ", broker)
client.connect(broker) #connect to broker
client.loop_start() #Start loop
#Start Add disconnect message part three
client.publish("house/sensor1","my first message")
#End Add disconnect message part three              
time.sleep(4)
client.loop_stop() #Stop loop
client.disconnect() #disconnect
