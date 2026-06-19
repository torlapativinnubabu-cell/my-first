#creation of intrest calculator
principal =0
rate =0
time =0
while True:
    principal = float(input("Enter the principal amount: "))
    if principal < 0:
        print("Principal amount cannot be negative.")
    else:
        break
while True:
    rate = float(input("Enter the rate of interest (in percentage): "))
    if rate < 0:
        print("Rate of interest cannot be negative.")
    else:
        break
while True:
    time = float(input("Enter the time in years: "))
    if time < 0:
        print("Time cannot be negative.")
    else:
        break

total_amount = principal *pow(1 + rate/100,time)
print(f"The total amount after, {time}, years is:, ${total_amount}")