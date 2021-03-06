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
        with open(base_user_path + "\\{}\\info.txt".format(username), "r") as f:
            data = f.readlines()
            data[0] = data[0].replace("\n", "")
            return data
    except:
        return None


def send_user_mail(base_user_path, username=str):
    try:
        with open(base_user_path + "\\{}\\info.txt".format(username), "r") as f:
            data = f.readlines()
            data[0] = data[0].replace("\n", "")
            print(data)
            if get_user_status(username):
                send_mail(receiver_email=str(data[0]), username=str(username),
                          message="{} has went in to the lab.".format(username))
            elif not get_user_status(username):
                send_mail(receiver_email=str(data[1]), username=str(username),
                          message="{} has went out of the lab.".format(username))
    except:
        pass


def get_user_status(username):
    status = int()
    conn = sqlite3.connect("users.sqlite3")
    cursor = conn.execute("select status from users where name='{}' ".format(str(username)))
    for i in cursor:
        status = int(i[0])
    conn.close()
    return bool(status)


def update_user_status(base_user_path, username):
    print(usr_time)
    new = []
    status = dict()
    conn = sqlite3.connect("users.sqlite3")
    cursor = conn.cursor()
    data = cursor.execute("select * from users")
    for i in data:
        print("usr_time:{}".format(usr_time))
        i = list(i)
        status[i[0]] = bool(i[1])
    if username not in list(status.keys()):
        status[username] = int(True)
        # sql = "SELECT in-time from Users WHERE Name='{}'".format(username)
        # data = conn.execute(sql)
        sql = "insert into users values('{}',{},'{}','{}');".format(username, int(status[username]), str(datetime.datetime.now()), "null")
        print(sql)
        conn.execute(sql)
        new.append(username)
        # usr_time[username][str(datetime.datetime.now()), str(datetime.datetime.now())] 
        # usr_time.update({username:})
        # t = {str(username):[str(datetime.datetime.now()), str(datetime.datetime.now())]}
        # usr_time.update(t)

        new.append(username)
        conn.commit()
    elif username in status and status[username]:
        status[username] = False
        # tmp = usr_time[username][0]
        sql = 'SELECT "In" from Users WHERE Name="{}"'.format(username)
        print(sql)
        data = conn.execute(sql)
        for i in data:
            tmp = i[0]
        print(tmp)
        conn.commit()
        sql = 'update users set Name="{}",status="{}", "In"="{}","Out"="{}";'.format(username, int(status[username]),str(tmp),str(datetime.datetime.now()) )
        # print(sql)
        print(sql)
        conn.execute(sql)
        conn.commit()
    elif username in status and not status[username]:
        status[username] = True
        # tmp = usr_time[username][1]
        sql = 'SELECT "Out" from Users WHERE Name="{}"'.format(username)
        data = conn.execute(sql)
        for i in data:
            tmp = i[0]
        # usr_time[username] = [str(datetime.datetime.now()), str(tmp)]
        sql = 'update users set Name="{}",status="{}", "In"="{}","Out"="{}";'.format(username, int(status[username]),str(datetime.datetime.now()),str(tmp))
        print(sql)
        conn.execute(sql)
        conn.commit()
    send_user_mail(base_user_path, username)
    # for name in status.keys():
    #     if name in new:
    #         sql = "insert into users values('{}',{},{},{});".format(name, int(status[name]), "null", "null")
    #         print(sql)
    #         conn.execute(sql)
    #     else:
    #         conn.execute("update users set status={} where Name='{}';".format(int(status[name]), str(name)))
    #     try:
    #         send_mail(receiver_email=get_user_info(base_user_path, username)[0],
    #                   message="Your record have recorded successfully, enjoy your work !")
    #     except:
    #         pass
    conn.close()
