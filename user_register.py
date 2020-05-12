import cv2
import FaceRecognizer
import random
import os

user_path = ""

dc=FaceRecognizer.FaceRecognizer()
c=cv2.VideoCapture(0)
base_user_path = os.getcwd()+"/user"
count = 0

print(base_user_path)

a = os.path.exists(base_user_path)


if not a:
    print("base_user_path exists : {}".format(a))
    os.mkdir(base_user_path)

def gen_user_photo():
    global user_path
    print(user_path)
    n=random.randint(0,1000)
    cv2.imwrite(user_path+"\{}.jpg".format(n),f)

def create_user_folder():
    global user_path
    n=random.randint(0,1000)
    user_name = "Person_{}".format(n)
    global base_user_path
    user_path = base_user_path+"/{}".format(user_name)
    if os.path.exists(user_path):
        return
    try:
        os.mkdir(user_path)
    except:
        create_user_folder()
    return (os.path.exists(user_path),user_name)


username = create_user_folder()[1]


while count != 4:
    s,f=c.read()
    if not s:
        c.release()
        break
    # cv2.putText()
    cv2.imshow("Press Space Bar to continue, captured {} of 4 photos".format(count),f)
    key=cv2.waitKey(13)
    if key==27:
        break
    elif key== 32:
        if len(dc.face_detect(cv2.cvtColor(f,cv2.COLOR_BGR2RGB),multi_detect=0)) == 0:
            continue
        try:
            gen_user_photo()
        except:
            gen_user_photo()
        count += 1
        cv2.destroyAllWindows()
    else:
        pass
std_email = ""
prt_email = ""
while True:
    std_email = str(input("Please enter student's email : "))
    if "@gmail.com" not in std_email[-10:]:
        print("We only support personal gmail account and please enter your email correctly !")
    else:
        break
while True:
    prt_email = str(input("Please enter parent's email : "))
    if prt_email == std_email or "@gmail.com" not in prt_email[-10:]:
        print("We only support personal gmail account \nand Parent's email must not be same as student's email !")
        print("Besides, please enter your email correctly !")
    elif prt_email != std_email and "@gmail.com" in prt_email:
        break
with open(user_path+"\\info.txt",mode="w+") as f:
    f.write(str(std_email) + "\n" + str(prt_email))
dc.calc_128D_by_path(user_path ,export=True)
cv2.destroyAllWindows()
c.release()

print("You have registered successfully and your name in this system is '{}'.\n Thank you for using our system !".format(username ))
print("A kind reminding to you, please ensure the setting 'Less secure apps' of the gmail accounts are enabled (which you can enable in https://myaccount.google.com/lesssecureapps?pli=1.),/n otherwise you will not recive our gmails, Thank you !")
