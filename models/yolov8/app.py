import argparse
import os
import sys

# Initialize parser for reading the command line
parser = argparse.ArgumentParser(description='Start the Flask app with a YOLO model and video input.')
parser.add_argument('model_path', type=str, help='Path to the YOLO model file')
parser.add_argument('video_path', type=str, help='Path to the video file')
args = parser.parse_args()

import cv2
from flask import Flask, Response
from ultralytics import YOLO

app = Flask(__name__)
model = YOLO(args.model_path, task="detect")
#cap = cv2.VideoCapture(args.video_path)

try:
    # Check if video_path is an integer (for webcam) or a file path
    if args.video_path.isdigit():
        video_path = int(args.video_path)
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            raise ValueError(f"Cannot open the webcam with id {video_path}.")
    else:
        # Check if the file exists
        if not os.path.exists(args.video_path):
            raise FileNotFoundError(f"Video file {args.video_path} does not exist.")

        # Check if the file extension is .mp4
        if not args.video_path.lower().endswith('.mp4'):
            raise ValueError(f"Video file {args.video_path} is not an .mp4 file.")

        cap = cv2.VideoCapture(args.video_path)
        if not cap.isOpened():
            raise ValueError(f"Cannot open the video file {args.video_path}.")

    print("Video source opened successfully.")
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

def generate_frames():
    """
    This function reads frames from the video, processes them with the YOLO model
    and generates the annotated frames for the video output.
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
