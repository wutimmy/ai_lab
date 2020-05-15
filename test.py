with open("config.ini",mode="r") as f:
        a = f.readline()
        a = a.split("=")[1]
        a = a.replace("/n","")
        a = a.replace("/t","")
        a = int(a)
