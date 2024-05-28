import cv2
from flask import Flask, Response
from ultralytics import YOLO

app = Flask(__name__)

model = YOLO("runs/detect/train7/weights/best.pt")

video_path = "person-bicycle-car-detection.mp4"
cap = cv2.VideoCapture(video_path)

def generate_frames():
    while cap.isOpened():
        success, frame = cap.read()

        if not success:
            break

        results = model.track(frame, persist=True)
        annotated_frame = results[0].plot()

        ret, buffer = cv2.imencode('.jpg', annotated_frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
