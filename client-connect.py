#!python3
import paho.mqtt.client as mqtt #import the client1
import time
#time imported to be able to put in delays
#first section Add callback functions from time 2:29 in video
def on_log(client, userdata, level, buf):
        print("log:  "+buf)
def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("Connected OK")
    else:
        print("Bad connection Returned code=",rc)
#end first section Add callback

#broker="test.mosquitto.org"
#broker="broker.heivemq.com"
#broker="iot.eclipse.org"

broker="192.168.1.206"
#ATTENTION IP address
#There is a publically accessible sandbox server for the Eclipse IoT projects available at iot.eclipse.org, port 1883
#https://eclipse.org/paho/
#iot.eclipse.org > 198.41.30.241

client = mqtt.Client("python1")  #create new instance
print("Connecting to broker ", broker)
client.connect(broker) #connect to broker

time.sleep(4)

client.disconnect() #disconnect
