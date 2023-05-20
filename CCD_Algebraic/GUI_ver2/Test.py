import numpy as np
import time
import serial

ser = serial.Serial(port="COM8",baudrate=115200)
#ser.open()
while True:
    din = '1'
    ser.write(din.encode('utf'))
    time.sleep(0.1)
    data = ser.readline().decode('utf')
    ser.flushInput()
    print(data)
    #time.sleep(1)

    