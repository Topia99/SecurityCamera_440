import Adafruit_DHT

sensor = Adafruit_DHT.DHT11

pin = 2

humidity,temperature = Adafruit_DHT.read_retry(sensor,pin)


if humidity is not None and temperature is not None:
	print(f'temp={temperature:.1f}*C  Humidity={humidity:.1f}%')
else:
	print('faled to read')
