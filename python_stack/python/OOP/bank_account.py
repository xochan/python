class BankAccount:
    def __init__(self, name, balance, interest):
        self.name = name
        self.balance = balance
        self.interest = 0.01

    def deposit(self,amount):
        self.balance += amount
        print(self.name, 'just deposit $',amount )
        print('now',self.name, 'with balance of $', self.balance,"\n","*"*30)
        return self

    def withdrawal(self,amount):
        if amount > self.balance:
            print(self.name, 'just withdraw $',amount )
            print('infufficient funds: charging a $5 fee')
            self.balance-= 5
            print('now',self.name, 'with balance of $', self.balance,"\n","*"*30)
            return self
        else: 
            self.balance -= amount
            print(self.name, 'just withdraw $',amount )
            print('Account',self.name, ': balance $', self.balance,"\n","*"*30)
            return self
    
    def display_account_info(self):
        print(self.name, ' balance is $', self.balance,"\n","*"*30)
        return self
    
    def transfer_money(self,other_user,amount):
        print('previous', self.name, 'with balance of $', self.balance)
        print('previous', other_user.name, 'with balance of $', other_user.balance)
        self.balance -= amount
        other_user.balance += amount
        print(self.name,'transfer $',amount,'to',other_user.name)
        print('now',self.name, 'with balance of $', self.balance)
        print('now',other_user.name, 'with balance of $', other_user.balance,"\n","*"*30)
        return self

    def yield_interest(self):
        if self.balance>=0:
            self.balance= self.balance*self.interest
            print('after interest rate, now',self.name, ' balance is $', self.balance,"\n","*"*30)
            return self
        else:
            print(self.name, 'is negative - balance - $',self.balance ,"\n","*"*30)
            return self


hoang = BankAccount('hoang', 15000, 0.01)
vy = BankAccount('vy', 6000, 0.01)
khoa = BankAccount('khoa', 7777, 0.01)
# hoang.display_account_info()
# vy.display_account_info()
# khoa.display_account_info()
# hoang.withdrawal(50)
# vy.deposit(300)
# hoang.transfer_money(vy,5500)
# khoa.withdrawal(1232888)
# khoa.withdrawal(1232888)
# hoang.transfer_money(khoa,3500)
# hoang.yield_interest()
# vy.yield_interest()
# khoa.yield_interest()

hoang.deposit(5).deposit(1000).deposit(500).withdrawal(590).yield_interest()
khoa.deposit(50).deposit(60).withdrawal(1000).withdrawal(1000).withdrawal(100000).withdrawal(1000000).yield_interest()