#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 08:35:11 2018

@author: hanlucky
"""

#### problem 1
# Q: write a program to creat a tuple
# Method and Function: tuple()

PyTuple1 = ()
PyTuple2 = ("Blue", "Red", "Yellow")

print( PyTuple1 )
print( PyTuple2 )

#### problem 2 
# Q: write a program to create a tuple with different data types

PyTuple3 = (1, 3.5, False, "a", ["a","c","v"])
print( PyTuple3 )

#### problem 3 
# Q: Write a program to create a tuple with numbers and print one item

PyTuple4 = (1,2,3,4)
print( PyTuple4[2] )

#### problem 4
# Q: write a python program to unpack a tuple in several variables.
v1, v2, v3 = ("1","2","3")
print( v1 )

#### problem 5 
# Q: write a program to add an item in a tuple
# Method and Function: concatenation, list(), list.append() 
# Hint: Tuples are immutable, so you cannot add new elements.
# Hint: Use + operator to concatenate tuples 

PyTuple1 = ("1","2","3")
PyTuple2 = PyTuple1 + ("4",)
PyTuple3 = PyTuple1[0:1] + ("a", "b", "c") + PyTuple1[1:]
print( PyTuple1 )
print( PyTuple2 )
print( PyTuple3 )
# list(): convert a tuple to a list 
# list.append(): append an element to the end of the list
# list is mutable
PyList = list( PyTuple1 )
print( PyList )
PyList.append( "4" )
print( PyList )

#### problem 6
# Q: write a program to convert a tuple to a string. 
# Method and Function: str.join()
PyTup = ("a","b","c","d")
PyStr = "".join(PyTup)
print( PyStr )

#### problem 7
# Q: write a program to get the 4th element and 4th element from last of a tuple
# Method and Function: tuple indexing, 
PyTuple = ("0","1","2","3", "4")
print( PyTuple[4] )
print( PyTuple[-4] )

#### problem 8
# Q: write a program to creat the colon of a Tuple
# Method and Function: tuple cloning; deepcopy()
# indexing and slicing will not make a copy of a Tuple
PyTuple = ([],"0","1","2","3","4")
print( PyTuple )

# correct
from copy import deepcopy
PyTuple_clone1 = deepcopy(PyTuple)
PyTuple_clone1[0].append(1)
print( PyTuple )
print( PyTuple_clone1 )

# wrong clone
PyTuple_clone = PyTuple[:]
PyTuple_clone[0].append(1)
print( PyTuple )
print( PyTuple_clone )


PySubTup = PyTuple[0:2]
print(PySubTup)
PySubTup[0].append(1)
print(PySubTup)
print(PyTuple)


#### problem 9 Edit Later
# Q: write a program to find the unique items of a tuple
def unique_tuple(PyTuple):
    
    # create an empty tuple to store unique elements 
    PyTuple_uniq = ()
    
    # a for loop to search for unique elements 
    for element in PyTuple:
        if element not in PyTuple_uniq:
            PyTuple_uniq += (element, )
    
    return PyTuple_uniq

# Test Case 
PyTuple = ("Red", "Blue", "Yellow", "Red", "Yellow")
print( unique_tuple(PyTuple) )

#### program 10 
# Q: write a program to check whether an element exits within a tuple
PyTuple = (1, 10/3, True, "string", ["a","b","c"])
print( 1 in PyTuple )
print( True in PyTuple )

#### problem 11 
# Q: write a program to convert a list to a tuple.
# Method and Function: tuple()
PyList = [1, 10/3, True, "string", ["1", "2"], (1, 2)]
PyTuple = tuple( PyList )
print( PyList )
print( PyTuple ) 

#### problem 12
# Q: write a program to remove an item from a tuple
# Hint: tuple is immutable, use concatenation 
# Hint: convert tuple to list, use list methods 
# Method and Function: +, list(), del(), list.remove(), tuple.index()
PyTuple = (1, 10/3, True, "string", ["a","b","c"])
print(PyTuple)

# method 1
del_index = PyTuple.index("string")
PyTuple1 = PyTuple[0:del_index] + PyTuple[del_index+1:]
print(PyTuple1)

# method 2
PyList = list(PyTuple)
PyList.remove("string")
PyTuple2 = tuple(PyList)
print(PyTuple2)

#### problem 13
# Q: write a program to slice a tuple
# Method and Function: tuple slicing 
PyTuple = (1, 10/3, True, "string", ["a","b","c"])
print( PyTuple[0:2] )
print( PyTuple[0:4:2] )

#### problem 14
# Q: write a program to find the index of an item of a tuple
# Method and Function: tuple.index()
PyTuple = (1,2, 3, 3, 5, 2)

## use tuple.index()
# index of non-existing element
print( PyTuple.index(4) )
# index of a unique element 
print( PyTuple.index(5) )
# index of a duplicated element
print( PyTuple. index(2) ) 
# define the starting and ending point for searching the element
print( PyTuple.index(3, 3, 5)) 

## self-defined function 
def tuple_index(PyTuple, element):
    '''
    PyTuple: a Tuple
    element: the given element to search index for
    returns: a tuple of indices for the given element in the tuple
    '''
    # raise an error if element does not exist in the tuple
    if element not in PyTuple:
        raise ValueError("The given element is not in the tuple.")
    
    # empty tuple to store the indices of the given element 
    index = ()
    
    # search for elements in the tuple and store its index 
    for i in range(len(PyTuple)):
        if PyTuple[i] == element:
            index = index + (i,)
            
    return index

# Test Case
PyTuple = (1,2, 3, 3, 5, 2, 2)
print( tuple_index(PyTuple, 2) )
print( tuple_index(PyTuple, 4) )

#### problem 15
# Q: write a program to find the length of a tuple
# Method and Function: len()
PyTuple = (1,2, 3, 3, 5, 2, 2)
print( len(PyTuple) )

#### problem 16 Edit Later
# Q: write a program to convert a tuple to a dictionary

#### problem 17 Edit Later
# Q: write a program to unzip a list of tuples into individual lists

#### problem 18
# Q: write a program to reverse a tuple.
PyTuple = (1,2, 3, 3, 5, 2, 2)
PyTuple_rev = tuple(reversed(PyTuple))
print( PyTuple_rev )

#### problem 19
# Q: write a program to convert a list of tuples into a dictionary

#### problem 20
# Q: write a program to print a tuple with string formatting
# Method and Function: str.format()
PyTuple = (100, 200, 300)
print( "This is a tuple {}".format(PyTuple))

#### problem 21
# Q: write a program to replace last value of tuples in a list.
# Method and Function: list(), tuple(), del(), list.append(), +

def last_value_replace1(PyList, element):
    '''
    PyList: a list with tuples as elements
    element: the given element to replace last values of tuples
    returns: a list 
    '''
    for i in range(len(PyList)):
        # convert each tuple into a list
        pylist = list(PyList[i])
        # delete the last element in the list
        del(pylist[-1]) 
        # append the given element into the list
        pylist.append(element)
        # convert the list to a tuple
        PyList[i] = tuple(pylist)   
    return PyList

def last_value_replace2(PyList, element):
    '''
    PyList: a list with tuples as elements
    element: the given element to replace last values of tuples
    returns: a list 
    '''
    for i in range(len(PyList)):
        PyList[i]= PyList[i][:-1] + (element, )
        
    return PyList

# Test Case
PyList = [(10,20,30), (40, 50, 60), (70,80,90)]
print( last_value_replace1(PyList, 100) )
print( last_value_replace2(PyList, 100) )
    

#### problem 22
# Q: write a program to remove empty tuples from a list of tuples

def empty_tuple_remove(pylist):
    '''
    pylist: a list of tuples
    returns: the list with empty tuple removed
    '''
    num = pylist.count(())
    
    while num>0:
        pylist.remove(())
        
    return pylist

PyList = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]  
print( empty_tuple_remove(PyList) )     
    
#### problem 23
# Q: write a program to sort a tuple by its floating element.
PyList = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print(PyList)
PyList.sort(key=)

#### program 24
# Q: Write a program to count the elements in a list unitl an element is a tuple
# Method and Function: type(), isinstance(obj, class)
def count_before_tuple(pylist):
    '''
    pylist: a list 
    returns: the number of elements before a tuple shows up
    '''
    if type(pylist) != list:
        raise ValueError("The input is not a list.")
        
    tot = 0 
    
    for element in pylist:
        if type(element) != tuple:
            tot += 1
        else:
            break
    
    return tot

# Test Case
PyTuple = (1,2,3)
PyList = [10,20,30,(10,20),40]
print( count_before_tuple(PyList) )
print( count_before_tuple(PyTuple) )









