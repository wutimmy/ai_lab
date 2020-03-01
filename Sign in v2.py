import cv2
import FaceRecognizer

dc = FaceRecognizer.FaceRecognizer()

c = cv2.VideoCapture(0)

while c.isOpened():
    success, frame = c.read()

    if not success:
        break

    color_image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    faces = dc.face_detect(color_image,multi_detect=1)

    # faces = dc.faces_shape(color_image,faces)

    frame = dc.draw_faces(frame,faces)

    # print(faces)

    cv2.imshow("Test",frame)


    key = cv2.waitKey(13)

    if key in [27,ord("q")]:
        break

c.release()
cv2.destroyAllWindows()