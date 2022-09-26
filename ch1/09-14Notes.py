from functools import reduce


def dbl(x):
	return 2*x

def add(x,y):
	return x + y
def addSq(x,y):
	return x + y**2
# Map 
#	* Don't need to import
# 	#* Takes two arguments
# 	* Function map takes 1 argument and returns one result
# 	* Map returns a list (use list())


# Reduce
#	* Must import functools
# 	* Takes two arguments
# 	* Function reduce takes receives 2 arguments returns one result
# 	* Returns integer value 



def guass(n):
	return reduce(add, range(n+1))

def sumOfSquares(n):
	return reduce(addSq, range(n+1))

def span(L):
        mx = reduce
        mn = reduce
        return mx - mn

#print(span([3,1,42,7]))
#print(span([42,42,42,42]))

print(guass(3))
print(sumOfSquares(3))



