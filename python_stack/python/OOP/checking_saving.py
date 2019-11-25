# class BankAccount:
#     def __init__(self, balance, interest):
#         self.balance = balance
#         self.interest = interest

class CheckingAccount:
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

class SavingAccount:
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

class user:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.checking = CheckingAccount(balance=0,interest=0.02)
        self.saving = SavingAccount(balance=0, interest=1)
        # if x == 'checking':
        #     self.account = CheckingAccount(balance=0,interest=0.02)
        # if x == 'saving':

    def deposit(self,amount,x):
        if x == "checking":
            print('checking')
            self.checking.balance += amount
            print(self.name, 'just deposit $',amount )
            print('now',self.name, 'with balance of $', self.checking.balance,"\n","*"*30)
            return self
        if x == "saving":
            print('saving')
            self.saving.balance += amount
            print(self.name, 'just deposit $',amount )
            print('now',self.name, 'with balance of $', self.saving.balance,"\n","*"*30)
            return self

    def withdrawal(self,amount,x):
        if x == "checking":
            print('checking')
            if amount > self.checking.balance:
                print(self.name, 'just withdraw $',amount )
                print('infufficient funds: charging a $5 fee')
                self.checking.balance-= 5
                print('now',self.name, 'with balance of $', self.checking.balance,"\n","*"*30)
                return self
            else: 
                self.checking.balance -= amount
                print(self.name, 'just withdraw $',amount )
                print('Account',self.name, ': balance $', self.checking.balance,"\n","*"*30)
                return self
        if x == "saving":
            print('saving')
            if amount > self.saving.balance:
                print(self.name, 'just withdraw $',amount )
                print('infufficient funds: charging a $5 fee')
                self.saving.balance-= 5
                print('now',self.name, 'with balance of $', self.saving.balance,"\n","*"*30)
                return self
            else: 
                self.saving.balance -= amount
                print(self.name, 'just withdraw $',amount )
                print('Account',self.name, ': balance $', self.saving.balance,"\n","*"*30)
                return self
    
    def display_account_info(self,x):
        if x == "checking":
            print('checking')
            print(self.name, ' balance is $', self.checking.balance,"\n","*"*30)
            return self
        if x == "saving":
            print('saving')
            print(self.name, ' balance is $', self.saving.balance,"\n","*"*30)
            return self
    
    def transfer_money(self,other_user,amount,x):
        if x == "checking":
            print('previous', self.name, 'with balance of $', self.checking.balance)
            print('previous', other_user.name, 'with balance of $', other_user.checking.balance)
            self.checking.balance -= amount
            other_user.checking.balance += amount
            print(self.name,'transfer $',amount,'to',other_user.name)
            print('now',self.name, 'with balance of $', self.checking.balance)
            print('now',other_user.name, 'with balance of $', other_user.checking.balance,"\n","*"*30)
            return self
        if x == "saving":
            print('saving')
            print('previous', self.name, 'with balance of $', self.saving.balance)
            print('previous', other_user.name, 'with balance of $', other_user.saving.balance)
            self.saving.balance -= amount
            other_user.saving.balance += amount
            print(self.name,'transfer $',amount,'to',other_user.name)
            print('now',self.name, 'with balance of $', self.saving.balance)
            print('now',other_user.name, 'with balance of $', other_user.saving.balance,"\n","*"*30)
            return self


    def yield_interest(self,x):
        if x == "checking":
            print('checking')
            if self.checking.balance>=0:
                self.checking.balance= self.checking.balance*self.checking.interest
                print('after interest rate, now',self.name, ' balance is $', self.checking.balance,"\n","*"*30)
                return self
            else:
                print(self.name, 'is negative - balance - $',self.checking.balance ,"\n","*"*30)
                return self
        if x == "saving":
            print('saving')
            if self.saving.balance>=0:
                self.saving.balance= self.saving.balance*self.saving.interest
                print('after interest rate, now',self.name, ' balance is $', self.saving.balance,"\n","*"*30)
                return self
            else:
                print(self.name, 'is negative - balance - $',self.saving.balance ,"\n","*"*30)
                return self

hoang = user('hoang', 'abc@gmail.com')
vy = user('vy','abc@gmail.com')
khoa = user('khoa','abc@gmail.com')
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

hoang.deposit(5,'checking').deposit(1000,'checking').deposit(500,'checking').withdrawal(590,'checking').yield_interest('checking')
khoa.deposit(50,'checking').deposit(60,'checking').withdrawal(1000,'checking').withdrawal(1000,'checking').withdrawal(100000,'checking').withdrawal(1000000,'checking').yield_interest('checking')
hoang.display_account_info('checking')
khoa.display_account_info('checking')
hoang.display_account_info('saving')
khoa.display_account_info('saving')
khoa.deposit(5000,'saving').yield_interest('saving')
khoa.deposit(1000,'saving').yield_interest('saving')