
'''
Created on Jun 24, 2023

@author: Hcl
'''

#Loops: It is used to do a repeated operation for a number of times.
#
#for loop: 
#    syntax: for i in range(initial_value,final_value,step_value):
#                Execution_statements
for i in range(0,50,5):
    print(i,end=' ')
print('\n')

#range() function executes statements starts from (initial_value) to (final_value - 1) by iterating (step_value) each time.
#By default, initial_value is '0' and step_value is '1'. But the final value must be defined by the user within the syntax.
for i in range(10):
    print(i,end=' ')
print('\n')

#while loop: 
#    syntax: while (condition_statement)
#                Execution_statements
a=0
while (a<=5):
    print(a,end=' ')
    a+=1
print('\n')

#Jump Statements:
#    break - It breaks the execution of the loop when the condition for the jump statement is true.
for i in range(5):
    if(i==2):
        break
    print(i,end=' ')
print('\n')

#    continue - It skips the particular iteration of the loop when the condition for the jump statement is true.
for i in range(5):
    if(i==2):
        continue
    print(i,end=' ')
print('\n')

#loop else: It executes the statement only when the execution of the loops completed successfully without external break statement.
for i in range(10):
    print(i,end=' ')
else:
    print('\nElse_Block')

#           If a execution of loop is stopped by break statements, then the codes within the else block will not be executed.
for i in range(5):
    if(i==2):
        break
    print(i,end=' ')
else:
    print('Else_Block')
print('\n')

#           If a execution of loop is skipped by continue statements, then the codes within the else block will be executed.
for i in range(5):
    if(i==2):
        continue
    print(i,end=' ')
else:
    print('\nElse_Block')

