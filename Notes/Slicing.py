'''
Created on Jun 25, 2023

@author: Hcl
'''
#Slicing: This option is used to slice the values in String or List or Tuple.
#syntax: variable[startIndex:endIndex:step]
#By default step value is '1',startIndex value is '0', endIndex value is its length.
a='python program'
print(a[0:6])
print(a[:])
b=[10,15,20,25,30,35,40,45,50]
print(b[0:9:2])
c=(1,2,3,4,5,6,7,8,9)
print(c[2:6])

#If we give step value in negative, then it is executes in reverse order.
#This slicing option does not affect the original value in the variable.
#It takes the copy of values and performs the given operation,leaving the actual value in the variable unaffected.
d=[1,2,3,4,5]
print(d[::-1])
print(d)

