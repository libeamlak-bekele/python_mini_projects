# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 21:00:34 2022

@author: legen
"""
#The first code after graduation

### Calculate the length of a string
# def length_str(name):
#     count = 0
#     for x in name:
#         count =  count + 1
#     return count 


### Count the number of character frequency in a string

# string = 'libeamlak'
# item = []
# for x in string:
#     if x in item:
#         break
    
#     out = f"'{x}': {str(string.count(x))}"
#     print(out)
#     item.append(x)

### get a string made of the first 2 and the last 2 chars from a given a string.
### If the string is made of less than two letters chars print 'Empty String'

# string = 'l'
# if len(string) < 2:
#     print('Empty String')
# else:
#     print(string[0:2] + string[-2:])

### Write a Python program to get a string from a given 
### string where all occurrences of its first char have 
## been changed to '$', except the first char itself.

# def newchar(string):
#     a = string[:1]
#     newone = string[1:]
#     for x in newone:
#         if x == a:
#             name = newone.replace(a, '$')
#     return a + name

# print(newchar('restartra'))

### question #6

# def change_last_to_ing(string):
#     newstring = string[-3:]
#     if len(string) < 3:
#         return string
#     elif newstring == 'ing':
#         return string + 'ly'
#     else:
#         return string + 'ing'
    
# print(change_last_to_ing('ling'))

### Python program to count the occurrences of each word in a given sentence.

# def count_word(sentence):
#     x = sentence.split()
#     item = []
#     for i in x:
#         if i in item:
#             break
#         else:
#             out = f'"{i}": {str(x.count(i))}'
#             print(out)
#         item.append(i)
        
# count_word('this python code is for students in this class')

# string = 'libeamlak,santa,abiti,misge,wore'
# newstr = string.split(',')
# print(sorted(newstr))

### Datetime
# from datetime import datetime, timedelta
# current_date = datetime.now()
# print(current_date)

### Question #20

# def reverse_string(string):
#     multi = len(string)/4
#     if multi == 1:
#         print(string[::-1])
#     else:
#         print(string)

# reverse_string('libe')

### Caesar's cipher or Caesar encryption

# def Caesar_cipher(string):
#     string = string.lower()
#     letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o'
#           ,'p','q','r','s','t','u','v','w','x','y','z']
#     new_string =''
#     for i in string:
#         index = letter.index(i)
#         if index == 23:
#             index = 0
#         elif index == 24:
#             index = 1
#         elif index == 25:
#             index = 2
#         else:
#             index = index + 3
#         new_string = new_string + letter[index]
    
#     return new_string
        
# print(Caesar_cipher('Libeamlak')) 

### print 2 floating number
# x = 3.1416987
# print(f'{x:.2f}')


        
            
        


        
        
    
    





    
