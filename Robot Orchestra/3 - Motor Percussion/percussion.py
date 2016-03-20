from gpiozero import Motor
import time
motor1 = Motor(9,10)
motor2 = Motor(7,8)

while True:
    
    for i in range(2):
        motor1.backward(speed=0.3)
        motor2.forward(speed=0.9)
        time.sleep(1)
    for i in range(2):
        motor1.backward(speed=1)
        motor2.forward(speed=0.2)
        time.sleep(1)    
    motor1.stop()
    motor2.stop()
    time.sleep(1)
