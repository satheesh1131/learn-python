'''
Created on Jun 25, 2023

@author: Hcl
'''

def powerOf(base,power):
    i=0
    temp=1
    while i<power:
        temp=temp*base
        i+=1
    return temp

base=int(input('Enter the base : '))
power=int(input('Enter the power : '))
print('The result : ',powerOf(base, power))