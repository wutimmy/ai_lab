import cv2
import FaceRecognizer
import os
import smtplib, ssl
import threading

status = {}

def send_mail(sender_email,sender_password,receiver_email,msg):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    message = str(msg)

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message)


def get_name(faces):
    names = list()
    for face in faces:
        if face["display_name"] == "unknown":
            continue
        else:
            names.append(face["display_name"])
    return names
def send_status(names,status):
    for name in names:
        person_status = status[str(name)]
        with open(user_path+"//"+name+"//"+"email.txt",mode="r") as f:
            txt = f.read()
            print(txt)
            txt = txt.split("\n")
            # a = []
            # for t in txt:
            #     a.append(t.)

        for adr in txt:
            if "@" not in adr:
                continue
            if person_status:
                send_mail("wutimmy01@gmail.com", "Wulokhin2006",adr,"{} has entered the lab.".format(name))
            else:
                send_mail("wutimmy01@gmail.com", "Wulokhin2006", adr, "{} has went out the lab.".format(name))

def process(faces,status):
    names = get_name(faces)
    for name in names:
        if name in status.keys():
            status[name] = False
        else:
            status[name] = True
        send_status(names,status)
    

dc = FaceRecognizer.FaceRecognizer()

user_path = os.getcwd() + "/user"
dc.load_users(user_path)

c = cv2.VideoCapture(-1)

while c.isOpened():
    success, frame = c.read()

    if not success:
        break

    color_image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    faces = dc.face_detect(color_image,multi_detect=1)
    faces = dc.recognize(color_image)
    # print(faces)

    # faces = dc.faces_shape(color_image,faces)

    frame = dc.draw_faces(frame,faces)

    # print(faces)

    cv2.imshow("Test",frame)

    print(status)

    key = cv2.waitKey(13)

    if key in [27,ord("q")]:
        break

    task = threading.Thread(target=process,args=(faces,status))
    task.start()

    while len(dc.face_detect(color_image,multi_detect=1)) != 0:
        print("waiting...")
        _,frame = c.read()
        color_image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)



c.release()
cv2.destroyAllWindows()