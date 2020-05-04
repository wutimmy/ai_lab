import cv2
import FaceRecognizer
dc=FaceRecognizer.FaceRecognizer()
c=cv2.VideoCapture(-1)
while c.isOpened():
    s,f=c.read()
    if not s:
        break
    color_image=cv2.cvtColor(f, cv2.COLOR_BGR2RGB)
    faces=dc.face_detect(color_image)
    f=dc.draw_faces(f,faces)
    cv2.imshow("test",f)
    key=cv2.waitKey(13)
    if key in (32,27):
        cv2.destroyAllWindows()
        c.release()
        break