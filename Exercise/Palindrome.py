'''
Created on Jun 27, 2023

@author: Hcl
'''

def palidromeCheck(inputStr):
    frwd=inputStr
    bkwd=inputStr[::-1]
    if (frwd==bkwd):
        print('The input Object is a palindrome')
    else:
        print('The input object is not a palindrome') 
    
temp=input('Enter the Object : ')
palidromeCheck(temp)   
        
    