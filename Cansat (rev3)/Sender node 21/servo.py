def servo(x):
    
    from gpiozero import Servo
    from time import sleep
    servo=Servo(17)
    
    if x > 30:
        servo.min()
        sleep(1)