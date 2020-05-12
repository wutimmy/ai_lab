import _sqlite3
conn = _sqlite3.connect("users.sqlite3")
cursor = conn.cursor()
data = conn.execute("select * from users")
print(data)
for i in data:
    print(i)
conn.close()

# conn = _sqlite3.connect("users.sqlite3")
# cursor = conn.cursor()
# name = str(input("name : "))
# status = int(input("status : "))
# conn.execute("update users set status={} where Name='{}'".format(status,name))
# conn.commit()
# conn.close()



conn = _sqlite3.connect("users.sqlite3")
cursor = conn.cursor()
username = str(input("name : "))
sql = "SELECT 'In' from Users WHERE Name='{}'".format(username)
data = conn.execute(sql)
for i in data:
        print(i)
conn.commit()
conn.close()
