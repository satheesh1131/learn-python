'''
Created on Jun 23, 2023

@author: Hcl
'''
#Print statement for a string input
print("Hello")
#Print statement for a string input, as " or ' is same in python.
#Because single character is also a string in python.
print('World')
#Multiple line Print statement is achieved by triple quotes. 
print('''This is 
my first program''')
#sep is used to separate a string with any specified characters that we give. default=' ' -->space
#end is used to give the end of the line value. default='\n' --> new line
#'\t'-->tabSpace : 
print('Hello','World',sep='_',end=' ')
print('Is Mine')
#To print string value number of times, we can just use *-> symbol and give n-> number of times.
print('Sathish'*5)
#To concadination of the string, we can add +-> symbol between string values we going to concadinate.
print('Hello'+'World')

#Example
str1='code'
str2='io'
print(str1,'.',sep='',end='')
print(str2)


#String Function:
#split(value) - It splits the entire String value into number of String values by the given Value.
#                Default value is ' '(space).It returns the values in form of List.
s='my python program'
print(s.split())
s='split*function*of*string'
print(s.split('*'))

#strip(value) - This function removes all the given value from start and end of the String value.
#rstrip(value) - This function removes all the given values from end of the String only.
#Lstrip(value) - This function removes all the given values from start of the String only.
#By default, the value is ' '(space). So, it removes all the blank spaces.
st='   sathish   '
print(st.strip())
print(st.lstrip())
print(st.rstrip())

#find(value,startIndex,endIndex) - This function finds the given value present in the actual value between the given index and returns its index.
#By default, startIndex is '0' and endIndex is the length of the string value.
s='python program'
print(s.find('pro'))
print(s.find('gram', 5, 11))
#It returns '-1' when the given value is not present in the actual String value within the specified index.

#isdigit() - This function checks whether the String value contains only numeric and returns boolean value.
#isalpha() - This function checks whether the String value contains only alphabets and returns boolean value.
#isalnum() - This function checks only alphabets and numeric values are present in the String value and returns boolean value.
#isspace() - It checks whether the String value contains only spaces and returns boolean value.
a='10 is a numeric value'
b='20'
c='python'
print(a.isalnum())
print(b.isdigit())
print(a.isspace())
print(c.isalpha())

#lower() - This function converts entire String value into lower case characters.
#upper() - This function converts entire String value into upper case characters.
#capitalize() - This function converts first letter of the String value into upper case character.
a='pyThoN ProgRaM'
print(a.upper())
print(a.lower())
print(a.capitalize())

 

