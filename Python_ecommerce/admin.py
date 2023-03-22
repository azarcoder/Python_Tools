import products as prod
import database as db
class Admin:
    def admin():
        id = input('Enter admin id:')
        psw = int(input('Enter password:'))
        if id=='azar' and psw == 123:
            while True:
                print('1.Create Products\n2.View Orders\n3.Approve orders\n4.Exit')
                try:
                    n = int(input())
                    if n==1:
                        while True:
                            print('1.Dairy\n2.Cakes\n3.Ice creams\n4.Cookies\n5.Exit')
                            try:
                                x=int(input())
                                if x==1:
                                    prod.products.dairy()
                                elif x==2:
                                    prod.products.cakes()
                                elif x==3:
                                    prod.products.ice_cream()
                                elif x==4:
                                    prod.products.cookies() 
                                elif x==5:
                                    break
                                else:
                                    print("Invalid input!")
                            except:
                                print("Error in product option!") 
                    #view orders
                    elif n==2:
                        sql = "SELECT * FROM orders"
                        db.mycursor.execute(sql)
                        r=db.mycursor.fetchall()
                        for i in r:
                            oid,pnm,prc,quan,odt,cid,app = i
                            print(f'Order id:{oid}\tProduct name:{pnm}\tProduct price:{prc}\tQuantity:{quan}\torder Date:{odt}\tcustomer id:{cid}\tApproval:{app}')
                         
                    #approve orders
                    elif n==3:
                        try:
                            sql = "UPDATE orders SET approval='true'"
                            db.mycursor.execute(sql)
                            db.mydb.commit()
                            print("All orders approved successfully!") 
                        except:
                            print("something went wrong in approval!")
                    elif n==4:
                        break 
                    else:
                        print('mismatch input from admin')
                except:
                    print('Something error in admin!')
        else:
            print("Id or Password mismatched!")