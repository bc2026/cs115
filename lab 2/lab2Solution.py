''' Bhagawat Chapagain
I pledge by my honor that I haved abided by the Stevens Honor System. '''


def add(x,y):
    ''' Returns the sum of values x and y'''
    return x + y 

def mult(x,y):
    '''Returns the product of values x and y'''
    return x*y


def dot(l1, l2):
    '''Finds the dot product of two vectors, l1 and l2, with recusion.'''
    if len(l1) == 0 or len(l2) == 0:
        return 0
    else:
        return l1[0] * l2[0] + dot(l1[1:], l2[1:])
        
# DONE



def explode(S):
    '''Explodes a string into a list'''
    if len(S) == 0:
        return []
    else:
        return [S[0]] + (explode(S[1:]))

# DONE

def ind(e, L):
    '''finds index given item e and list L'''
    if L == [] or L == "":
        return 0 

    if e == L[0]:
        return 0
    
    if L[0] == e:
        return ind(e,L)
    
    else:
        return 1 + ind(e,L[1:])
    
# DONE

def removeAll(e,L):
    '''remove all instances of item e in list L'''
    if L == []:
        return []
    if L[0] == e:
        return removeAll(e, L[1:])
    else:
        return [L[0]] + removeAll(e, L[1:])

# DONE


def myFilter(f, L):
    ''' my version of filter function'''
    # 
    if L == []:
        return [] 
    if f(L[0]) == False:
        return myFilter(f, L[1:])
    else:
        return [L[0]] + myFilter(f, L[1:])

def deepReverse(L):
    ''' returns reversal of list with item that are lists also reversed'''
    if L == []:
        return []
    if isinstance(L[-1], list):
        return [deepReverse(L[-1])] + deepReverse(L[:-1])
    else:
        return [L[-1]] + deepReverse(L[:-1])

        


