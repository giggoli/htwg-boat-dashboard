from websocket import create_connection
from paho.mqtt import client as mqtt_client
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import configloader.config as cnf

def connect_mqtt(user, broker, port):
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT broker")
        else:
            print("Failed to connect, CODE %d", rc)
    
    def on_message(client, userdata, msg):
        print(f'Received: {msg.payload.decode()} from: {msg.topic}')
        ws_adress = f'ws://127.0.0.1:8123/{msg.topic}'
        ws = create_connection(ws_adress)
        ws.send(msg.payload.decode())
        ws.close()

    client = mqtt_client.Client(user)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker, port)
    return client


def subscribe(client, topic): 
    client.subscribe(topic)



def launch_mqtt():
    broker, port, client_name, topics = cnf.getMqttConfig()

    client = connect_mqtt(client_name, broker, port)

    # run loop_forever to subscribe all time
    for topic in topics:
        subscribe(client, topic)

    client.loop_forever()

# if __name__ == "__main__":
#     broker, port, client_name, topics = cnf.getMqttConfig()

#     client = connect_mqtt(client_name, broker, port)

#     # run loop_forever to subscribe all time
#     for topic in topics:
#         subscribe(client, topic)

#     client.loop_forever()
