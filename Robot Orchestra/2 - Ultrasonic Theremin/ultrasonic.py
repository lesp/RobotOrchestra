import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pinTrigger = 2
pinEcho = 3

GPIO.setup(pinTrigger, GPIO.OUT)
GPIO.setup(pinEcho, GPIO.IN)
global Distance

def ultra():
    
    GPIO.output(pinTrigger, False)
    time.sleep(0.5)
    GPIO.output(pinTrigger, True)
    time.sleep(0.00001)
    GPIO.output(pinTrigger, False)
    StartTime = time.time()
    while GPIO.input(pinEcho)==0:
        StartTime = time.time()
    while GPIO.input(pinEcho)==1:
        StopTime = time.time()
    ElapsedTime = StopTime - StartTime
    Distance = ElapsedTime * 34326
    Distance = Distance / 2
    
while True:
    
