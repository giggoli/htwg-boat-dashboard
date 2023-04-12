import paho.mqtt.publish as sender
import time

host = "192.168.178.50"


def send_msg(payload, topic):
    sender.single("fuellevel", payload, hostname=host)



with open("test/JSON_files/fuellevel.json", "r") as file:
    send_msg(file.read(), "fuellevel")
    

if __name__ == "__main__":
    for i in range(10):
        print(f"Remaining loops {10-i}")
        with open("test/JSON_files/fuellevel.json", "r") as file:
            send_msg(file.read(), "fuellevel")
        
        time.sleep(2)
        
        with open("test/JSON_files/fuellevel2.json", "r") as file:
            send_msg(file.read(), "fuellevel")
        
        time.sleep(2)