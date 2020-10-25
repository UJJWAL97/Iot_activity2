import paho.mqtt.client as mqttClient
import time
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


def on_message(client, userdata, message):
    #Task-5 Write code here


curr=location_generator()
#Task-1 Write code here
client_name=





#Task-2 Write code here








client.loop_start()  # start the loop

#Task-3 Write code here





end_time=time.time()+15
while time.time() < end_time:
    # Task-4 Write code here


    
 
print("exiting")


print(contact)
time.sleep(10)
