#!python3
import paho.mqtt.client as mqtt #import the client1
import time
#time imported to be able to put in delays

#broker="test.mosquitto.org"
#broker="broker.heivemq.com"
#broker="iot.eclipse.org"

broker="192.168.1.206"
#ATTENTION IP address

client = mqtt.Client("python1")  #create new instance
print("Connecting to broker ", broker)
client.connect(broker) #connect to broker

time.sleep(4)

client.disconnect() #disconnect
