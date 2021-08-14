import mysql.connector as mycon

con=mycon.connect(host='localhost',user='root',password='roshani1306',database='bookstoredb')
curs=con.cursor()

aut=input('Enter author name : ')
curs.execute("select * from books where author='%s'" %(aut))
rec=curs.fetchone()

public=(input('Enter publication name : '))
curs.execute("select * from books where publication= '%s'"%(public))
rec=curs.fetchone()

print('List of book is :')

if rec :
    print("Book Name : %s" %rec[1])
    print("Category : %s" %rec[2])
    print("Edition :%d" %rec[5])
    print("price : %.2f" %rec[6])
else :
    print('Author and Publication Name does not EXIST..')


    
con.close()    
