from gpiozero import Servo
from time import sleep
servo=Servo(17)

for i in range(1):
    servo.max()