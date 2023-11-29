from flask import Flask, render_template, Response
import picamera
import time
import io
import threading
import os

app = Flask(__name__)

def generate():
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.framerate = 24
        time.sleep(2)  # Camera warm-up time

        stream = io.BytesIO()
        for _ in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
            stream.seek(0)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + stream.read() + b'\r\n')
            stream.seek(0)
            stream.truncate()

@app.route('/')
def index():
    return render_template('index.html')  # Ensure you have an 'index.html' file in the 'templates' folder

@app.route('/video_feed')
def video_feed():
    return Response(generate(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def run_server():
    app.run(host='10.66.45.179', port=8000, debug=True, use_reloader=False)

def listen_for_exit():
    while True:
        if input() == 'q':
            print("Exiting...")
            os._exit(0)

if __name__ == '__main__':
    threading.Thread(target=run_server).start()
    listen_for_exit()
