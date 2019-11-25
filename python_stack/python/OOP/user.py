class user:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def make_deposit(self,amount):
        self.balance += amount
        print(self.name, 'just deposit',amount )
        print('now',self.name, 'with balance of', self.balance,"\n","*"*30)

    def make_withdrawal(self,amount):
        self.balance -= amount
        print(self.name, 'just withdraw',amount )
        print('now',self.name, 'with balance of', self.balance,"\n","*"*30)
    
    def display_user_balance(self):
        print(self.name, 'with balance of', self.balance,"\n","*"*30)
    
    def transfer_money(self,other_user,amount):
        print('previous', self.name, 'with balance of', self.balance)
        print('previous', other_user.name, 'with balance of', other_user.balance)
        self.balance -= amount
        other_user.balance += amount
        print(self.name,'transfer',amount,'to',other_user.name)
        print('now',self.name, 'with balance of', self.balance)
        print('now',other_user.name, 'with balance of', other_user.balance,"\n","*"*30)
hoang = user('hoang', 15000)
vy = user('vy', 6000)
khoa = user('khoa', 7777)
hoang.display_user_balance()
vy.display_user_balance()
khoa.display_user_balance()
hoang.make_withdrawal(50)
vy.make_deposit(300)
vy.make_deposit(100)
hoang.transfer_money(vy,5500)
khoa.make_deposit(4000)
khoa.make_withdrawal(400)
khoa.make_withdrawal(888)
hoang.transfer_money(khoa,3500)