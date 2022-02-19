import time
import serial
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

def executeArduino():
    dir = db.reference()  # 기본 위치 지정
    print(dir.get())

    ser = serial.Serial(
        port='COM3',
        baudrate=9600
        )

    while True:
        c = input()  # 유저가 입력 '1' 또는 '2' 테스트 하기 위해.
        dir = db.reference('light/centerFirst')
        print(dir.get())
        if dir.get() == "Y":
           c='A'
           c = c.encode("utf-8")
           ser.write(c)

        else:
            pass