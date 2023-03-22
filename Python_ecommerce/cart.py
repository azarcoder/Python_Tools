import customer as cus
import database as db
import buy_products as bbuy
class Cart:
    def view_cart():
        uid = cus.gvar.id
        sql = f"SELECT * FROM cart where cust_id='{uid}'"
        db.mycursor.execute(sql)
        r=db.mycursor.fetchall()
        if len(r)>0:
            for i in r:
                pd,pn,pc,qt,cid=i
                print(f'Product id:{pd}\tProduct Name:{pn}\tProduct Price:{pc}\tAvailable stock:{qt}')
            while True:
                print('1.Buy Products in your cart\n2.Remove products in your cart\n3.Exit')
                try:
                    ch = int(input())
                    if ch==1:
                        bbuy.Buyprod.buyp()
                    elif ch==2:
                        pass
                    elif ch==3:
                        break
                    else:
                        print("Invalid input choice!")
                except:
                    print('Wrong input choice!')
        else:
            print('Your cart is Empty! Buy products Now :)')
        
