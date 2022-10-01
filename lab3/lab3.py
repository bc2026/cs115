# Bhagawat Chapagain
# I pledge my honor that I haved abided by the
# Stevens Honors System. 

def change(amount, coins):

    '''This function will return the shortest way to pay for some amount withn some array of coins, called coins'''

    if amount == 0:
        return 0  # If there is no amount, then obviously there are only zero ways to make up zero
    elif coins == []:
        return float('inf') # Do this so that the algorithm doesn't keep looping if coins is empty
    elif amount < coins[0]:
        return change(amount, coins[1:]) # go one into the coins array and recurse
    else: 
        use_it = 1 + change(amount-coins[0], coins) # the current coins
        lose_it = change(amount, coins[1:]) # the rest of the array from the first one
        return min(use_it, lose_it) # return the smallest number 







