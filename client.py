import paho.mqtt.client as mqttClient
import time
import ast
import random
import math
import sys

all_clients=[]
for i in range(1,11):
    all_clients.append('client'+str(i))
contact=[]

def location_generator():
    corr={'x':random.randrange(0,250,1),
          'y':random.randrange(0,250,1)}
    return corr

def distance(curr,to):
    return math.sqrt((to['x']-curr['x'])**2+(to['y']-curr['y'])**2)



def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected  # Use global variable
        Connected = True  # Signal connection
    else:
        print("Connection failed")

def on_message(client, userdata, message):
    #Task-5 Write code here


Connected = False  # global variable for the state of the connection
#Task-1 Write code here
client_name=


curr=location_generator()
broker_address = "127.0.0.1"  # Broker address
port = 1883  # Broker port

#Task-2 Write code here
client =   # create new instance

client.on_connect = on_connect  # attach function to callback
client.on_message = on_message  # attach function to callback


client.connect(broker_address, port=port)  # connect to broker


client.loop_start()  # start the loop

#Task-3 Write code here



while Connected != True:  # Wait for connection
    time.sleep(0.1)

end_time=time.time()+15
while time.time() < end_time:
    # Task-4 Write code here


print("exiting")
client.disconnect()
client.loop_stop()

print(contact)
time.sleep(10)
