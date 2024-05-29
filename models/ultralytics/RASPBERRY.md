# Deploying to raspberry pi

This is tested on a Raspberry Pi 4 Model B Rev 1.1 running Raspberry Pi OS Lite (64bit). I chose 64bit because I heard that it's necessary for pytorch. Maybe that's not true or even better, we can completely get rid of pytorch for inference and use a 32bit system instead.

**[Ultralytics Raspberry Pi Docs and Benchmarks](https://docs.ultralytics.com/guides/raspberry-pi/)**

## Finding and connecting to the Raspberry Pi

Try to connect to the Raspberry Pi using the user you set up and the device name.

```sh
ssh <user>@raspberrypi
```
If this works, gg. If not, follow the steps below.

In my case, all user devices are to be found in the subnetwork 2. Change that to whatever is the case for your network and then scan the network.

```sh
sudo nmap -sn 192.168.2.0/24
```

This should yield all of the devices in your network, then simply connect to it using ssh and the user you set up for the device.

```sh
ssh <user>@<ip_address>
```

## Sending files to the Raspberry Pi over the network

Example to send a .pt file over the network.

```sh
scp runs/detect/train7/weights/best.pt pierre@raspberrypi:/home/<user>
```

Add a `-r` flag if you want to send a directory. This is usefull for models in ncnn format.

```sh
scp -r runs/detect/train7/weights/best_ncnn_model/ pierre@raspberrypi:/home/<user>
```

## Benchmarks

| model   | format   | speed  |
| ------- | -------- | ------ |
| Yolov8  | ncnn     | 375ms  |
| YOLOv8  | openvino | 550ms  |
| YOLOv8  | onnx     | 575ms  |
| Yolov10 | onnx     | 600ms  |
| Yolov10 | normal   | 800ms  |
| Yolov8  | normal   | 1100ms |
| Yolov10 | ncnn     | error  |
| YOLOv10 | openvino | error  |

Unfortunately some layer used in the YOLOv10 archticture ins't implemented in the ncnn library. At least that's my guess. If we could get YOLOv10 to run with ncnn we would probably get a really nice performance boost.