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

#broker="test.mosquitto.org"
#broker="broker.heivemq.com"
#broker="iot.eclipse.org"

broker="192.168.1.206"
#ATTENTION IP address
#There is a publically accessible sandbox server for the Eclipse IoT projects available at iot.eclipse.org, port 1883
#https://eclipse.org/paho/
#iot.eclipse.org > 198.41.30.241

client = mqtt.Client("python1")  #create new instance
#start Add links to callback functions
client.on_connect=on_connect #blind call back function
client.on_log=on_log

#end Add links to callback functions

print("Connecting to broker ", broker)
client.connect(broker) #connect to broker

time.sleep(4)

client.disconnect() #disconnect
