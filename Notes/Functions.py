'''
Created on Jun 25, 2023

@author: Hcl
'''

#Functions: It is used for code re-usability. 
#            If a set of codes performs an action which will be needed several times,
#            then we can define it as a function and we can call this function whenever and wherever we want.
#syntax: 
#def functionName():
#    Executable_Statements
#Non-Void Function: If a function return a value to the function call, then it is Non-Void Function.
def add():
    a=int(input('Enter the number : '))
    b=int(input('Enter the number to add : '))
    return a+b

print('The added value : ',add())

#Void Function: If a function does not return a value to the function call, then it is Void Function.
#                By default, these functions will return 'None' - Absence of value.
def sub():
    a=int(input('Enter the number : '))
    b=int(input('Enter the number to subtract : '))
    print('The subtracted value : ',(a-b))

print(sub())

#Parameterized function - This function will have the input values for our operation in the function call statement.
#                            This will be received by the function definition.
def multiply(a,b):
    return a*b

print(multiply(5, 10))

#We can also give a default value for the parameter in the function definition.
#It will be assigned if we did not give any input values in the function call statement.
#If the input values are given in the function call statement,
#then, the given default value in the function definition will be ignored.
def division(a=1,b=1):
    return (a/b)

print(division(15, 3))
print(division())

