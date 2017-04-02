import time

from paho.mqtt.client import Client as MQTTClient

from config import NIBE_UPLINK_CONF, MQTT_CONF
from nibe_downlink import NibeDownlink

nd = NibeDownlink(**NIBE_UPLINK_CONF)
mqtt_client = MQTTClient()
if 'auth' in MQTT_CONF:
  mqtt_client.username_pw_set(**MQTT_CONF['auth'])
mqtt_client.connect(MQTT_CONF['hostname'])
mqtt_client.loop_start()

while True:
  online, values = nd.getValues()
  # print values
  mqtt_client.publish(MQTT_CONF['prefix'] + '/online', 1 if online else 0, retain=True)
  if values:
    for key, value in values.iteritems():
      mqtt_client.publish(MQTT_CONF['prefix'] + '/variables/' + str(key), value, retain=True)
  time.sleep(60)
