def kfp(n):
    if n == 1:
        return 1
    elif n == 2: 
        return 2
    elif n == 3:
        return 4 
    else:
        return kfp(n-3) + kfp(n-2) + kfp(n-1)


##########################
'''Using Memoization'''
##########################


dic = {1:1, 2:2, 3:4}

def fastKfp(n):
    if n in dic: 
        return dic[n]
    ans1 = fastKfp(n-1)
    dic[n-1] = ans1
