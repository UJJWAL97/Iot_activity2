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
    print(str(message.topic).split('/')[1])
    recv_data=ast.literal_eval(message.payload.decode('utf8'))
    print(curr)
    print(recv_data)
    d=distance(curr,recv_data)
    print(d)
    if(d<25):
	
	contact.append(str(message.topic).split('/')[1])


Connected = False  # global variable for the state of the connection
#Task-1 Write code here
client_name=sys.argv[1]


curr=location_generator()
broker_address = "127.0.0.1"  # Broker address
port = 1883  # Broker port

#Task-2 Write code here
client = mqttClient.Client(client_name,clean_session=True)  # create new instance

client.on_connect = on_connect  # attach function to callback
client.on_message = on_message  # attach function to callback


client.connect(broker_address, port=port)  # connect to broker


client.loop_start()  # start the loop

#Task-3 Write code here
for i in all_clients:
    if i != client_name:
	print(i)
        client.subscribe("location/"+i)


while Connected != True:  # Wait for connection
    time.sleep(0.1)

end_time=time.time()+15
while time.time() < end_time:
    # Task-4 Write code here
    client.publish("location/"+client_name,str(location_generator()))
    time.sleep(2)
    curr=location_generator()

print("exiting")
client.disconnect()
client.loop_stop()

print(contact)
time.sleep(10)
