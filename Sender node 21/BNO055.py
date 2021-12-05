# Simple Adafruit BNO055 sensor reading example.  Will print the orientation
# and calibration data every second.
#
# Copyright (c) 2015 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import logging
import sys
import time

from Adafruit_BNO055 import BNO055

def gyro():
    bno = BNO055.BNO055(rst=18)
    # Create and configure the BNO sensor connection.  Make sure only ONE of the
    # below 'bno = ...' lines is uncommented:
    # Raspberry Pi configuration with serial UART and RST connected to GPIO 18:
    #bno = BNO055.BNO055(serial_port='/dev/serial0', rst=18)
    # BeagleBone Black configuration with default I2C connection (SCL=P9_19, SDA=P9_20),
    # and RST connected to pin P9_12:
    #bno = BNO055.BNO055(rst='P9_12')


    # Enable verbose debug logging if -v is passed as a parameter.
    #if len(sys.argv) == 2 and sys.argv[1].lower() == '-v':
        #logging.basicConfig(level=logging.DEBUG)

     #Initialize the BNO055 and stop if something went wrong.
    if not bno.begin():
        raise RuntimeError('Failed to initialize BNO055! Is the sensor connected?')

    # Print system status and self test result.
    status, self_test, error = bno.get_system_status()
    #print('System status: {0}'.format(status))
    #print('Self test result (0x0F is normal): 0x{0:02X}'.format(self_test))
    # Print out an error if system status is in error mode.
    if status == 0x01:
        print('System error: {0}'.format(error))
        print('See datasheet section 4.3.59 for the meaning.')

    # Print BNO055 software revision and other diagnostic data.
    #sw, bl, accel, mag, gyro = bno.get_revision()
    #print('Software version:   {0}'.format(sw))
    #print('Bootloader version: {0}'.format(bl))
    #print('Accelerometer ID:   0x{0:02X}'.format(accel))
    #print('Magnetometer ID:    0x{0:02X}'.format(mag))
    #print('Gyroscope ID:       0x{0:02X}\n'.format(gyro))

    #print('Reading BNO055 data, press Ctrl-C to quit...')
    #while True:
    # Read the Euler angles for heading, roll, pitch (all in degrees).
    heading, roll, pitch = bno.read_euler()
    # Read the calibration status, 0=uncalibrated and 3=fully calibrated.
    sys, gyro, accel, mag = bno.get_calibration_status()
    # Print everything out.

    resolutionModifier = 10

    # Other values you can optionally read:
    # Orientation as a quaternion:
    #x0,y0,z0,w0 = bno.read_quaterion()
    # Sensor temperature in degrees Celsius:
    #temp_c = bno.read_temp()
    # Magnetometer data (in micro-Teslas):
    x1,y1,z1 = bno.read_magnetometer()
    # Gyroscope data (in degrees per second):
    x2,y2,z2 = bno.read_gyroscope()
    # Accelerometer data (in meters per second squared):
    x3,y3,z3 = bno.read_accelerometer()

    # Linear acceleration data (i.e. acceleration from movement, not gravity--
    # returned in meters per second squared):
    x4,y4,z4 = bno.read_linear_acceleration()
    x4 = x4 * resolutionModifier;
    y4 = y4 * resolutionModifier;
    z4 = z4 * resolutionModifier;
    # Gravity acceleration data (i.e. acceleration just from gravity--returned
    # in meters per second squared):
    x5,y5,z5 = bno.read_gravity()
    x5 = x5 * resolutionModifier;
    y5 = y5 * resolutionModifier;
    z5 = z5 + resolutionModifier;
    # Sleep for a second until the next reading.
    #print("xAccel=",x,"yAccel=",y,"zAccel=",z,"Temperatur=",temp_c,'Heading={0:0.2F} Roll={1:0.2F} Pitch={2:0.2F}\tSys_cal={3} Gyro_cal={4} Accel_cal={5} Mag_cal={6}'.format(
          #heading, roll, pitch, sys, gyro, accel, mag))
    #with open('Output.txt') as f:
    #    last_line = f.readlines()[-1]
    #print(last_line)
    decimalplaces = 4
    delimiter = ","
    gyrolist = ""
    #gyrolist = delimiter.join([str(round(x1,decimalplaces)),str(round(y1,decimalplaces)),str(round(z1,decimalplaces))])
    #tpalist = str(round(x1,decimalplaces)) + delimiter + str(round(y1,decimalplaces)) + delimiter + str(round(z1,decimalplaces))
    #gyrolist = delimiter.join([gyrolist, str(round(x2,decimalplaces)),str(round(y2,decimalplaces)),str(round(z2,decimalplaces))])
    #tpalist = tpalist + delimiter + str(round(x2,decimalplaces)) + delimiter + str(round(y2,decimalplaces)) + delimiter + str(round(z2,decimalplaces))
    #gyrolist = delimiter.join([gyrolist, str(round(x3,decimalplaces)),str(round(y3,decimalplaces)),str(round(z3,decimalplaces))])
    #tpalist = tpalist + delimiter + str(round(x3,decimalplaces)) + delimiter + str(round(y3,decimalplaces)) + delimiter + str(round(z3,decimalplaces))
    #gyrolist = delimiter.join([gyrolist, str(round(x4,decimalplaces)),str(round(y4,decimalplaces)),str(round(z4,decimalplaces))])
    #tpalist = tpalist + delimiter + str(round(x4,decimalplaces)) + delimiter + str(round(y4,decimalplaces)) + delimiter + str(round(z4,decimalplaces))
    #gyrolist = delimiter.join([gyrolist, str(round(x5,decimalplaces)),str(round(y5,decimalplaces)),str(round(z5,decimalplaces))])
    gyrolist = delimiter.join([gyrolist, str(x5), str(y5), str(z5)])
    return gyrolist#,last_line)
    #print("X_Mag=",x1,"Y_Mag=",y1, "Z_Mag=",z1,"X_Gyr=",x2,"Y_Gyr=",y2, "Z_Gyr=",z2,"X_Acc=",x3,"Y_Acc=",y3, "Z_Acc=",z3,"X_LinAcc=",x4,"Y_LinAcc=",y4, "Z_LinAcc=",z4,"X_Grav=",x5,"Y_Grav=",y5, "Z_Grav=",z5)

    #print("xAccel=",x4,"yAccel=",y4,"zAccel=",z4,'Heading={0:0.2F} Roll={1:0.2F} Pitch={2:0.2F} Sys_cal={3} Gyro_cal={4} Accel_cal={5} Mag_cal={6}'.format(
          #heading, roll, pitch, sys, gyro, accel, mag))
    #print(temp_c)
    #time.sleep(1)


