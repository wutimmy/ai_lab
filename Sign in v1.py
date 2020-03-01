import cv2
import FaceRecognizer

dc = FaceRecognizer.FaceRecognizer()

c = cv2.VideoCapture(0)

while True:
    success, frame = c.read()

    if not success:
        break

    cv2.imshow("Test",frame)

    key = cv2.waitKey(13)

    if key in [27,ord("q")]:
        break

c.release()
cv2.destroyAllWindows()