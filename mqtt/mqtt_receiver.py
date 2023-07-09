from websocket import create_connection
from paho.mqtt import client as mqtt_client
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import configloader.config as cnf

msg_buffer = dict()

def connect_mqtt(user, broker, port):
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT broker")
        else:
            print("Failed to connect, CODE %d", rc)
    
    def on_message(client, userdata, msg):
        print(f'Received: {msg.payload.decode()} from: {msg.topic}')
        ws_address = f'ws://0.0.0.0:8123/{msg.topic}'
        ws = create_connection(ws_address)
        decoded_msg = msg.payload.decode()
        msg_buffer[msg.topic] = decoded_msg
        ws.send(decoded_msg)
        ws.close()

    client = mqtt_client.Client(user)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker, port)
    return client


def subscribe(client, topic): 
    client.subscribe(topic)

def send_buffered_messages():
    for topic in msg_buffer:
        ws_address = f'ws://0.0.0.0:8123/{topic}'
        ws = create_connection(ws_address)
        ws.send(msg_buffer[topic])
        ws.close()



def launch_mqtt():
    broker, port, client_name, topics = cnf.getMqttConfig()

    client = connect_mqtt(client_name, broker, port)

    # run loop_forever to subscribe all time
    for topic in topics:
        subscribe(client, topic)

    while True:
        client.loop(timeout=1.0)
        send_buffered_messages()


# if __name__ == "__main__":
#     broker, port, client_name, topics = cnf.getMqttConfig()

#     client = connect_mqtt(client_name, broker, port)

#     # run loop_forever to subscribe all time
#     for topic in topics:
#         subscribe(client, topic)

#     client.loop_forever()