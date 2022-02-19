import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# firebase 연결할 url 파일에서 불러오기
firebase_url_file = open('firebase_url.txt', 'r')
firebase_url = firebase_url_file.read()
firebase_url_file.close()

# firebase 연결부
cred = credentials.Certificate('firebase_key.json')
firebase_admin.initialize_app(cred,{'databaseURL':firebase_url})
rdb = db.reference()

# 입력
answer = int(input())

#처리
if answer == 1:
	rdb.update({'light1':'1'})
	rdb.update({'light2':'0'})
else:
	rdb.update({'light1':'0'})
	rdb.update({'light2':'1'})