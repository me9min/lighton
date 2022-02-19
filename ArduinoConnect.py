import time

import serial
from firebase_admin import db

def executeArduino():
    dir = db.reference()  # 기본 위치 지정
    print(dir.get())

    ser = serial.Serial(
        port='COM6',
        baudrate=9600
        )
    while True:
        if ser.readable():
            dir = db.reference('light/centerFirst')
            val = dir.get()

            if val == 'Y':
                val = val.encode('utf-8')
                ser.write(val)
                print("LED TURNED ON")
                time.sleep(0.5)

            elif val == 'N':
                val = val.encode('utf-8')
                ser.write(val)
                print("LED TURNED OFF")
                time.sleep(0.5)