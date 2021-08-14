import mysql.connector as mycon

con=mycon.connect(host='localhost',user='root',password='roshani1306',database='bookstoredb')
curs=con.cursor()

bcode=int(input('Enter book code to delete : '))

curs.execute("select * from books where bookcode=%d" %bcode)
rec=curs.fetchone()

try:
    print("bookcode : %d" %rec[0])
    print("bookname : %s" %rec[1])
    print("category : %s" %rec[2])
    print("author : %s" %rec[3])
    print("publication : %s" %rec[4])
    print("edition : %d" %rec[5])
    print("price : %.2f" %rec[6])

    curs.execute("delete from books where bookcode=%d" %bcode)
    bcode=input('Do you want to delete?(yes/no) ')
    while bcode.upper()=='YES':
        print('Book deleted successfully')
        con.commit()
except:
    print('Book does not EXIST...')
    print('-'*20)

con.close()