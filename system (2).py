import time
import os
while True:
    os.system("sudo python3 BMP180.py >> BMP.txt")
    os.system("sudo python3 BNO055.py >> Output.txt")
    
    time.sleep(0.5)
