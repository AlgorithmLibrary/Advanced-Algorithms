# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 15:27:19 2021

@author: Grant
"""

from itertools import product
from itertools import permutations  

points = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 5], [3, 6]]
#points = [[1, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7]]
#points = [[1, 2, 3], [4, 5, 6]]

def sublists(lst):
    for doslice in product([True, False], repeat=len(lst) - 1):
        slices = []
        start = 0
        for i, slicehere in enumerate(doslice, 1):
            if slicehere:
                slices.append(lst[start:i])
                start = i
        slices.append(lst[start:])
        yield slices

def check_independence(input_list):
    independence = True
    
    if len(input_list) == 1:
        return independence
    
    for a in range(len(input_list)):
        for b in range(len(input_list)):
            if a == b:
                continue
            else:
                if [input_list[a], input_list[b]] in points or [input_list[b], input_list[a]] in points:
                    independence = False
    
    return independence

def check_list(input_list, n):
    summation = 0
    
    single_independence = True
    for a in range(len(input_list)):
        independent_set = check_independence(input_list[a])
        
        if independent_set == True:
            summation += 1
        else:
            single_independence = False
    
    if single_independence == False:
        summation = 0
    
    return summation

n = 6

total_summation = 0

k = 3

perm = permutations([1, 2, 3, 4, 5, 6])
perm_list = [list(i) for i in perm]

colorable_exist = False

for vertices in perm_list:
    subsets = list(sublists(vertices))
    for i in range(len(subsets)):    
        temp_factor = check_list(subsets[i], n)
        if len(subsets[i]) != k:
            temp_factor = 0

        f_factor = temp_factor
        
        total_summation += f_factor


if total_summation > 0:
    print("There is a", k, "colorable subset")
else:
    print("There is not a", k, "colorable subset")


  