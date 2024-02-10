'''
Created on Jun 26, 2023

@author: Hcl
'''

def factorial(factValue):
    i=0
    total=1
    while(i<factValue):
        total=total*(i+1)
        i+=1
    return total
    
temp=int(input('Enter the number : '))
print('The factorial of the number : ',factorial(temp))

    