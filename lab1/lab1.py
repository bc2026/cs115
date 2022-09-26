############################################################
# Name: Bhagawat Chapagain
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS115 Lab 1
#  
############################################################

from math import factorial # import factorial function
from functools import reduce # import reduce function


def addition(n,k):
    return n+k # returns the sum of n and k

def inverse(x):
    return 1/x # returns the inverse of x

def e(n):
    L = range(n+1) # gets a list of nuns from 1 to n+1
    F = list(map(factorial, L)) # gets a list of facotirals from previous list L
    I = list(map(inverse, F)) # gets the inverse of the factorials
    
    return (reduce(addition, I))# return the sum of all of the inverses



