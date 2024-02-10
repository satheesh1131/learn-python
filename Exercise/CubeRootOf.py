'''
Created on Jun 27, 2023

@author: Hcl
'''

def cubeRootOf(cubeRT):
    i=cubeRT-1
    while (i>0):
        if ((cubeRT%i)==0):
            temp1=cubeRT//i
            if ((i//temp1)==temp1):
                print('The cube root : ',temp1)
                break
        i-=1
    else:
        print('The given number is not perfect cube root')

temp=int(input('Enter the number : '))
cubeRootOf(temp)
                
            
            