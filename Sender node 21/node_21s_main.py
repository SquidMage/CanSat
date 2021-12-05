#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import sx126x
import threading
import time
import select
import termios
import tty
import logging
from threading import Timer

#Importing BMP .py file with library and code
from BMP085run import tpa
from BNO055 import gyro

old_settings = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin.fileno())

#    The following is to obtain values from the BMP sensor (Temperature, pressure and altitude)
# We call the BMP sensor function within tpa() function

def TPA():
    return tpa()

def GYRO():
    return gyro()


node = sx126x.sx126x(serial_num = "/dev/ttyS0",freq=868,addr=21,power=22,rssi=False)

# Only the send function is left

def send_cpu_continue(send_to_who,continue_or_not = True):
    global timer_task
    global seconds
    node.send_to = send_to_who
    node.addr_temp = node.addr
    node.set(node.freq,node.send_to,node.power,node.rssi)
    node.send("tpa:" + str(TPA()))
    time.sleep(0.2)
    node.set(node.freq,node.addr_temp,node.power,node.rssi)
    timer_task = Timer(seconds,send_cpu_continue,(send_to_who,))
    timer_task.start()  
    
    # Here we would call the new gyro function
    node.send("gyro:" + str(GYRO()))
    
    # .txt is not generated with this code
    
try:
    
    time.sleep(1)
    print("\n You are sendind data now...\n")
    
    send_to_who = 65535 
    seconds = 1
    
    # The esc key is not sorted out to work. At this point we just closed the cmd when we wanted to run the code again
    
    while True:
        
        if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
            c = sys.stdin.read(1)
          
            pass
        
        else:
            timer_task = Timer(seconds,send_cpu_continue,(send_to_who,))
            timer_task.start()
            
            while True:
                if sys.stdin.read(1) == '\x63':
                    timer_task.cancel()
                    break
            
        sys.stdout.flush()
        
        # timer,send messages automatically
        
except:
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
    # print('\x1b[2A',end='\r')
    # print(" "*100)
    # print(" "*100)
    # print('\x1b[2A',end='\r')

termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
# print('\x1b[2A',end='\r')
# print(" "*100)
# print(" "*100)
# print('\x1b[2A',end='\r')
