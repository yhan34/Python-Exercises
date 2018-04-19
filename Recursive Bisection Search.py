#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 12:03:13 2018

@author: hanlucky
"""

###### Practice 1: Bisection Search #####
# Problem: use biasection search to determine whether a character is in a string
# Hint: Test the middle character of a string. 
# Hint: Done if it is equal to the test char.
# Hint: Search the first half of the string if it is bigger than the test char.
# Hint: Search the second half of the string if it is smaller than the test char.

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    return: True if char is in aStr; False otherwise
    '''
    # Base Case I: If aStr is empty, return False
    if len(aStr) == 0:
        return False
    
    # Base Case II: If aStr is of length 1, check whether aStr is equal to char
    if len(aStr) == 1:
        return aStr == char
    
    # Base Case III: chech wheher the middle char in aStr equal to char
    mid = len(aStr) // 2
    if aStr[mid] == char:
        return True
    
    # Recursive Case: If mid is bigger than char, search the first half 
    elif aStr[mid] > char:
        return isIn(aStr[0:mid])
    
    # Recursive Case: If mid is smaller than char, search the second half
    else:
        return isIn(aStr[mid+1,:])