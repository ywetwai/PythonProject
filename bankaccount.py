class BankAccount:
    def __init__(self,owner,balance = 0.0):
        self.owner = owner
        self.balance =balance

    def deposit(self,amount):
        if amount > 0:
           self.balance += amount
           print(f"{amount} is added")
        else:
            print(f'Your amount is not defined')

    def showbalance(self):

        print(f"your balance is ${self.balance:.2f}")

    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance -=amount
            print(f'you have withdraw {amount}, your balance is ${self.balance:.2f}')
        else:
            print("Insufficent Balance")

def main():
    
    name = input("Enter your name : ")
    account = BankAccount(owner=name)
    while True:
        print("1.Show Balance\n ")
        print("2. Deposit \n")
        print("3. withdraw \n")
        print("4. Exit")
        try:
            choice = int(input("Enter the number (1.4) "))

            if choice == 1:
                account.showbalance()

            elif choice == 2:
                try:
                    amount = float(input("Enter your amount : "))
                    account.deposit(amount)
                except ValueError:
                    print("Invalid amount")

            elif choice == 3:
                try:

                    amount = float(input("Enter your amount : "))
                    account.withdraw(amount)
                except ValueError:
                    print("Invalid amount")
        
            else:
                print("Thanks You!")
                break
        except ValueError:
            print("pls enter the number (1-4)")

if __name__=='__main__':
    main()
           
               