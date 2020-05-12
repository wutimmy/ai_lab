import _sqlite3
conn = _sqlite3.connect("users.sqlite3")
cursor = conn.cursor()
data = cursor.execute("select * from users")
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
name = str(input("name : "))
data = conn.execute("select status from users where name='{}' ".format(name))
print(data[0])
conn.commit()
conn.close()
