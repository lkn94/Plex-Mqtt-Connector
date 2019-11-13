from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import requests
import json
import paho.mqtt.publish as publish

app = Flask(__name__)
api = Api(app)

host = 'HOST_OF_MQTT'
topic = 'plex/'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = json.loads(request.form['payload'])
    print(data['event'])
    publish.single(topic + data['Player']['uuid'], data['event'], hostname=host)
    publish.single(topic + data['Player']['uuid'] + '/title', data['Metadata']['title'],
                   hostname=host)
    publish.single(topic + data['Player']['uuid'] + '/type', data['Metadata']['type'],
                   hostname=host)
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
