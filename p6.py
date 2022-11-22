# write a python program to display swapping of two numbers without third variable
a=int(input('Enter the a value: '))
b=int(input('Enter the b value: '))
print('Before swapping a=',a)
print('Before swapping b=',b)
a=a+b
b=a-b
a=a-b
print('After swaping a=',a)
print('After swaping b=',b)