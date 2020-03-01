import cv2
import FaceRecognizer

dc = FaceRecognizer.FaceRecognizer()

c = cv2.VideoCapture(0)

while c.isOpened():
    
    success, frame = c.read()
    
    if not success:
        break
        
    frame = cv2.putText("Press Space bar when you are ready.")

    cv2.imshow("test",frame)

    key = cv2.waitKey(13)

    if key in [32,ord("q")]:
        break