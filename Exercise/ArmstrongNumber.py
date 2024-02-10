'''
Created on Jun 26, 2023

@author: Hcl
'''
def powerOf(base,power):
    i=0
    temp=1
    while i<power:
        temp=temp*base
        i+=1
    return temp
def armstrongNumber(armst):
    digit=list(armst)
    i=0
    total=0
    while(i<len(digit)):
        temp1=int(digit[i])
        total=total+powerOf(temp1,len(digit))
        i+=1
    if total==int(armst):
        print('The number is a Armstrong number')
    else:
        print('The number is not a Armstrong number')

temp=input('Enter the number : ')
armstrongNumber(temp)