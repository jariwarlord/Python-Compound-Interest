p = float(input("Enter the principal amount: $"))
r = float(input("Enter the annual interest rate: "))
n = float(input("Enter the number of times per year interest has compounded: "))
t = float(input("Enter the number of years account will be left for earn interest: "))

r /= 100

A = p * (r/n)**(n**t)

print('After', t , 'years $', A, 'amount of money will be in the account')