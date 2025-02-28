# from flask import Flask, render_template, Response
# import cv2

# app = Flask(__name__)

# # Start video capture
# cap = cv2.VideoCapture(0)

# def generate_frames():
#     """Generates video frames for streaming."""
#     while True:
#         success, frame = cap.read()
#         if not success:
#             break
#         else:
#             ret, buffer = cv2.imencode('.jpg', frame)
#             frame = buffer.tobytes()
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# @app.route('/')
# def index():
#     """Render the main HTML page."""
#     return render_template('index.html')

# @app.route('/video_feed')
# def video_feed():
#     """Video streaming route."""
#     return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, Response
import cv2
import os

app = Flask(__name__, template_folder="templates",static_folder="static")

# Initialize video capture
cap = cv2.VideoCapture(0)

def generate_frames():
    """Generates video frames for streaming."""
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    """Render the main index page."""
    return render_template('index.html')

@app.route('/signtotext')
def sign_to_text():
    """Render the sign-to-text page."""
    return render_template('sign_to_text.html')

@app.route('/video_feed')
def video_feed():
    """Video streaming route."""
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/texttovoice')
def text_to_voice():
    """Render the text-to-voice page."""
    return render_template('text_to_voice.html')

@app.route('/voicetotext')
def voice_to_text():
    """Render the voice-to-text page."""
    return render_template('voice_to_text.html')

if __name__ == '__main__':
    app.run(debug=True)
