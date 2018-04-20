#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 09:56:50 2018

@author: hanlucky
"""

########### Problem 1 Debt over a year ########### 
# Q: write a program to calculae the credit card balance after one year if a 
# person only pay the minimum monthly payment required by the credit card company.

def balance_over_year(balance, annualInterestRate, monthlyPaymentRate):
    '''
    balance: the starting balance on the credit card
    annualInterestRate: annual interest rate as a decimal
    monthlyPaymentRate: minimum monthly payment rate as a decimal
    
    returns: the balance on the credit card over a year
    '''
    # calcualte the monthly interest rate
    monthlyInterestRate = annualInterestRate/12.0
    
    i = 1
    while i <= 12:
        # calculate the minimum monthly payment one pay and the balance  
        # at the end of month (i-1)
        monthlyPayment = balance * monthlyPaymentRate
        monthlyUnpaidBalance = balance - monthlyPayment
        
        # update balance at end of month i
        balance = monthlyUnpaidBalance * (1 + monthlyInterestRate)
        
        i += 1
        
    return balance

# Test Case
balance = balance_over_year(balance=42, annualInterestRate=0.2, monthlyPaymentRate=0.04)
print("Remaining Balance: " + str(round(balance, 2)))
        
        
########### Problem 2 Paying Debt off in a year ###########
# Q: write a program to calcuate the minimum fixed monthly payment needed 
# in order to pay off a credit card balance within 12 month.    

def lowest_monthly_payment(balance, annualyInterestRate):
    '''
    balance: the outstanding balance on the credit card
    annualInterestRate: annual interest rate as a decimal 
    
    returns: the lowest monthly payment (in $10) to pay off the debt in a year
    '''
    
    # a function to calculate the balance on the credit card over a year
    def balance_over_year(balance, monthly_payment, annualInterestRate):
        
        monthlyInterestRate = annualInterestRate/12.0
        
        i = 1
        while i <= 12:
            balance = (balance-monthly_payment)*(1 + monthlyInterestRate)
            i += 1
        
        return balance
    
    # Base Case: the remaining balance on the credit card 
    guess = 0
    remaining = balance_over_year(balance, guess, annualInterestRate)
    
    # a while loop to search for the lowest monthly payment with increment 10
    while remaining >= 0:
        guess += 10
        remaining = balance_over_year(balance, guess, annualInterestRate)
        
    lowest_monthly_payment = guess
    
    return print("Lowest Payment: " + str(lowest_monthly_payment))
    
# Test Case
lowest_monthly_payment(balance=3329, annualyInterestRate=0.2)

  
########### Problem 3 Paying Debt off in a year (Bisection Search) ###########
# Q: write a program to calcuate the minimum fixed monthly payment needed 
# in order to pay off a credit card balance within 12 month. 

def lowest_monthly_payment(balance, annualInterestRate):
    '''
    balance: the outstanding balance on the credit card
    annualInterestRate: annual interest rate as a decimal 
    
    returns: the lowest monthly payment to pay off the debt in a year
    '''
    
    # a function to calculate the balance on the credit card over a year
    def balance_over_year(balance, monthly_payment, annualInterestRate):
        
        monthlyInterestRate = annualInterestRate/12.0
        
        i = 1
        while i <= 12:
            balance = (balance-monthly_payment)*(1 + monthlyInterestRate)
            i += 1
        
        return balance
    
    # Base Case:
    lower = balance/12.0 
    upper = balance_over_year(balance, 0, annualInterestRate)/12.0
    mid = (lower + upper)/2
    remaining = balance_over_year(balance, mid, annualInterestRate)
    criterion = 0.001
   
    # a while loop to search for the lowest monthly payment
    while abs(remaining) > criterion:
        
        if remaining > 0:
            lower = mid
        else:
            upper = mid
        
        mid = (lower + upper)/2
        remaining = balance_over_year(balance, mid, annualInterestRate)
    
    lowest_monthly_payment = round(mid,2)
    
    return print("Lowest Payment: " + str(lowest_monthly_payment ))
              
            
# Test Case
lowest_monthly_payment(balance=32, annualInterestRate=0.2)         
        
