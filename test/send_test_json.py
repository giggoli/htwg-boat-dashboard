import paho.mqtt.publish as sender
import time

host = "192.168.178.30"


def send_msg(payload, topic):
    sender.single(topic, payload, hostname=host)



with open("test/JSON_files/fuellevel.json", "r") as file:
    send_msg(file.read(), "fuellevel")
    

if __name__ == "__main__":
    for i in range(10):
        print(f"Remaining loops {10-i}")
        with open("test/JSON_files/fuellevel.json", "r") as file:
            send_msg(file.read(), "fuellevel")
        with open("test/JSON_files/gps.json", "r") as file:
            send_msg(file.read(), "gps")
        with open("test/JSON_files/fuelcell.json", "r") as file:
            send_msg(file.read(), "fuelcell")
        with open("test/JSON_files/weather.json", "r") as file:
            send_msg(file.read(), "weather")
        with open("test/JSON_files/batcoap.json", "r") as file:
            send_msg(file.read(), "batcoap")
        with open("test/JSON_files/solar.json", "r") as file:
            send_msg(file.read(), "solar")
        

        time.sleep(1)
        with open("test/JSON_files/fuellevel2.json", "r") as file:
            send_msg(file.read(), "fuellevel")
        with open("test/JSON_files/gps2.json", "r") as file:
            send_msg(file.read(), "gps")
        with open("test/JSON_files/fuelcell2.json", "r") as file:
            send_msg(file.read(), "fuelcell")
        with open("test/JSON_files/weather2.json", "r") as file:
            send_msg(file.read(), "weather")
        with open("test/JSON_files/batcoap2.json", "r") as file:
            send_msg(file.read(), "batcoap")
        with open("test/JSON_files/solar.json", "r") as file:
            send_msg(file.read(), "solar")
        

        time.sleep(1)