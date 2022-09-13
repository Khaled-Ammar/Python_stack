class User :
    def __init__ (self,name,email,balnce):
        self.name=name 
        self.email=email 
        self.balnce=balnce

    def make_withdrawal(self,amount):
        self.balnce-=amount
    def make_deposits(self,amount1):
        self.balnce+=amount1
    def display_user_balance(self):
        print("name",self.name,"email",self.email,"balance",self.balnce)

user1=User("khaled","kh@jsdld.com",900)
user2=User("yosef","ya@jsdld.com",1900)
user3=User("ahmad","ah@jsdld.com",3900)

user1.make_deposits(100)
user1.make_deposits(20)
user1.make_deposits(44)
user1.make_withdrawal(100)
user1.display_user_balance()
user2.make_deposits(20)
user2.make_deposits(44)
user2.make_withdrawal(20)
user2.make_withdrawal(20)
user2.display_user_balance()

user3.make_deposits(100)
user3.make_withdrawal(20)
user3.make_withdrawal(20)
user3.make_withdrawal(40)
user3.display_user_balance()