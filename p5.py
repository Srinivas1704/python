# write a python program to calculate EMI
p=int(input('Enter principle amount: '))
t=int(input('Enter the time period: '))
r=float(input('Enetr the rate of intrest: '))
si=(p*t*r)/100
print('Simple intrest of given principle is ',si)
emi=(p+si)/t*12
print('EMI is ',emi)