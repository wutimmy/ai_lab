import cv2
import FaceRecognizer
import random
import os
from tkinter import messagebox

user_path = os.getcwd() + "//user"

username = "Person_{}".format(input("Please enter username for new user, leave blank to use random numbers , then press enter : "))

if len(username) == 0:
    username = "Person_{}".format(random.randint(1,10000))

user_profile_path = user_path + "//{}".format(username)
try:
    os.mkdir(user_profile_path)
except:
    username = "Person_{}".format(random.randint(1, 10000))

if not os.path.exists(user_path):
    os.mkdir(user_path)


count = 0

dc = FaceRecognizer.FaceRecognizer()

c = cv2.VideoCapture(-1)

while c.isOpened():
    
    success, frame = c.read()
    
    if not success:
        break
        
    frame = cv2.putText("Press Space bar when you are ready.")

    cv2.imshow("test",frame)

    key = cv2.waitKey(13)

    if key in [27,ord("q")]:
        break
    elif key == '32':
        filename = "{}.jpg".format(random.randint(1, 100000))
        if count > 4:
            cv2.destroyAllWindows()
            c.release()
            with open(user_profile_path+"\\email.txt",mode="w+") as f:
                pass
            with open(user_profile_path+"\\email.txt",mode="w") as f:
                ans = input("Please enter parent's email (key in '-1' to finnish signup process.)")
                while ans != "-1":
                    if ans == "-1" or len(ans) < 10 or "@" not in ans:
                        continue
                    f.write(ans+"\n")
                    ans = input("Please enter parent's email (key in '-1' to finnish signup process.)")

        elif count <= 4:
            try:
                cv2.imwrite(user_profile_path+"\\{}".format(filename))
            except:
                filename = "{}.jpg".format(random.randint(1, 100000))
                cv2.imwrite(user_profile_path + "\\{}".format(filename))
