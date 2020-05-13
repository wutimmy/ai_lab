import cv2
import os
import func
import FaceRecognizer
from threading import Thread
from mail_test import send_mail

def hi():
    print("hi")

base_user_path=os.getcwd()+"\\user"
dc=FaceRecognizer.FaceRecognizer()
dc.load_users(os.getcwd()+"\\user")
c=cv2.VideoCapture(0)
while c.isOpened():
    s,f=c.read()
    if not s:
        break
    color_image=cv2.cvtColor(f, cv2.COLOR_BGR2RGB)
    faces=dc.face_detect(color_image)
    faces = dc.recognize(color_image,multi_detect=1)
    f=dc.draw_faces(f,faces)
    names = func.print_usr_name(faces)
    for name in names:
        thread = Thread(target = send_mail, args = ("{}".format(name), ))
        thread.start()
        # TODO : Read user info and send mail to user and user's parent
    cv2.imshow("test",f)
    key=cv2.waitKey(1)
    if key in (32,27):
        cv2.destroyAllWindows()
        c.release()
        break
