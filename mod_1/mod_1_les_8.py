# программа Tip Calculator
am_bill = float(input('Enter the amount of the bill: '))
am_tip = float(input('Enter the tip amount: '))
nu_visitors = int(input('Enter the number of visitors: '))
summa = am_bill + am_tip
am_per_one = summa / nu_visitors
print('Each person should pay: ' + str(am_per_one))
