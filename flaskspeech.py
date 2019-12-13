from flask import Flask, render_template
# from flask_minio import Minio
from minio import Minio
from minio.error import (ResponseError, BucketAlreadyOwnedByYou, BucketAlreadyExists)
from record import RecordAudio
import fileuploader
from models import User,Post

app = Flask(__name__)
app.config.from_pyfile('fileuploader.py')
db = Minio(app)

# app.config['SECRET_KEY'] = '!ue4U>QAa=~CuEckWm^]EYyZL$kJx,?Pc-f0$HFy'

@app.route("/")
@app.route("/detect")
def detect():
	return "helllo world"

@app.route("/signup")
def signup():
    RecordAudio()
	# return render_template('signup.html')

@app.route("/login")
def login():
	return render_template('login.html')

@app.route("/success")
def success():
	return render_template('success.html')

@app.route('/upload')
def upload_file():
	fileuploader.minioClient
    # res = db.connection.fput_object('maylogs', 'pumaserver_debug.log', '/tmp/pumaserver_debug.log')
    
if __name__=='__main__':
	app.run(debug=True)