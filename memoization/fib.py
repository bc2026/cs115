memo = {}


def fastFib(n):
    if n in memo:
        return memo[n]
    if n < 0: 
        return "Incorrect input"
    elif n == 0:
        memo[n] = 0
        return 0 
    elif n == 1 or n == 2:
        memo[n] = 1 
        return 1
    else:
        first_term = fastFib(n-1)
        memo[n-1] = first_term
        second_term = fastFib(n-2)
        memo[n-2] = second_term
        return first_term + second_term