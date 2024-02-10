'''
Created on Jun 26, 2023

@author: Hcl
'''

def factors(factValue):
    i=1
    while(i<=factValue):
        if(factValue%i==0):
            print(i,end=' ')
        i+=1
        
temp=int(input('Enter the number : '))
print('The factors of the number : ')
factors(temp)