import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from ArduinoConnect import executeArduino

firebase_url_file = open('firebase_url.txt', 'r')

firebase_url = firebase_url_file.read()
firebase_url_file.close()

# firebase 연결
cred = credentials.Certificate('firebase_key.json')
firebase_admin.initialize_app(cred, {'databaseURL': firebase_url})

def loadFirebase():
	rdb = db.reference()

	# 입력
	answer = int(input())

	# 처리
	if answer == 1:
		rdb.update({'light': {"centerFirst": False}} )

executeArduino()