import mysql.connector as mycon

con=mycon.connect(host='localhost',user='root',password='roshani1306',database='bookstoredb')
curs=con.cursor()

bcode=int(input('Enter bookcode '))

curs.execute("select bookname,category,author,publication,edition,price from books where bookcode=%d" %bcode)
# curs.execute("select * from books where bookcode=%d" %bcode)

rec=curs.fetchone()
print(rec)

try:
    print("Book Name : %s" %rec[0])
    print("Category : %s" %rec[1])
    print("Author :%s" %rec[2])
    print("Publication :%s" %rec[3])
    print("Edition :%d" %rec[4])
    print("price : %.2f" %rec[5])
except:
    print('Book Not found.....')

con.close()