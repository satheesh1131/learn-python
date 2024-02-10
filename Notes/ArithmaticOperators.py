'''
Created on Jun 24, 2023

@author: Hcl
'''

#'+'-> Addition
#'-'-> Subtraction
#'*'-> Multiplication
#'/'-> Division
#'%'-> Modular Function


#Type Promotion: 
#    If we do arithmatic operations with same data type values, then the return type of the output value is also the same.
#    If we do arithmatic operations between two different data types, then the return type of the output is higher type of the two different types.            
a=int(input('Enter a number:\n'))
b=int(input('Enter a number:\n'))
c=a+b
print(c)
print(type(c))
#Here, the return type of c is Integer.
a=int(input('Enter a number:\n'))
b=float(input('Enter a number:\n'))
c=a+b
print(c)
print(type(c))
#Here, the return type of c is Float.
#It applies for Addition,Subtraction,Multiplication

#But by default, Division of two values will always return the output value in Float type.
a=int(input('Enter a number:\n'))
b=int(input('Enter a number:\n'))
c=a/b
print(c)
print(type(c))
#To avoid this float value, we can use '//' as a division operator.
#Now, it will return the output value in Integer type ignoring the values after the decimal point irrespective of any value.
#This is known as Floor Division or Integer Division.
a=int(input('Enter a number:\n'))
b=int(input('Enter a number:\n'))
c=a//b
print(c)
print(type(c))

#Modular function will return the remainder value when dividing two values.
a=int(input('Enter a number:\n'))
b=int(input('Enter a number:\n'))
c=a%b
print(c)


