import mysql.connector as mycon

con=mycon.connect(host='localhost',user='root',password='roshani1306',database='bookstoredb')
curs=con.cursor()

try:
    bcode=int(input('Enter Book code : '))

    curs.execute("select * from books where bookcode=%d" %bcode)
    rec=curs.fetchone()

    if rec:
       
        reviews=input('Enter review comments :')

        curs.execute("update books set review='{p1}' where bookcode={p2}".format(p1=reviews,p2=bcode) )
        
        con.commit()
        print('.....REVIEW ENTERED SUCCESSFULLY....')

    else:
        print('Book does not exist')

        con.close()

except Exception as e : 
    print(e)
    print('Invalid input...')