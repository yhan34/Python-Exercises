#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 20:00:06 2018

@author: hanlucky
"""

################# Python String ###################
# successive concatenation 4*"xy"
# indexing and slicing str[0:10:2]
# len(str): calculate the length of a tring
#### methods of string
# str.replace(old, new): replace characters to other characters in a string
# str.upper(): return the string in upper case
# str.lower(): return the string in lower case
# str.join(): combine a list of strings into a new single string


##### problem 1
# write a python program to calculate the length of a string. 
string = input("Enter the string:")
print(len(string))

##### problem 3 
# write a python program to get a string made of the first 2 and the last 2 characters
# from a given string. If the string length is less than 2, return instead of the empty string.
def sub_str(string):
    if len(string)<2:
        return "Empty String"
    else:
        return string[0:2] + string[-2:]
print( sub_str("w3resource") )
print( sub_str("w3") )
print( sub_str("w") )

#### problem 4
# write a program to get a string from a given string by replacing the occurance
# of the first char by "$", except the first char.
def replace_string(str_old):
    str_new = str_old[0]
    for letter in str_old[1:]:
        if letter == str_old[0]:
            str_new = str_new + "$"
        else:
            str_new = str_new + letter
    return str_new
replace_string("restart")

def change_char(str_old):
    str_new = str_old[0] + str_old[1:].replace(str_old[0], "$")
    return str_new
change_char("restart")  

#### problem 5
# write a program to get a single string from two given strings
# seperated by a space and swap the first two characters of each string
def swap_chars(str1, str2):
    return str2[0:2] + str1[2:] + " " + str1[0:2] + str2[2:]
swap_chars("abc","xyz")

#### problem 6
# write a program to add "ing" at the end of a given string
# if the given string ends with "ing" then add "ly" instead
# if the length of the given string is less than 3, leave it unchanged
def add_ing(str_old):
    if len(str_old) < 3:
        str_new = str_old
    elif str_old[-3:] == "ing":
        str_new = str_old + "ly"
    else:
        str_new = str_old + "ing"
    return str_new
print( add_ing("abc") )
print( add_ing("string") )
print( add_ing("ac"))

#### problem 9
# write a program to remove the nth index character from a non-empty string
def char_remove(string, n):
    if n > len(string):
        raise TypeError("The value of n must be smaller than the length of the string.")
    else:
        return string[:(n-1)] + string[n:]
print( char_remove("Hello", 5))

#### problem 10
# write a program to change a given string to a new string
# by exchanging the first and last chars of the given string
def exchange_str(str_old):
    return str_old[-1] + str_old[1:-1] + str_old[0]
print(exchange_str("Hello"))

#### problem 11
# write a program to remove the chars with odd index
def str_even(str_old):
    str_new = ""
    for i in range(len(str_old)):
        if i % 2 == 0:
            str_new += str_old[i]
    return str_new
            
print(str_even("Hello!"))

##### problem 13
# write a program that takes input from the user and display that in upper
# and lowever cases
info = input("Please enter a string:")
upper = info.upper()
lower = info.lower()
print("Original: {} \n Upper Case: {} \n Lower Case: {}".format(info, upper, lower))

##### problem 16
# write a python function to insert a string in the middle of a string
def insert_string_middle(str1, str2):
    half = int(len(str1)/2)
    str_new = str1[0:half] + str2 + str1[half:]
    return str_new
print( insert_string_middle("<<>>","Hello") )
   
##### problem 17
# write a function to get a string made of 4 copies of the last two characters
# of a specified string (length must be at least 2).
def insert_end(str_old):
    if len(str_old) < 2:
        raise TypeError("The length of the input string must be at least 2.")
    else:
        return 4*str_old[-2:]
print( insert_end("Python") )
print( insert_end("Exercises") )

#### problem 18
# write a function to get a string made of its first three characters of a
# specified string. If the length of the string is less than 3 then return the
# original string.
def first_three(str_org):
    if len(str_org) < 3:
        return str_org
    else:
        return str_org[0:3]
print( first_three("ipy") )
print( first_three("python") )

#### problem 19
# Q: write a python program to get the last part of a string before a specified 
# character. 
# Methods and Functions: str.split(), str.rsplit(), str.join()
def str_before_chr(s, c):
    '''
    s: a string
    c: a character
    returns: the substring before the last spectified character
    '''
    # split the string s with character c as separator
    # slicing all elements in the resulting list expect the last one
    # join elements in the list with ""
    return ''.join(s.split(c)[:-1])    

# test case
str1 = "https://www.w3resource.com/python-exercises/string"
str_before_chr(str1, '/')
str_before_chr(str1, '-')
        
#### problem 20 
# Q: write a python program to reverse a string if its length is a multiple of 4
# Methods and Functions: len(), str.join(), reversed()
def reverse4(s):
    '''
    s: a string
    returns: return a reversed copy of the string if its length is a multiple of 4
    return the original string otherwise
    '''        
    if len(s)%4 == 0:
        return s[::-1]
    else:
        return s
# test case
str1 = "Hello World!"
print( reverse4(str1) )
        
# Alternative Method
"".join(reversed(str1))        

#### problem 21
# Q: write a python function to convert a string to all uppercases if it contains
# at lease 2 uppercase characters in the first 4 characters. 
# Methods and Functions: str.upper(), str.isupper()
def convert_upper(s):
    
    count = 0
    for letter in s[0:4]:
        if letter.isupper():
            count +=1
    
    if count >=2:
        return s.upper()
    else:
        return s

# Test Case
str1 = "HeLLo, world!"  
str2 = "Hello, world!"
print( convert_upper(str1) )
print( convert_upper(str2) )           
          
#### problem 22        
# Q: write a python program to sort a string lexicographically
# Methods and Functions: sorted(iterable, key, reverse), str.join()
def lexicographical(str1):
    return "".join(sorted(str1))       
    
# Test Case
PyStr = "dfeE42"
lexicographical(PyStr)

#### Problem 23 
# Q: Write a python program to remove a new line in Python.
# Method and Function: str.rsplit(separator, maxisplit)
def delete_new_line(PyStr):
    '''
    PyStr: a string with several lines. 
    returns: a string with the last line deleted.
    '''
    return PyStr.rsplit("\n", 1)[0]

PyStr = "This is the 1st line.\nThis is the 2nd line.\nThis is the 3rd line."
print(PyStr)
print( delete_new_line(PyStr) )

#### Problem 24
# Q: write a python program to check whehter a string start with a specified character
# Method and Function: str.startswith()
def startwith(PyStr, PyChr):
    return PyStr[0] == PyChr

# Test Case
startwith("Hello!", "H")

# Alternative method
"Hello".startswith("Hell")

#### problem 28 Edit Later
# Q: write a python program to add a prefix text to all the lines in a string

def prefix_line(PyStr, prefix):
    
    PyList = PyStr.split('\n')
    
    for i in range(len(PyList)):
        PyList[i] = prefix + PyList[i] 
        
    return "\n".join(PyList)

# Test Case
PyStr = "This is the 1st line.\nThis is the 2nd line.\nThis is the 3rd line."
print( prefix_line(PyStr, "Alex says: ") )

#### problem 30 Edit
# write a python program to print the following floating numbers upto 2 decimals.
PyFloat = 10/3
print( round(PyFloat, 2) )


#### problem 38
# Q: write a program to count occurance of a substring 
# Method and Function: str.count()
PyStr = "Learn Python the hard way."
print( PyStr.count("a") )
print( PyStr.count("Python") )

#### problem 39
# Q: write a program to reverse a string.
# Method and Function: reversed(), str.join() 
def string_reverse(PyStr):
    return "".join(reversed(PyStr))

# Test Case
PyStr = "Learn Python the hard way."
print( string_reverse(PyStr) )


#### problem 40 
# Q: write a program to reverse words in a sentence. 
# Method and Function: str.split(), str.join(), reversed()
def words_reverse(PyStr):
    
    # split the string into a list of words
    # reverse the list and then join words with " "
    
    PyList = PyStr.split(" ")
    PyStr = " ".join(reversed(PyList))
    return PyStr

# Test Case
PyStr = "Learn Python the hard way."
print( words_reverse(PyStr) )

#### problem 41 
# write a program to strip a set of characters from a string
def strip_chr(PyStr, PyChr):
    
    PyStr_new = ""
    
    for letter in PyStr:
        if letter not in PyChr:
            PyStr_new += letter
    
    return PyStr_new

# Test Case
PyStr = "Learn Python the hard way."
PyChr = "aeiou"
print( strip_chr(PyStr, PyChr) )

#### problem 42 
# Q: write a program to count repeated characters in a string. 
PyStr = "learnpythonthehardway"
def chr_count(PyStr):
    for character in "abcdefghigklmnopqrstuvwxyz":
        if character in PyStr:
            print(character + str(PyStr.count(character)))
            
chr_count(PyStr)
    
    
#### problem 44
# Q: write a program to print the index of the characters in a string 
PyStr = "Learn Python the hard way."

for i in range(len(PyStr)): 
    print ("Current character " + PyStr[i] + " position at " + str(i))
    print ("Current character {} position at {}".format(PyStr[i], str(i)))

#### problem 45
# Q: write a program to check whether a string contains all alphabetical letters
# Method and Function: str.isalpha
PyStr1 = "Learn Python the hard way."
PyStr2 = "LearnPythonthehardway"
print( PyStr1.isalpha() )
print( PyStr2.isalpha() )

#### problem 46
# Q: write a program to convert a string into a list.
# Method and Function: str.split()
PyStr = "Learn Python the hard way."
PyStr.split()


#### problem 47
# Q: write a program to lowercase first n characters in a string.
# Method and Function: str.lower()
def lower_n(PyStr, n):
    return PyStr[:n].lower() + PyStr[n:]
# Test Case
PyStr = "Learn Python the hard way."
print( lower_n(PyStr, 7) )

#### problem 48
# Q: Write a program to swap comma and dot in a string
# Method and Function: str.split() str.join()
def comma_dot_swap(PyStr):
    
    PyList = PyStr.split(",")
    
    for i in range(len(PyList)):
        PyList[i] = ",".join(PyList[i].split("."))
        
    return ".".join(PyList)

# Test Case
PyStr = "301,204.15"
print( comma_dot_swap(PyStr) )    

#### problem 49
# Q: Write a program to count and display the vowels of a given text
def vowels(PyStr):
    
    PyStr_new = ""
    
    for letter in PyStr:
        if letter in "aeiouAEIOU":
            PyStr_new += letter
    
    return ( len(PyStr_new), PyStr_new )
    
# Test Case
PyStr = "Learn Python the Hard Way."
print( vowels(PyStr) )

#### problem 50 
# Q: write a program to split a string on the last occurance of the delimer.
# Method and Function: str.rsplit(separator, maxsplit)
PyStr = "Learn Python the hard way."
print( PyStr.rsplit(" ", 1) )





    


 