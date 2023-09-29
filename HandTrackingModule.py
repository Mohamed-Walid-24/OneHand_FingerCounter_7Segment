# Version : 8
import cv2
import mediapipe as mp


class HandDetector:

    def __init__(self, img, maxHand, mode=False, modelComplex=1, detectionCon=0.5, trackCon=0.5):
        self.img = img
        self.mode = mode
        self.maxHand: int = maxHand
        self.modelComplex = modelComplex
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHand, self.modelComplex, self.detectionCon, self.trackCon)

        self.mpDraw = mp.solutions.drawing_utils

        self.dotColor: tuple = (255, 0, 0)
        self.dotRadius: int = 3
        self.connColor: tuple = (0, 0, 0)
        self.connThick: int = 1

        self.results = None

        self.height, self.width, c = self.img.shape

    def findHand(self, showDot=True, showDotConn=True):
        imgRGB = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if showDot:
                    dotSpec = self.mpDraw.DrawingSpec(color=self.dotColor, circle_radius=self.dotRadius)
                    self.mpDraw.draw_landmarks(self.img,
                                               landmark_list=handLms,
                                               landmark_drawing_spec=dotSpec)
                if showDotConn:
                    dotSpec = self.mpDraw.DrawingSpec(color=self.dotColor, circle_radius=self.dotRadius)
                    connSpec = self.mpDraw.DrawingSpec(color=self.connColor, thickness=self.connThick)
                    self.mpDraw.draw_landmarks(self.img,
                                               landmark_list=handLms,
                                               landmark_drawing_spec=dotSpec,
                                               connections=self.mpHands.HAND_CONNECTIONS,
                                               connection_drawing_spec=connSpec)

    def findAllPositions(self, handNo):
        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id_, lm in enumerate(myHand.landmark):
                cx, cy = int(lm.x * self.width), int(lm.y * self.height)
                lmList.append([id_, cx, cy])
        return lmList

    def findPosition(self, handNo, pointNo, draw=False, color=(0, 0, 0), radius=10):
        positions = self.findAllPositions(handNo)

        if len(positions) != 0:
            position = positions[pointNo]
            x = position[1]
            y = position[2]
            if draw:
                cv2.circle(self.img, (x, y), radius, color, cv2.FILLED)
            return [x, y]

    def propDots(self, color, radius):
        self.dotColor = color
        self.dotRadius = radius

    def propConn(self, color, thick):
        self.connColor = color
        self.connThick = thick

    def handShown(self): # Show number of hands shown
        if self.results.multi_hand_landmarks:
            return len(self.results.multi_hand_landmarks)


def main():
    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)

        # From the class
        detector = HandDetector(img=img, maxHand=2)
        detector.propDots(color=(255, 100, 50), radius=10)
        detector.propConn(color=(150, 200, 255), thick=5)
        detector.findHand()
        position = detector.findPosition(handNo=0, pointNo=8, draw=True)
        print(position)
        print("Number of hands showing: ", detector.handShown())
        # End

        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    main()
