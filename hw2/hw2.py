'''
Created on 09 26 2022
@author:   Bhagawat Chapagain & Neel Kulkarni
Pledge:    I pledge my honor that I have abided by the Stevens Honor System. 
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

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.
def letterScore(letter, scoreList):
  if letter == "" or scoreList == []:
    return 0
  elif letter == scoreList[0][0]:
    return scoreList[0][1]
  else:
    return letterScore(letter, scoreList[1:])

'''print(letterScore("z", scoreList=scrabbleScores)) -> returns 10''' 

def wordScore(S, scoreList):
  if S == "":
    return 0
  else:
    return letterScore(S[0], scoreList) + wordScore(S[1:], scoreList)
    
'''print(wordScore("spam", scrabbleScores)) -> returns 8
print(wordScore("wow", [['o', 10], ['w', 42]])) -> returns 94'''

def scoreList(Rack):
    pass
