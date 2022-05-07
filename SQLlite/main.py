import sqlite3

'''
db = sqlite3.connect('ineuron.db')
c = db.cursor() #cursor object
#c.execute('create table fsds(name text , batchid int, marks real)')
c.execute("Insert into fsds values('sudh',123,267)")
c.execute("Insert into fsds values('sudh',123,267)")
c.execute("Insert into fsds values('sudh',123,267)")
c.execute("Insert into fsds values('sudh',123,267)")
c.execute("Insert into fsds values('sudh',123,267)")
c.execute("Insert into fsds values('sudh',123,267)")



#data=c.execute('Select * from fsds')
#for i in data :
#    print(i)

data = c.execute('select * from fsds where marks >100')
for i in data:
    print(i)
    
c.execute('drop table fsds')
db.commit()
db.close()

'''


db1 = sqlite3.connect('jobdb.db')
c1=db1.cursor()
#c1.execute('create table table1(student_id int, student_name text, mailid text, marks int)')
#c1.execute('create table table2(student_id int, pincode int , location text, nearby text, phone_no int)')


c1.execute("insert into table1 values(234,'sarvjeet' , 'sjitbh121993@gmail.com', 300)")
c1.execute("insert into table1 values(235,'sarvjeet' , 'sjitbh121993@gmail.com', 300)")
c1.execute("insert into table1 values(236,'sarvjeet' , 'sjitbh121993@gmail.com', 300)")
c1.execute("insert into table1 values(237,'sarvjeet' , 'sjitbh121993@gmail.com', 300)")
c1.execute("insert into table1 values(238,'sarvjeet' , 'sjitbh121993@gmail.com', 300)")
c1.execute("insert into table1 values(239,'sarvjeet' , 'sjitbh121993@gmail.com', 300)")
c1.execute("insert into table1 values(240,'sarvjeet' , 'sjitbh121993@gmail.com', 300)")


c1.execute("insert into table2 values(234, 4567, 'begusarai', 'masjid',7789384)")
c1.execute("insert into table2 values(237, 4567, 'begusarai', 'masjid',7789384)")
c1.execute("insert into table2 values(240, 4567, 'begusarai', 'masjid',7789384)")
c1.execute("insert into table2 values(242, 4567, 'begusarai', 'masjid',7789384)")
c1.execute("insert into table2 values(238, 4567, 'begusarai', 'masjid',7789384)")
c1.execute("insert into table2 values(245, 4567, 'begusarai', 'masjid',7789384)")
c1.execute("insert into table2 values(290, 4567, 'begusarai', 'masjid',7789384)")


data=c1.execute("select * from table1 t1 left join table2 t2 on t1.student_id = t2.student_id where t1.student_id >235 and  t1.student_id is not null")
#data=c1.execute("select * from table1 t1 left join table2 t2 on t1.student_id = t2.student_id where t1.student_id is not null
for i in data:
    print(i)

c1.execute('update table1 set student_id = 1000 where student_id = 240')

data = c1.execute('select * from table1')
for i in data:
    print(i)
