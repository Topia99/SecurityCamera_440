import RPi.GPIO as GPIO
import time
import datetime
import picamera
# import Adafruit_DHT

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# Set GPIO Pins for ultrasonic sensor
GPIO_TRIGGER = 17
GPIO_ECHO = 3

# Set GPIO Pin for DHT11 temperature sensor
GPIO_DHT = 22

# Set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

# DHT sensor setup
# sensor = Adafruit_DHT.DHT11

# Initialize camera
camera = picamera.PiCamera()

def distance():
    # Set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # Set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # Save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # Save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # Time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # Multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance

def capture_image():
    timestamp = datetime.datetime.now().isoformat()
    camera.capture('/home/pi/security_images/image_{}.jpg'.format(timestamp))
    print("Image Captured at {}".format(timestamp))

try:
    while True:
        dist = distance()
        print("Measured Distance = {:.1f} cm".format(dist))
        time.sleep(1)

        # Check for motion
        if dist < 50:  # Change 50 to your desired trigger distance
            print("Motion detected!")
            capture_image()

        # # Check temperature
        # humidity, temperature = Adafruit_DHT.read_retry(sensor, GPIO_DHT)
        # if temperature is not None:
        #     print("Temperature = {:.1f}*C".format(temperature))
        #     # Add your temperature change logic here

        time.sleep(1)

except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()

