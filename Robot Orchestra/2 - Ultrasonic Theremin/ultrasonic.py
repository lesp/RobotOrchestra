import RPi.GPIO as GPIO
import time
from psonic import *

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pinTrigger = 17
pinEcho = 18

GPIO.setup(pinTrigger, GPIO.OUT)
GPIO.setup(pinEcho, GPIO.IN)
global Distance

def ultra():
    
    GPIO.output(pinTrigger, False)

    time.sleep(0.1)

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
    print("Distance : %.1f" % Distance)
    note = Distance /2
    use_synth(MOD_PULSE)
    play(note)
    time.sleep(0.1)

   
while True:
    
    ultra()
    
    
