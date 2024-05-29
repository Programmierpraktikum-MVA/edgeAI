import argparse

# Parser zum Einlesen der Kommandozeile initialisieren
parser = argparse.ArgumentParser(description='Start the Flask app with a YOLO model and video input.')
parser.add_argument('model_path', type=str, help='Path to the YOLO model file')
parser.add_argument('video_path', type=str, help='Path to the video file')
args = parser.parse_args()

import cv2
from flask import Flask, Response
from ultralytics import YOLO

app = Flask(__name__)
model = YOLO(args.model_path, task="detect")
cap = cv2.VideoCapture(args.video_path)


def generate_frames():
    """
    Diese Funktion liest Frames aus dem Video, verarbeitet sie mit dem YOLO-Modell
    und generiert die annotierten Frames für die Videoausgabe.
    """
    while cap.isOpened():
        success, frame = cap.read()

        if not success:
            break

        results = model(frame)
        annotated_frame = results[0].plot()

        ret, buffer = cv2.imencode('.jpg', annotated_frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')


@app.route('/')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


app.run(host='0.0.0.0', port=5000)
