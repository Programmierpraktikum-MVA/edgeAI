import cv2


def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Webcam could not be opened. Make sure the camera is connected and accessible.")
        return

    ret, frame = cap.read()

    if not ret:
        print("Could not read image from webcam.")
        cap.release()
        return

    cv2.imshow("Webcam Test", frame)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cap.release()
    print("Webcam was successfully recognized ")


if __name__ == "__main__":
    main()
