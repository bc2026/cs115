'''
Created on 9/26/2022
@author:   Neel Kulkarni, Bhagawat Chapagain
Pledge:    I pledge my honor that I have abided by the Stevens Honor System
CS115 - Hw 2
'''

import sys
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]



# Implement your functions here.




#1. Take the dictionary and filter out words that can't be made from the rack
Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']


def validWords(Dict): #Returns a filtered list of words in the dictionary that can be made from the rack
    filteredList = list(filter(canWord, Dict))
    return filteredList

def canWord(w): #Returns if a word can be made from a rack
    return w == wordInRack(w, rack)

def ind(e, L):
    '''Returns the index where e is found in sequence L'''
    if (L == [] or L == ""): 
        return 0
    if (L[0] == e):
        return 0 #If the value is e, then it returns 0 and ends recursion
    else:
        return 1 + ind(e,L[1:])

def wordInRack(w, R): #Returns the combination of letters in a word that can be made with the letters in a rack (used in combination with canWord to see if the combination matches the actual word)
    if R == [] or w == '' or (w[0] not in R):
        return ''
    else:
        return w[0] + wordInRack(w[1:], R[0:ind(w[0],R)] + R[ind(w[0],R)+1:])

#2. Assign each of those words scores

def wordScoreList(S): #Returns a word and its score in list format
    return [S, wordScore(S, scrabbleScores)]

def wordScore(S, scorelist): #Returns the score for a word
    if S == '':
        return 0
    else:
        return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)

def letterScore(letter, scorelist): #Returns the score for an individual letter
    if scorelist == []:
        return 0
    elif scorelist[0][0] == letter:
        return scorelist[0][1]
    else:
        return letterScore(letter,scorelist[1:])

def listofScores(L, scoreList): #For a given list of words, returns the word and score of each
    return list(map(wordScoreList, L))

def scoreList(R): #Returns a scoreList with each word and it's given score
    global rack
    rack = R
    newDictionary = validWords(Dictionary)    
    return listofScores(newDictionary, scrabbleScores)

#3. Choose the highest score out of all

def maxInList(L): #Returns the max number in the scoreList
    if L == []:
        return 0
    else:
        return max(L[0][1], maxInList(L[1:]))

def findWord(L, s): #Finds the word that matches with the max score in the scoreList
    if (L == []):
        return ''
    elif (L[0][1] == s):
        return L[0][0]
    else:
        return findWord(L[1:], s)
        

def bestWord(R): #Returns the best word based on the max score
    listOfScores = scoreList(R)
    maxScore = maxInList(listOfScores)
    word = findWord(listOfScores, maxScore)
    return [word,maxScore]
