# You can find the library on https://github.com/micropython/micropython-lib/tree/master/umqtt.simple
from umqtt.simple import MQTTClient
import Si7021
import time

def sub_cb(topic, msg):
#Set callback for received subscription messages
#Visualizzo il messaggio solo quando arrivato dal broker MQTT
    print(msg)
        
temp_topic = b"testFLR/temp"
rH_topic = b"testFLR/rH"

s = Si7021.Si7021()
temp = s.readTemp()

c = MQTTClient('clientFLR', 'broker.mqttdashboard.com')#il primo parametro è un nome che posso dare al client
c.set_callback(sub_cb)
c.connect()
c.subscribe(temp_topic)
c.subscribe(rH_topic)

while True:
    temp = s.readTemp()
    temp = '{:03.1f}'.format(temp)
    rH = s.readRH()
    rH = '{:03.1f}'.format(rH)
    c.publish(temp_topic, b'%s' % (temp,))
    c.publish(rH_topic, b'%s' % (rH,))
    time.sleep_ms(1000)
    c.check_msg()#sblocca il temp_topic
    c.check_msg()#sblocca il rH_topic