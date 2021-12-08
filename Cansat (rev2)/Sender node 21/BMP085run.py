import BMP085
import time

def tpa():

    while True:
        temp,pressure,altitude=BMP085.readBmp180()
        tpalist = str(temp) + "," + str(pressure) + "," + str(altitude)
        return tpalist
    