import torch
import cv2

def test_GPU():
    if torch.cuda.is_available():
        print(f"CUDA is available. Your GPU: {torch.cuda.get_device_name(0)}")
    else:
        print("CUDA is not available. Please check your installation.")


def test_webcam():
    # Versuche, die Webcam zu öffnen (Index 0 für die Standard-Webcam)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Fehler: Webcam konnte nicht geöffnet werden. Stellen Sie sicher, dass die Kamera angeschlossen und zugänglich ist.")
        return

    # Lese ein einzelnes Bild von der Webcam
    ret, frame = cap.read()

    if not ret:
        print("Fehler: Konnte kein Bild von der Webcam lesen.")
        cap.release()
        return

    # Zeige das Bild in einem Fenster an
    cv2.imshow('Webcam Test', frame)

    # Warte auf eine Taste, um das Fenster zu schließen
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Schließe den VideoCapture
    cap.release()
    print("Webcam was successfully recognized ")

if __name__ == "__main__":
    test_GPU()
    test_webcam()

