# publisher

import time
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import circuit 

GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

def ledOnOff(led, onOff):
  GPIO.output(led, onOff)
  
ledTem = 6
ledHum = 13
ledIllum = 19

GPIO.setup(ledTem, GPIO.OUT)
GPIO.setup(ledHum, GPIO.OUT)
GPIO.setup(ledIllum, GPIO.OUT)

broker_ip = "localhost" # 현재 이 컴퓨터를 브로커로 설정

client = mqtt.Client()
client.connect(broker_ip, 1883)
client.loop_start()

while(True):
  # 온도를 측정하고 적정 범위를 벗어나면 경고메세지를 보내고 LED에 불이 들어오게 한다.
  tem = circuit.measureTem()
  if tem > 40 :
    onOff=1
  ledOnOff(ledTem, onOff)
  msg1 = "온도가 적정 범위를 벗어났습니다 : " + str(tem)
  client.publish("warning", msg1, qos=0)
  elif tem <= 40 :
    onOff=0
  ledOnOff(ledTem, onOff)
  client.publish("temperature", tem, qos=0)
 
  # 습도를 측정하고 적정 범위를 벗어나면 경고메세지를 보내고 LED에 불이 들어오게 한다. 
  hum = circuit.measureHum()
  if hum > 40 :
    onOff = 1
  ledOnOff(ledHum, onOff)
  msg2 = "습도가 적정 범위를 벗어났습니다 : " + str(hum)
  client.publish("warning", msg2, qos=0)
  elif hum <= 40:
    OnOff = 0
  ledOnOff(ledHum,OnOff)
  client.publish("humidity", hum, qos=0)
  
# 조도를 측정하고 적정 범위를 벗어나면 경고메세지를 보내고 LED에 불이 들어오게 한다.
  illum = circuit.measureIllum()
  if illum > 200 :
    onOff=1
  ledOnOff(ledIllum, onOff)
  msg3 = "조도가 적정 범위를 벗어났습니다 : " + str(illum) 
  client.publish("warning", msg3, qos=0)
  elif illum <=200 :
    onOff=0
  ledOnOff(ledIllum, onOff)
  client.publish("illuminance",illum, qos=0)
  time.sleep(1)
  
client.loop_stop()
client.disconnect()
