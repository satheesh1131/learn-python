'''
Created on Jun 25, 2023

@author: Hcl
'''

#Dictionary: It is not index based feature. So, the given values are not in the user defined order.
#            It is a key based feature and each key has its own value and the values are accessed by the value.
#            The key values are unique, that means duplicate key value is not allowed.
#            The value can be any data types but the key value must be a immutable data type like integer, string or tuple.
a={0:'My' , 1:'first' , 2:'program' }
for i in a:
    print(i,a[i])
print('\n')

#update() - This function will add the given dictionary value to the actual dictionary. If there is same keys in both the values, then the values will be updated in the actual dictionary.
#            This will not affect the given value to be added.
b={2:'python' , 3:'program'}
a.update(b)
print(a)
print(b)

#Defining the key and its value will add this entry to the dictionary. If we give the key value which is already in the dictionary, then it will be updated.
a[5]='sathish'
print(a)

#del D[key] - This will delete the entry of the given key and its value.
del a[5]
print(a)

#pop(key) - This will also delete the given key and its value. But, it will return the deleted value.
print(a.pop(0))
print(a)

#keys() - This function will return all the keys in the dictionary as a list.
#values() - This function will return all the values in the dictionary as a list.
#items() - This function will return all key value pair in a list. Each pair will be in a tuple inside this list.
print(a.keys())
print(a.values())
print(a.items())

#value in dictionary - This will check whether the given value is present in the keys of dictionary. And returns boolean value.
#value in dictionary.values() - This will check the given value is present in the values of dictionary. And returns boolean value.
print(1 in a)
print('first' in a.values())

