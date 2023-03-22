import database as db
class products:
    def dairy():
        n=int(input('Enter how many products you want to add:'))
        val=[]
        for i in range(n):
            t = int(input('Product id:')),input('Product name:'),int(input('Price:')),int(input('Quantity:'))
            val.append(t)
        try:
            sql ="INSERT INTO dairy(product_id,name,price,quantity) VALUES(%s,%s,%s,%s)"
            db.mycursor.executemany(sql,val)
            db.mydb.commit()
            print(db.mycursor.rowcount,'Created Successfully!')
        except:
            print("Error in dairy product creation!") 
    def cookies():
        n=int(input('Enter how many products you want to add:'))
        val=[]
        for i in range(n):
            t = int(input('Product id:')),input('Product name:'),int(input('Price:')),int(input('Quantity:'))
            val.append(t)
        try:
            sql ="INSERT INTO cookies(product_id,name,price,quantity) VALUES(%s,%s,%s,%s)"
            db.mycursor.executemany(sql,val)
            db.mydb.commit()
            print(db.mycursor.rowcount,'Created Successfully!')
        except:
            print("Error in cookie products creation!") 
    def ice_cream():
        n=int(input('Enter how many products you want to add:'))
        val=[]
        for i in range(n):
            t = int(input('Product id:')),input('Product name:'),int(input('Price:')),int(input('Quantity:'))
            val.append(t)
        try:
            sql ="INSERT INTO icecream(product_id,name,price,quantity) VALUES(%s,%s,%s,%s)"
            db.mycursor.executemany(sql,val)
            db.mydb.commit()
            print(db.mycursor.rowcount,'Created Successfully!')
        except:
            print("Error in icecream product creation!") 
    def cakes():
        n=int(input('Enter how many products you want to add:'))
        val=[]
        for i in range(n):
            t = int(input('Product id:')),input('Product name:'),int(input('Price:')),int(input('Quantity:'))
            val.append(t)
        try:
            sql ="INSERT INTO cakes(product_id,name,price,quantity) VALUES(%s,%s,%s,%s)"
            db.mycursor.executemany(sql,val)
            db.mydb.commit()
            print(db.mycursor.rowcount,'Created Successfully!')
        except:
            print("Error in cakes product creation!") 