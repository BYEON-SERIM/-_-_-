import time
import RPi.GPIO as GPIO
from adafruit_htu21d import HTU21D #온습도
import busio #온습도
import Adafruit_MCP3008 #조도
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

sda = 2 # GPIO 핀 번호, sda라고 이름이 보이는 핀
scl = 3 # GPIO 핀 번호, scl이라고 이름이 보이는 핀
i2c = busio.I2C(scl, sda)
sensor = HTU21D(i2c) # HTU21D 장치를 제어하는 객체 리턴
mcp = Adafruit_MCP3008.MCP3008(clk=11, cs=8, miso=9, mosi=10) # 조도

# 온도를 측정하는 함수
def measureTem():
  return float(sensor.temperature)

# 습도를 측정하는 함수
def measureHum():
  return float(sensor.relative_humidity)

# 습도를 측정하는 함수
def measureIllum():
  return mcp.read_adc(0)
