import mysql.connector as mycon

con=mycon.connect(host='localhost',user='root',password='roshani1306',database='bookstoredb')
curs=con.cursor()


code=int(input('Enter bookcode '))
nm=input('Enter bookname')
cat=input('Enter category ')
aut=input('Enter author')
public=input('Enter publication')
ed=input('Enter edition')
cost=float(input('Enter price '))

curs.execute("insert into books values(%d,'%s','%s','%s','%s','%d',%.2f)" %(code,nm,cat,aut,public,ed,float))
con.commit()
print('.....New Book inserted Successfully....') 

con.close()
