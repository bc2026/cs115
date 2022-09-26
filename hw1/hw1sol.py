# Name: Bhagawat Chapagain
# Pledge: I pledge my honor that I have abided by the Stevens Honor System. 


from functools import reduce

def mult(x,y):
    ''' Returns the product of x and y''' 
    return x * y

def add(x,y):
    '''return the sum of x and y'''
    return x + y 
def factorial(n):
    '''Factorial function as defined by n! = n*(n-1)(n-2)...'''
    return reduce(mult, range(1, n+1)) 

def mean(L):
    '''Finds the mean of numbers in a list L'''
    return reduce(add, L)/(len(L)) 


