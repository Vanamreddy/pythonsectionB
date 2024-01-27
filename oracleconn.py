import cx_Oracle
import csv
conn=cx_Oracle.Connection('system/manager@mother')
cur=conn.cursor()

def createtable():
    query='''create table mohanmca(
    id number(2) primary key,
    name varchar(50)
    )
    '''
    cur.execute(query)
def insertrecord(sid,name):
    record={'id':str(sid),'name':name}
    cur.execute("insert into mohanmca(id,name) values(:id,:name)",record)
    conn.commit()
#insertrecord(2,'einstein')
#insertrecord(3,'nielsbohr')
#insertrecord(4,'thomas')
#insertrecord(5,'edison')

def read_records():
    query='select*from mohanmca'
    cur.execute(query)
    record=cur.fetchall()
    for row in record:
        print(row)
   # with open('records.csv','w',newline='') as csvfile:
    #    data=csv.writer(csvfile)git remote add origin https://github.com/Mohanreddy321/sqlconn.git
     #   data.writerow(['id','name'])
      #  for row in records:
       #     data.writerow(row)
#read_records()
        
def fetch_records(sid):
    record={'id':str(sid)}
    query='select*from mohanmca where id=:id'
    cur.execute(query,record)
    record=cur.fetchall()
    for row in record:
        print(row)
 
def update_name(sid):
    fetch_records(sid)
    name=input('enter new name to update:- ')
    record={'id':str(sid),'name':name}
    query='update mohanmca set name=:name where id=:id'
    cur.execute(query,record)
    conn.commit()
    fetch_records(sid)

def delete(sid):
    fetch_records(sid)
    record={'id':str(sid)}
    query='delete from mohanmca where id=:id'
    cur.execute(query,record)
    conn.commit()
    fetch_records(sid)
#delete(3)
def truncate():
    query='truncate table mohanmca'
    cur.execute(query)
#truncate()
    
def insert_from_csv():
    with open('records.csv','r') as csvfile:
        data=csv.reader(csvfile)
        #for row in data:
         #   print(row)
#insert_from_csv()
        data=list(data)
        for row in range(1,len(data)):
            insertrecord(*data[row])
insert_from_csv()