# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 16:40:05 2022

@author: legen
"""

### max of three numbers
# def max_of_three_nums(x,y,z):
#     if x == y and x == z:
#         return 'The three numbers are equal'
#     elif x >= y and x >= z:
#         return x
#     elif y >= x and y >= z:
#         return y
#     elif z >= x and z >= y:
#         return z

# print(max_of_three_nums(5, 5, 5))

def sum_list(num):
    added = 0
    for i in num:
        added = added + i
    return added

a = [1,2,3,4,5]
print(sum_list(a))


