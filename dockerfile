FROM python:3.11.3-slim

WORKDIR /dashboard-app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install dash dash-extensions dash-bootstrap-components dash-bootstrap-templates
RUN pip install websockets websocket-client paho-mqtt numpy asyncio

COPY . .

EXPOSE 8050
EXPOSE 8123


CMD [ "python", "dashboard/app.py" ]
