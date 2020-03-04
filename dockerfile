FROM python:3.8-slim-buster
ADD Mqtt-Plex-Connector.py .
RUN pip install flask-restful paho-mqtt requests

CMD [ "python", "./Mqtt-Plex-Connector.py" ]
