import database as db
import customer as cus
class Buy:
    def dairy():
        sql = 'select * from dairy'
        db.mycursor.execute(sql)
        r = db.mycursor.fetchall()
        for i in r:
            pid,name,price,available =i 
            print(f'Product id:{pid}\tName:{name}\tPrice:\u20B9{price}\tAvailabe count:{available}') 
        while True:
            print('1.Add to your cart\n2.Exit')
            try:
                n = int(input())
                if n==1:
                    uid = cus.gvar.id
                    pid = int(input('Enter product id:'))
                    pdata = f"SELECT * FROM dairy WHERE product_id='{pid}'" 
                    db.mycursor.execute(pdata)
                    r = db.mycursor.fetchall()
                    for i in r:
                        prod_id,nm,pc,qty=i
                    val=[]
                    val.append(prod_id)
                    val.append(nm)
                    val.append(pc)
                    val.append(qty)
                    val.append(uid)
                    val=tuple(val)
                    sql ="INSERT INTO cart(product_id,name,price,quantity,cust_id) VALUES(%s,%s,%s,%s,%s)"
                    db.mycursor.execute(sql,val)
                    db.mydb.commit()
                    print('Product Added in your Cart :)')
                elif n==2: 
                    break
                else:
                    print("inavlid input!")
            except:
                print("input mismatched!")
    def cookie():
        sql = 'select * from cookies'
        db.mycursor.execute(sql)
        r = db.mycursor.fetchall()
        for i in r:
            pid,name,price,available =i 
            print(f'Product id:{pid}\tName:{name}\tPrice:\u20B9{price}\tAvailabe count:{available}') 
        while True:
            print('1.Add to your cart\n2.Exit')
            try:
                n = int(input())
                if n==1:
                    uid = cus.gvar.id
                    pid = int(input('Enter product id:'))
                    pdata = f"SELECT * FROM cookies WHERE product_id='{pid}'" 
                    db.mycursor.execute(pdata)
                    r = db.mycursor.fetchall()
                    for i in r:
                        prod_id,nm,pc,qty=i
                    val=[]
                    val.append(prod_id)
                    val.append(nm)
                    val.append(pc)
                    val.append(qty)
                    val.append(uid)
                    val=tuple(val)
                    sql ="INSERT INTO cart(product_id,name,price,quantity,cust_id) VALUES(%s,%s,%s,%s,%s)"
                    db.mycursor.execute(sql,val)
                    db.mydb.commit()
                    print('Product Added in your Cart :)')
                elif n==2: 
                    break
                else:
                    print("inavlid input!")
            except:
                print("input mismatched!")
    def cake():
        sql = 'select * from cakes'
        db.mycursor.execute(sql)
        r = db.mycursor.fetchall()
        for i in r:
            pid,name,price,available =i 
            print(f'Product id:{pid}\tName:{name}\tPrice:\u20B9{price}\tAvailabe count:{available}') 
        while True:
            print('1.Add to your cart\n2.Exit')
            try:
                n = int(input())
                if n==1:
                    uid = cus.gvar.id
                    pid = int(input('Enter product id:'))
                    pdata = f"SELECT * FROM cakes WHERE product_id='{pid}'" 
                    db.mycursor.execute(pdata)
                    r = db.mycursor.fetchall()
                    for i in r:
                        prod_id,nm,pc,qty=i
                    val=[]
                    val.append(prod_id)
                    val.append(nm)
                    val.append(pc)
                    val.append(qty)
                    val.append(uid)
                    val=tuple(val)
                    sql ="INSERT INTO cart(product_id,name,price,quantity,cust_id) VALUES(%s,%s,%s,%s,%s)"
                    db.mycursor.execute(sql,val)
                    db.mydb.commit()
                    print('Product Added in your Cart :)')
                elif n==2: 
                    break
                else:
                    print("inavlid input!")
            except:
                print("input mismatched!")
    def ice():
        sql = 'select * from icecream'
        db.mycursor.execute(sql)
        r = db.mycursor.fetchall()
        for i in r:
            pid,name,price,available =i 
            print(f'Product id:{pid}\tName:{name}\tPrice:\u20B9{price}\tAvailabe count:{available}') 
        while True:
            print('1.Add to your cart\n2.Exit')
            try:
                n = int(input())
                if n==1:
                    uid = cus.gvar.id
                    pid = int(input('Enter product id:'))
                    pdata = f"SELECT * FROM icecream WHERE product_id='{pid}'" 
                    db.mycursor.execute(pdata)
                    r = db.mycursor.fetchall()
                    for i in r:
                        prod_id,nm,pc,qty=i
                    val=[]
                    val.append(prod_id)
                    val.append(nm)
                    val.append(pc)
                    val.append(qty)
                    val.append(uid)
                    val=tuple(val)
                    sql ="INSERT INTO cart(product_id,name,price,quantity,cust_id) VALUES(%s,%s,%s,%s,%s)"
                    db.mycursor.execute(sql,val)
                    db.mydb.commit()
                    print('Product Added in your Cart :)')
                elif n==2: 
                    break
                else:
                    print("inavlid input!")
            except:
                print("input mismatched!")
