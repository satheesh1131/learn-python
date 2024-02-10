'''
Created on Jun 26, 2023

@author: Hcl
'''

def primeNumber(prime):
    i=2
    while(i<prime):
        if ((prime%i)==0):
            print('The given number is not a prime number')
            break
        i+=1
    else:
        print('The given number is a prime number')

temp=int(input('Enter the number : '))
primeNumber(temp)