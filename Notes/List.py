'''
Created on Jun 24, 2023

@author: Hcl
'''


#List: It is used to store set of values in a single variable. 
#        It is a index based feature. So, the given values are in the user-defined order.
#        It stores the values in a continuous index starting from 0.
#        If we give negative index value, then it retrieve the value starting from last value of the list.
a=[10,20,30,40,50]
print(a[2],end=' ')
print(a[-2],end='\n')
for i in a:
    print(i,end=' ')
print('\n')

#len(list_name) - This function is used to find the length of the list.
#max(list_name) - This function is used to find the maximum value in the list.
#min(list_name) - This function is used to find the minimum value in the list.
print(len(a))
print(max(a))
print(min(a))

#append(value) - This function adds the given value to the list at the end.
#insert(index,value) - This function inserts the given value in the given index of the list and the current index value will be shifted next.
#extend(listOfValues) - This function adds the given list of values to the end of the list.
#append(listOfvalues) - This will adds the entire list to the actual list as an element in the end of the list.
#                        This list inside the list is called as Nested List.
#remove(value) - This function will remove first occurance of the given value from the list.
#pop(index) - This function will remove the value of the given index from the list and returns the removed value.
a.append(60)
print(a)
a.insert(0, 0)
print(a)
a.extend([70,80,90])
print(a)
a.append([100,110,120])
print(a)
a.remove(0)
print(a)
print(a.pop(9))
print(a)

#sort() - This function will arrange the values in the list in ascending order by default.
#sort(reverse=True) - This will arrange the values in the list in descending order.
a.sort()
print(a)
a.sort(reverse= True)
print(a)

#list(values) - List Constructor - This will convert a given String or Tuple value as a list.
b=list('SATHISH')
print(b)

