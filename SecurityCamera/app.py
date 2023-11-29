from flask import Flask, render_template, Response
import picamera
import time
import io

app = Flask(__name__)

# Global flag to track camera usage
camera_in_use = False

def generate():
    global camera_in_use

    if camera_in_use:
        print("Camera already in use.")
        return

    camera_in_use = True

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

    camera_in_use = False

@app.route('/')
def index():
    return render_template('index.html')  # Ensure you have an 'index.html' file in the 'templates' folder

@app.route('/video_feed')
def video_feed():
    return Response(generate(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='10.66.45.45.179', port=8000, debug=True)

