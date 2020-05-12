import sqlite3
import datetime
usr_time = {}
def print_usr_name(faces):
    names = []
    for face in faces:
        names.append(face["display_name"])
    return names

import smtplib, ssl
port = 587  # For starttls
smtp_server = "smtp.gmail.com"

def send_mail(sender_email="codeme2006@gmail.com", receiver_email=str, message=str):
    password = "Wulokhin2006"
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

def get_user_info(base_user_path, username):
    try:
        with open(base_user_path+"\\{}\\info.txt".format(username),"r") as f:
            data = f.readlines()
            data[0] = data[0].replace("\n","")
            return data
    except:
        return None


def send_user_mail(base_user_path, username=str):
    try:
        with open(base_user_path+"\\{}\\info.txt".format(username),"r") as f:
            data = f.readlines()
            data[0] = data[0].replace("\n","")
            print(data)
            if get_user_status(username):
                send_mail(receiver_email=str(data[0]),username=str(username),message="{} has went in to the lab.".format(username))
            elif not get_user_status(username):
                send_mail(receiver_email=str(data[1]),username=str(username),message="{} has went out of the lab.".format(username))
    except:
        pass

def get_user_status(username):
    status = int()
    conn=sqlite3.connect("users.sqlite3")
    cursor=conn.execute("select status from users where name='Timmy' ".format(str(username)))
    for i in cursor:
        status=int(i[0])
    conn.close()
    return bool(status)

def update_user_status(base_user_path,username):
    print(usr_time)
    new=[]
    status={}
    conn = sqlite3.connect("users.sqlite3")
    cursor = conn.cursor()
    data = cursor.execute("select * from users")
    for i in data:
        i=list(i)
        status[i[0]]=bool(i[1])
    if username not in list(status.keys()):
        status[username]=int(True)
        usr_time.update({username:[str(datetime.datetime.now()),str(datetime.datetime.now())]}) 
        new.append(username)
    elif username in status and status[username]:
        status[username]=False
        tmp = usr_time[username]
        usr_time.update({username:[str(tmp),str(datetime.datetime.now())]})
    elif username in status and not status[username]:
        status[username]=True
        tmp = usr_time[username][1]
        usr_time.update({username:[str(datetime.datetime.now()),str(tmp)]})
    send_user_mail(base_user_path,username)
    for name in status:
        if name in new:
            sql = "insert into users values('{}',{},{},{});".format(name,int(status[name]),"null","null")
            print(sql)
            conn.execute(sql)
        else:
            conn.execute("update users set status={} where Name='{}';".format(int(status[name]),str(name)))
        try:
            send_mail(receiver_email=get_user_info(base_user_path,username)[0],message="Your record have recorded successfully, enjoy your work !")
        except:
            pass
    conn.commit()
    conn.close()
