import database as db
import buy
import cart
class gvar:
    id = 0 
class Customer(gvar):
    def customer():
        while True:
            print('1.Signup\n2.Login\n3.Exit')
            try:
                n=int(input())
                a = Customer()
                if n==1:
                    a.signup()
                elif n==2:
                    a.login()
                elif n==3:
                    break
                else:
                    print("invalid input :(")
                
            except:
                print("invalid input from customer!")
        
    def signup(self):
        id = int(input('Enter id:'))
        name = input('Enter name:')
        name = name.lower()
        city = input('Enter city:')
        city = city.lower()
        psw  = input('Enter password:')
        psw = psw.lower()
        contact = int(input('Enter contact no:'))
        l=[]
        l.append(id)
        l.append(name)
        l.append(city)
        l.append(psw)
        l.append(contact)
        val=tuple(l)
        try:
            sql = "INSERT INTO customers(id,name,city,password,contact) VALUES(%s,%s,%s,%s,%s)"
            db.mycursor.execute(sql,val)
            print("Signed Up Successfully!")
            db.mydb.commit()

        except:
            print("Id Already registered. Try another id!")
            
    def login(self):
       sql = "SELECT id,password,name from customers"
       db.mycursor.execute(sql)
       r = db.mycursor.fetchall()
       lid = int(input('Enter your Id:'))
       gvar.id = lid
       lpsw = input("Enter your Password:")
       f=False
       for i in r:
            id,psw,name= i 
            if lid == id and lpsw == psw:
                f=True
                break
       if f:
           print("Welcome,",name)
           while True:
               print('1.Buy Products\n2.Your cart\n3.Track Orders\n4.Logout')
               try:
                   n=int(input())
                   if n==1:
                       print('Welcome to Azar foods \u00a9')
                       while True:
                           print('1.Dairy products\n2.Cakes\n3.Ice creams\n4.Cookies\n5.Exit')
                           c = int(input())
                           try:
                                if c==1:
                                    buy.Buy.dairy()
                                elif c==2:
                                    buy.Buy.cake()
                                elif c==3:
                                    buy.Buy.ice() 
                                elif c==4:
                                    buy.Buy.cookie() 
                                elif c==5:
                                    break
                                else:
                                    print("input mismatched!")
                           except:
                               print("Something error in your input!") 
                           

                   elif n==2:
                       cart.Cart.view_cart()
                   elif n==3:
                        try:
                            q = f"SELECT * from orders WHERE cust_id='{gvar.id}'"
                            db.mycursor.execute(q)
                            r = db.mycursor.fetchall()
                            if r[0][-1]=='true':
                                    print('Your order will be dispatched after 2 days :) ')
                            elif r[0][-1]=='false':
                                print("Your order under checking...")
                            else:
                                print("You didn't order aything:)")
                        except:
                            print("Error in Track orders!")
                   elif n==4:
                       break
                   else:
                       print('input mismatched!')
               except:
                   print("something wrong in your input!")
                   
       else:
           print("Account not found!")
        
           
           