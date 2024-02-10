'''
Created on Jun 25, 2023

@author: Hcl
'''
   
def squareRoot(sqrt):
    i=2
    while i<sqrt:
        if  (sqrt//i)==i:
            print('The square root of the number :',i)
            break
        i+=1
    else:
        print('The given number is not a perfect square')   

sqrt = int(input('Enter the number : '))
squareRoot(sqrt)