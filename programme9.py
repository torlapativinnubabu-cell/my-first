#creation of banking programme
#1.show balance,2.deposit,3.withdraw 
def show_balance():
    print(f'your balance is {balance:2f}')
def deposit():
    amount = float(input('enter the amount to deposit:'))
    if amount < 0:
        print('amount must greater than 0:')
    else:
        return amount
    
def withdraw():
    amount = float(input('enter the amount to withdraw:'))
    if amount < 0:
        print('the amount must be greater than 0:')
        return 0
    if amount < balance:
        print('insufficient fumds')
        return 0
    else:
        return amount

balance = 0
while True:
    print('BANKING PROGRAMME:💸')
    print('1.show balance:💰')
    print('2.deposit:🏦')
    print('3.withdraw:💳')
    print('4.exit🚪')
    user = input('choose a option:')

    if user == '1':
        show_balance()
    elif user == '2':
       balance += deposit()  
    elif user == '3':  
       balance -= withdraw()
    elif user == '4':
     break 
    else:
        print('invalid in put')

