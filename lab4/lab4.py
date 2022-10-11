'''
Bhagawat Chapagain
I pledge my honor that I have abided by the Stevens Honor System. 
CS115 Lab 4
Oct. 6, 2022
'''
def knapsack(capacity, itemList):
    """ returns both the maximum value and the list of items that make this value, without exceeding the cap of your knapsack"""
    if itemList == []:
        return [0,[]]
    if capacity == 0:
        return [0, []]
    if capacity - itemList[0][0] < 0:
        return knapsack(capacity, itemList[1:])
    useIt = knapsack(capacity - itemList[0][0], itemList[1:])
    lostIt = knapsack(capacity, itemList[1:])
    if itemList[0][1] + useIt[0] >= lostIt[0]:
        return [itemList[0][1] + useIt[0]] + [[itemList[0]] + useIt[1]]
    else:
        return [lostIt[0]] + [lostIt[1]]
