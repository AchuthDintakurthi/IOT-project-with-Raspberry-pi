from Adafruit_IO import*
import RPi.GPIO as GPIO
import time, smbus2

ADAFRUIT_IO_KEY = 'fcd3eba32a8e4002a5ea9263d6ddb6f3'
ADAFRUIT_IO_USERNAME = 'Arjun007'

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
bus = smbus2.SMBus(1)

relay_1 = 18
relay_2 = 23
fan = 24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_1,GPIO.OUT)
GPIO.setup(relay_2,GPIO.OUT)
GPIO.setup(fan,GPIO.OUT)

i2cAdd=0x48
A0=0x40
A1=0X41
A2=0X42
A3=0X43

def temp():
	return 2*bus.read_byte_data(i2cAdd,A0,force=None)


'''
feed = Feed(name="Counter")
response = aio.create_feed(feed)
'''
'''
while True:
    print('sending count: ', 50)
    aio.send('temperature', 50)
    time.sleep(10)
'''

while True:
	aio.send('temperature',temp())
	time.sleep(10)
