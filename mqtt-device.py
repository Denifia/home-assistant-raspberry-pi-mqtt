#!/usr/bin/env python
import paho.mqtt.client as mqtt
import time
from subprocess import call

#configuration:
brokerAdr = "192.168.X.X"
brokerPort = 1883
brokerUserName = "XXX"
brokerPassword = "XXX"

name = "friendly name"
uniqueId = "unique_id"

availabilityTopic = uniqueId+"/available"
stateTopic = uniqueId+"/power"
commandTopic = uniqueId+"/power/set"
discoveryTopic = "homeassistant/switch/"+uniqueId+"/config"

# "on connect" event
def connectFunction (client, userdata, flags, rc):
  if rc==0:
    print("connected OK Returned code=",rc)
    MyClient.publish(discoveryTopic, "{\"~\":\""+uniqueId+"\"name\":\""+name+"\",\"unique_id\":\""+uniqueId+"\",\"state_topic\":\"~/power\",\"command_topic\":\"~/power/set\",\"availability_topic\":\"~/available\"}", 1, True)
    MyClient.publish(availabilityTopic, "online") # Publish message to MQTT broker
    MyClient.publish(stateTopic, "ON")
    MyClient.subscribe(commandTopic) # Subscribe after re-connect
  else:
    print("Bad connection Returned code=",rc)

# "on message" event
def messageFunction (client, userdata, message):
  topic = str(message.topic)
  payload = str(message.payload.decode("utf-8"))
  print("New message received:", topic+" "+payload)
  if topic==commandTopic:
    handleCommand(payload)

# handle new MQTT command function
def handleCommand (command):
  if command=="reboot":
    MyClient.publish(stateTopic, "OFF")
    call(['shutdown', '-r', 'now'], shell=False) #reboot host
  elif command=="OFF":
    MyClient.publish(stateTopic, "OFF")
    call(['shutdown', '-h', 'now'], shell=False) #shut down host
  elif command=="test":
    MyClient.publish(stateTopic, "Reply to test msg") # Publish reply to an incomming msg with payload "test"

while (1):
  MyClient = mqtt.Client() # Create a MQTT client object
  MyClient.username_pw_set(brokerUserName, brokerPassword)
  MyClient.on_connect = connectFunction # run function on connect with broker
  MyClient.will_set(availabilityTopic, "offline")
  MyClient.connect(brokerAdr, brokerPort) # Connect to the test MQTT broker
  MyClient.on_message = messageFunction # Attach the messageFunction to subscription
  MyClient.loop_forever()
