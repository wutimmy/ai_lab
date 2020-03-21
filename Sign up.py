import cv2
import FaceRecognizer
import random
import os
from tkinter import messagebox

c = cv2.VideoCapture(-1)

font = cv2.FONT_HERSHEY_SIMPLEX

# org
org = (50, 50)

# fontScale
fontScale = 1

# Blue color in BGR
color = (255, 0, 0)

# Line thickness of 2 px
thickness = 2

success,_ = c.read()

if not success:
    print("Fail to turn on camera")
    exit(-1)



if not os.path.exists(user_path):
    os.mkdir(user_path)

username = "Person_{}".format(input("Please enter username for new user, leave blank to use random numbers , then press enter : "))

if len(username) == 0:
    username = "Person_{}".format(random.randint(1,10000))

user_profile_path = user_path + "/{}".format(username)
try:
    os.mkdir(user_profile_path)
except:
    username = "Person_{}".format(random.randint(1, 10000))
    user_profile_path = user_path + "/{}".format(username)
    os.mkdir(user_profile_path)

# os.mkdir(user_path)


count = 0

dc = FaceRecognizer.FaceRecognizer()

user_path = os.getcwd() + "/user"

while c.isOpened():
    
    success, frame = c.read()
    
    if not success:
        break
        
    frame = cv2.putText(frame, "Press Space bar when you are ready.",(25,25),font,fontScale, color,thickness,cv2.LINE_AA)
    frame = cv2.putText(frame, "Captured {} of 4 photos.".format(count), org, font, fontScale, color, thickness,
                        cv2.LINE_AA)

    cv2.imshow("test",frame)

    key = cv2.waitKey(13)

    if key in [27,ord("q")]:
        break
    elif key == 32:
        filename = "{}.jpg".format(random.randint(1, 100000))
        if count > 4:
            cv2.destroyAllWindows()
            c.release()
            dc.calc_128D_by_path(user_path)
            with open(user_profile_path+"/email.txt",mode="w+") as f:
                pass
            with open(user_profile_path+"/email.txt",mode="w") as f:
                ans = input("Please enter parent's email (key in '-1' to finnish signup process.)")
                while ans != "-1":
                    ans = input("Please enter parent's email (key in '-1' to finnish signup process.) :")
                    print(ans)
                    if ans == "-1" or len(ans) < 10 or "@" not in ans:
                        continue
                    f.write(ans+"\n")
                messagebox.showinfo("Success", "You have successfully regerted !")


        elif count <= 4:
            filename = "{}.jpg".format(random.randint(1, 100000))
            try:
                cv2.imwrite(user_profile_path+"/{}".format(filename),frame)
            except:
                filename = "{}.jpg".format(random.randint(1, 100000))
                cv2.imwrite(user_profile_path + "/{}".format(filename),frame)
            count += 1

