'''
Created on Jun 25, 2023

@author: Hcl
'''
# Tuple: It is just like the List. But we cannot change or add or remove the value from tuple.
#        Because it is a Immutable Data Type. 
#        It is a index based feature. So, the given values are in the user-defined order.
a=(10,20,30)
print(a[2])
for i in a:
    print(i,end=' ')
print('\n')

#As it is immutable, the 'append', 'insert', 'remove', 'extend', 'pop', 'sort' functions cannot be used in Tuple.
#tuple() - we can use this Constructor Tuple just like the List. We can also convert a list into Tuple by using this function.
b=tuple('SATHISH')
for i in b:
    print(i,end=' ') 
print('\n')

#If a single value is assigned to the tuple, then its actual data type will be returned instead of tuple.
a=(1,2,3)
b=(1)
print(type(a))
print(type(b))
