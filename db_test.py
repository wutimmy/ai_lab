import sqlite3
conn = sqlite3.connect("/home/timmyw/PycharmProjects/ai_fablab/test.sqlite3")

"""
print(conn)
cursor = conn.execute('SELECT * FROM user')
for i in cursor:
    print(i)
"""

"""
cursor = conn.execute("UPDATE user SET intime=CURRENT_TIMESTAMP WHERE name='timmy';")
conn.commit()
conn.close()
"""

'''
cursor = conn.execute('SELECT * FROM user')
print(cursor)
for i in cursor:
    for g in i:
        print("timmy" in g)
    print(i)
# print("timmy" in cursor)
'''

cursor = conn.execute("UPDATE user SET status=False WHERE name='timmy';")
conn.commit()
conn.close()

