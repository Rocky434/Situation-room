from multiprocessing.sharedctypes import Value
from threading import local
from flask import Flask , render_template
from numpy import var
from flask_mqtt import Mqtt
from flask_bootstrap import Bootstrap
import json
data1 =dict()
app = Flask(__name__)
'''app.config['MQTT_BROKER_URL'] = 'www.coolerd.net'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_REFRESH_TIME'] = 1.0 
mqtt = Mqtt(app)
@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('Try/MQTT/CarData')
    
@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    payload=message.payload.decode()
    p = json.loads(payload)
    data = eval(p)
    global data1
    data1=data
'''
@app.route('/')
def index():
    title='電動車'
    data =  {'la':  23.70210039692756 , 'lo': 120.42595030807432}
    ###print(data)
    #return render_template('index.html',title = title,dataa=data)
    return render_template('index.html',title = title,dataa=data)
if __name__ == '__main__':
    app.run(debug=True ,host='0.0.0.0',port=3000)