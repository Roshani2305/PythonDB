import mysql.connector as mycon

con=mycon.connect(host='localhost',user='root',password='roshani1306',database='bookstoredb')
curs=con.cursor()

curs.execute("select * from books")

while True:
    data=curs.fetchmany(12)
    if not data:
        break
    print(data)
    print('-'*40)



con.close()
