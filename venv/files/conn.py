import datetime
import mysql.connector
class employee:
    def __init__(self,idd,fn,ln,sal):
        self.id=int(idd)
        self.fname=fn
        self.lname=ln
        self.salary=int(sal)

    def display(self):
        print(self.id,"    ",self.salary)

    def com(self,d):
        if(self.id==d):
            print(self.fname," salary is :",self.salary)

cnx = mysql.connector.connect(user='root',password='root1234',host='localhost',database='mydb')
cursor = cnx.cursor()

query = ("SELECT * FROM sal")
cursor.execute(query)

li=[]
for (id,fname, lname,salary) in cursor:
    g=id
    f=fname
    l=lname
    s=salary
    li.append(employee(g,f,l,s))


for j in range(1,len(li)):
    key=li[j].salary
    key1=li[j]
    i=j-1
    while(i>-1 and li[i].salary>key):
        li[i+1]=li[i]
        i=i-1
    li[i+1]=key1

for j in li:
    j.display()

d=int(input("Enter id to find salary :"))

for i in li:
    i.com(d)



cnx.commit()
cursor.close()
cnx.close()
