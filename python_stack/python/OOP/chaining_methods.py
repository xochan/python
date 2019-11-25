class user:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def make_deposit(self,amount):
        self.balance += amount
        print(self.name, 'just deposit',amount )
        print('now',self.name, 'with balance of', self.balance,"\n","*"*30)
        return self

    def make_withdrawal(self,amount):
        self.balance -= amount
        print(self.name, 'just withdraw',amount )
        print('now',self.name, 'with balance of', self.balance,"\n","*"*30)
        return self
    
    def display_user_balance(self):
        print(self.name, 'with balance of', self.balance,"\n","*"*30)
        return self
    
    def transfer_money(self,other_user,amount):
        print('previous', self.name, 'with balance of', self.balance)
        print('previous', other_user.name, 'with balance of', other_user.balance)
        self.balance -= amount
        other_user.balance += amount
        print(self.name,'transfer',amount,'to',other_user.name)
        print('now',self.name, 'with balance of', self.balance)
        print('now',other_user.name, 'with balance of', other_user.balance,"\n","*"*30)
        return self
hoang = user('hoang', 15000)
vy = user('vy', 6000)
khoa = user('khoa', 7777)
hoang.display_user_balance().make_withdrawal(50).transfer_money(vy,5500).transfer_money(khoa,3500)
vy.display_user_balance().make_deposit(300).make_deposit(100)
khoa.display_user_balance().make_deposit(4000).make_withdrawal(400).make_withdrawal(888)




