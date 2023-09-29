import cv2
import serial
from FingerCountingModule import FingerCounting

port = "com16"
baudRate = 9600
ard = serial.Serial(port, baudRate)


def main():
    cap = cv2.VideoCapture(0)
    last_value = 0
    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        counting = FingerCounting(img, maxHand=1)
        value = counting.count()
        if value != last_value:
            print(value)
            ard.write(str(value).encode(encoding="utf-8"))

        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        last_value = value

if __name__ == "__main__":
    main()
