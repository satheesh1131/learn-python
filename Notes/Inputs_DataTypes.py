'''
Created on Jun 24, 2023

@author: Hcl
'''
#Variables-> Used to store values or data.
#String-> Single or collection of characters. Data must be given in single or double quotes.
#Integer-> Any number is called as a Integer. It can be a positive or negative numbers.
#Float-> Decimal numbers are called as Float.



#type()-> It is used to find the data type of a given variable.
a=5
b='String value'
c=100.258
print(type(a))
print(type(b))
print(type(c))

#input()-> It is a function used to get inputs from user while running program.
#It always return the input value in String.
i=input('Enter Value:')
print(i) 
print(type(i))

#int()-> It is function used to convert input values from string to Integer type.
j=int(input('Enter the value:'))
print(j)
print(type(j))

#float()-> It is function used to convert input values from string to Float value.
k=float(input('Enter the value:'))
print(k)
print(type(k))
