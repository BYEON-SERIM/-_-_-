from flask import Flask, render_template, request
import picamera
import os
import time

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route("/camera")
def controlCamera():
  fname = takePicture()
  return render_template("camera.html", path = request.path, fname = fname)

camera = None
fileName = "" 

def takePicture():
  global fileName
  global camera
  
 if len(fileName) != 0:
   os.unlink(fileName)
 if camera == None:
   camera = picamera.PiCamera()
 takeTime = time.time()
 fileName = "./static/%d.jpg" % (takeTime * 10) # 촬영한 파일 이름 만들기
 camera.capture(fileName, use_video_port = True) # 카메라 촬영 지시
 return "%d.jpg" % (takeTime * 10) # 촬영한 파일 이름 리턴

def stopPicture():
 camera = None
 fileName = ""
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080) 
