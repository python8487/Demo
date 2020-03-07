import pymysql as py
import pandas as pd

db=py.connect(host="localhost", port=3306, user="root", passwd="mysql123", db="stu", charset="utf8")
cursor=db.cursor()

# sql="""create table phone(
#         id int not null,
#         name varchar(20),
#         phone varchar(11)
#         )"""

# sql='''insert into phone(id,name,phone)
#         values(2,"lily","13760252733")
#     '''

# sql="select * from phone "
# cursor.execute(sql)
# date1=cursor.fetchall()

sql="update phone set name='gj' where id=2"
cursor.execute(sql)
db.commit()




db.close()
