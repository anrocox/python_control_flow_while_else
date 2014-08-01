#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 23, 2014

@author: anroco

How to use the while-else loop in Python?

¿Cómo se usa la estructura while-else en Python?
'''

#The while loop has associated else statement, as occurs with the if statement
#the else statement runs only if the while loop ends normally and not by a
#break statement

#create a integer
n = 1

#iterates whilst the value of n is less than 10
while n < 10:
    print ('n = ' + str(n))

    #checks if the remainder of the division by two is equal to 0
    #if n is a odd number ends the cycle
    if n % 2 != 0:
        break

    #adds 2 to value n
    n += 2

#runs only if the condition of while loop is False
else:
    print('the values of n are even numbers')

print('the value of n after of end the while loop is {}'.format(n))
