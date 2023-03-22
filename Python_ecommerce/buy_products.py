import database as db
from datetime import date
import customer as cus
class Buyprod:
    def buyp():
        while True:
            uid = cus.gvar.id
            sql = f"SELECT * FROM cart where cust_id='{uid}'"
            db.mycursor.execute(sql)
            r=db.mycursor.fetchall()
            for i in r:
                pd,pn,pc,qt,cid=i
            try:
                y_pid = int(input('Enter product Id to buy:'))
                qry = f"SELECT name FROM cart WHERE product_id='{y_pid}'"
                db.mycursor.execute(qry)
                res = db.mycursor.fetchall()
                for i in res:
                    nam=i
                print('You choosed:',nam[0])
                y_qty = int(input('Enter Quantity:'))
                fqty = qt-y_qty
                print(f'Your Order Amount:\u20B9{pc * fqty}')
                x=input('press Y/y to continue or N/n to leave:')
                print('*** PAYMENT HERE ***')
                y_pri = int(input('Give Amount:'))
                if x=='Y' or 'y':
                    if fqty>=0:
                        if pc * fqty==y_pri:
                            # sql = f"UPDATE ORDERS SET quantity = '{fqty}' WHERE cust_id ='{cid}'" #need to work
                            name = nam[0]
                            curr_date = date.today()
                            l=[]
                            l.append(None)
                            l.append(name)
                            l.append(y_pri)
                            l.append(y_qty)
                            l.append(curr_date)
                            l.append(uid)
                            l.append('false')
                            val= tuple(l)
                            try:
                                sql = "INSERT INTO orders(order_id,product_name,product_price,quantity,ordered_date,cust_id,approval) VALUES(%s,%s,%s,%s,%s,%s,%s)"
                                db.mycursor.execute(sql,val)
                                db.mydb.commit()
                                print("Ordered Successfully!")
                                break
                            except:
                                print("Error while Signup try again:(")
                        else:
                            print("Give correct Amount!")
                    else:
                        print("Stocks less than youe need! Try Again...")
                elif x=='N' or 'n':
                    break 
                else:
                    print('Your option invalid...Please try again :)')
            except:
                print("Something error while buying products ! Try Again...")
        

