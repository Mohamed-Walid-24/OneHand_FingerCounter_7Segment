#Version : 3
import cv2
from HandTrackingModule import HandDetector

fingersTip = [8, 12, 16, 20]
fingersPip = [6, 10, 14, 18]


class FingerCounting:
    def __init__(self, img, maxHand):
        self.img = img
        self.maxHand = maxHand
        self.detector = HandDetector(img=self.img, maxHand=maxHand)
        self.Tip_y = []
        self.Pip_y = []
        self.fingers = []

    def count(self):

        self.detector.propDots(color=(255, 100, 50), radius=3)
        self.detector.propConn(color=(150, 200, 255), thick=2)
        self.detector.findHand(showDot=False, showDotConn=True)

        if self.findPos(0, 0) is not None:
            if self.detector.handShown() == 1:
                return self.oneHand(0)

    def oneHand(self, handNo):
        pos_17 = self.findPos(handNo, 17)[0]
        pos_5 = self.findPos(handNo, 5)[0]
        if pos_17 > pos_5:  # RightHand
            number = FingerCounting.fingers(self, handNo)
            number += self.thumb(handNo, True)
            return number
        elif pos_17 < pos_5:  # LeftHand
            number = FingerCounting.fingers(self, handNo)
            number += self.thumb(handNo, False)
            return number

    def twoHand(self): # Not working Properly
        #print("0", self.oneHand(0))
        # print("1", self.oneHand(1))
        number = self.oneHand(0) + self.oneHand(1)
        return number

    def findPos(self, handNo, pointNo):
        return self.detector.findPosition(handNo=handNo, pointNo=pointNo)

    def fingers(self, handNo):
        self.Tip_y = list(map(lambda x: self.findPos(handNo, x)[1], fingersTip))
        self.Pip_y = list(map(lambda y: self.findPos(handNo, y)[1], fingersPip))
        for k in range(0, 4):
            if self.Tip_y[k] < self.Pip_y[k]:
                self.fingers.append(1)
            else:
                self.fingers.append(0)
        number = self.fingers.count(1)

        return number

    def thumb(self, handNo, right: bool):
        pos_4 = self.findPos(handNo, 4)
        pos_3 = self.findPos(handNo, 3)
        if pos_4 < pos_3:
            if right:
                return 1
            else:
                return 0
        else:
            if right:
                return 0
            else:
                return 1


def main():
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        counting = FingerCounting(img, maxHand=1)
        count = counting.count()
        print(count)
        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    main()
