# import sys
# sys.path.append("/home/sakalosj/projects/pagure_initial/src")
# sys.path.append("/home/sakalosj/projects/venv/")
import os

import paho.mqtt.client as mqtt
import ssl

token_packit = os.getenv("PACKIT_TOKEN")

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def on_log(client, userdata, level, buf):
    print(client, userdata, level, buf)


client = mqtt.Client()
client.enable_logger()
client.on_connect = on_connect
client.on_message = on_message
# client.on_log = on_log

client.tls_set(ca_certs="/home/sakalosj/.centos-server-ca.cert", certfile="/home/sakalosj/.centos.cert", keyfile="/home/sakalosj/.centos.cert", cert_reqs=ssl.CERT_REQUIRED,
    tls_version=ssl.PROTOCOL_TLS)

client.connect(host="mqtt.stg.centos.org", port=8883)
# mosquitto_sub --cafile ~/.centos-server-ca.cert --cert ~/.centos.cert --key ~/.centos.cert -h mqtt.centos.org -p 8883 -t \# -v -d

client.loop_forever()