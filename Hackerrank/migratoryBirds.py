#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 23:46:56 2020

@author: aims
"""

arr = (1,2,3,4,5,4,3,2,1,3, 3, 4,4)

def migratoryBirds(arr):
    dic = {}
    
    for i in range(len(arr)):
        if arr[i] not in dic:
            dic[arr[i]] = 1
        else:
            dic[arr[i]] += 1
    out = [0, 0]     
    for i in set(arr):
        if dic[i] > out[1]:
            out = [i, dic[i]]
    
    #maxim = (max(dic, key = dic.get))
            
    return out[0]

print(migratoryBirds(arr))

    