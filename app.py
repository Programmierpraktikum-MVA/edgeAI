import argparse

parser = argparse.ArgumentParser()
parser.add_argument("model_path", type=str, help="Path to the YOLO model file")
args = parser.parse_args()

import os
import socket
import gradio as gr
from ultralytics import YOLO

model = YOLO(args.model_path, task="detect")
port = 7860


def predict_video(video, conf_threshold, iou_threshold):
    results = model(
        source=video,
        stream=True,
        conf=conf_threshold,
        iou=iou_threshold,
        show_labels=True,
        show_conf=True,
        imgsz=640,
    )

    for result in results:
        result.save(filename="result.jpg")
        yield "result.jpg"

    return results


iface = gr.Interface(
    fn=predict_video,
    inputs=[
        gr.Video(interactive=True, label="Upload Video"),
        gr.Slider(minimum=0, maximum=1, value=0.25, label="Confidence threshold"),
        gr.Slider(minimum=0, maximum=1, value=0.45, label="IoU threshold"),
    ],
    outputs=gr.Image(type="pil", label="Result"),
    title="Computer Vision on Edge Devices",
    examples=(
        [[os.path.join("videos", file), 0.25, 0.45] for file in os.listdir("videos")]
        if os.path.isdir("videos")
        else []
    ),
)

# https://stackoverflow.com/a/28950776/19264633
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

if __name__ == "__main__":
    print(f"Server started at http://{get_ip()}:{port}")
    iface.launch(server_name="0.0.0.0", server_port=port)