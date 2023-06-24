import paho.mqtt.publish as sender
import time

#host = "192.168.178.30"
host = "127.0.0.1"


def send_msg(payload, topic):
    sender.single(topic, payload, hostname=host)

   

if __name__ == "__main__":
    for i in range(100):
        print(f"Remaining loops {100-i}")
        with open("test/JSON_files/fuellevel.json", "r") as file:
            send_msg(file.read(), "daq/fuellevel/data")
        with open("test/JSON_files/gps.json", "r") as file:
            send_msg(file.read(), "gps/data")
        with open("test/JSON_files/fuelcell.json", "r") as file:
            send_msg(file.read(), "fuelcell/data")
        with open("test/JSON_files/weather.json", "r") as file:
            send_msg(file.read(), "weather/data")
        with open("test/JSON_files/batcoap.json", "r") as file:
            send_msg(file.read(), "batcoap/data")
        with open("test/JSON_files/solar.json", "r") as file:
            send_msg(file.read(), "solar/data")
        time.sleep(1)

        with open("test/JSON_files/fuellevel2.json", "r") as file:
            send_msg(file.read(), "daq/fuellevel/data")
        with open("test/JSON_files/gps2.json", "r") as file:
            send_msg(file.read(), "gps/data")
        with open("test/JSON_files/fuelcell2.json", "r") as file:
            send_msg(file.read(), "fuelcell/data")
        with open("test/JSON_files/weather2.json", "r") as file:
            send_msg(file.read(), "weather/data")
        with open("test/JSON_files/batcoap2.json", "r") as file:
            send_msg(file.read(), "batcoap/data")
        with open("test/JSON_files/solar2.json", "r") as file:
            send_msg(file.read(), "solar/data")
        time.sleep(1)