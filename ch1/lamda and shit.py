def mystery(item, L): 

        newL = map(lambda X: X == item, L)  # <--- this one will look for values greater than item
        return sum(newL) > 0


def mysteryA(item, L):

    newL = filter(lambda x: x == item, L)  # <--- this one will only look for values equal to item
    return sum(newL) > 0


# returns true if item first argument is in the list;  else, false 


def prime(n):
    possibleDivisiors = range(2,n)
    divisors = filter(lambda x: n % x == 0, possibleDivisiors)

    return sum(divisors) == 0



def primes(n):
    return sieve(range(2,n+1))


def sieve(L):
    if L == []: return []
    else: filter(lambda x: L[0] % x , L[1:])

    
def listPrime(n):
    numbers = range(2,n)

    lambda x : n % x == 0