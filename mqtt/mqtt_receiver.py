from websocket import create_connection
from paho.mqtt import client as mqtt_client
import config
import os


def connect_mqtt(user, broker, port):
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to broker")
        else:
            print("Failed to connect, CODE %d", rc)
    
    def on_message(client, userdata, msg):
        print(f'received {msg.payload.decode()} from {msg.topic}')
        # currently send whole payload to websocket
        ws_adress = f'ws://127.0.0.1:9001/{msg.topic}'
        ws = create_connection("ws://127.0.0.1:9001")
        ws.send(msg.payload.decode())
        ws.close()

    client = mqtt_client.Client(user)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker, port)
    return client


def subscribe(client, topic): 
    client.subscribe(topic)




if __name__ == "__main__":
    cnf_path = os.path.join(os.path.dirname(__file__), 'config.json')
    cnf = config.getConfig(cnf_path)

    broker = cnf["broker_ip"]
    port = cnf["broker_port"]
    client_name = cnf["client_name"]
    topics = cnf["topics"]

    client = connect_mqtt(client_name, broker, port)

    # run loop_forever to subscribe all time
    for topic in topics:
        subscribe(client, topic)

    client.loop_forever()