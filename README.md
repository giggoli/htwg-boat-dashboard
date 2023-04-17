# htwg-boat-dashboard

## Overview
Python based dashboard for the HTQG-Boat. The Dashboard itself is build with python dash and will receive its value via MQTT. The whole project can be used in a docker-container.

<br>

## Requirements
To be able to run the docker-container we need to bind two files. One of the file is a simple config.json file and the other file contains a mapbox token.
>Its not necessary to provide a mapbox token. It will only be used to display values on a map
To get a token visit [Mapbox](https://www.mapbox.com/).

<br>
<br>

---
## How to run
Its suggested to run the dashboard with dokcer-compose. Eitherway you have to pass above mentioned files to the container. The container structure is the following:

```
├── dashboard-app
   ├── configloader
   │   ├── config.json
   │
   ├── dashboard
   │   ├── pages
           ├── .mapboxtoken

```

<br>
<br>

Here you can find a example for a config and for a compse file.


### Example config file
```json
{
    "broker_ip": "your broker ip ",
    "broker_port": 1883,
    "client_name": "dashboard",
    "topics":[
        "batcoap",
        "fuelcell",
        "fuellevel",
        "gps",
        "solar",
        "weather"
    ]
}
```
<br>

### Example compose file
```yml
version: '3.9'
services:
  app:
    image: giggoli/htwg-boat-dashboard:latest
    ports:
      - "8050:8050"
      - "8123:8123"
    volumes:
      - ${PWD}/config.json:/dashboard-app/configloader/config.json
      - ${PWD}/.mapboxtoken:/dashboard-app/dashboard/pages/.mapboxtoken
```
