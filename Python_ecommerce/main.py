import database as db
import admin as ad
import customer as ct
class Food:
    def __init__(self):
        while True:
            print('1.Admin\n2.Customer\n3.Exit Application')
            try:
                n = int(input())
                if n==1:
                    ad.Admin.admin()
                elif n==2:
                    ct.Customer.customer()
                elif n==3:
                    break
                else:
                    print('input mismatched!')
            except:
                print('Choose correct input !')




if __name__=='__main__':
    f= Food()
