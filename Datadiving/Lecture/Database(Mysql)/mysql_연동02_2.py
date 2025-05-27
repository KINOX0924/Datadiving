from mysql_연동02 import Database

db = Database()
sql = "select * from tb_member"
rows = db.executeAll(sql)

for row in rows :
    print(row)

db.close()