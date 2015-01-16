import mm_utility as Util   # utility file for cleaner code
import numpy as np
import sys
from numpy.random import rand
import random


def main():
    filename = 'oldmansea'
    #filename = 'cockoosnest' 
    # num distinct words, list of a'll words, list of all distinct words 
    allwords, d_allwords = cleanInput(filename)    
    
    # our markov model (2 dimentional array)
    # height x width: number of distinct words in the story
    markov = createModel(allwords, d_allwords)

    # We have our matrix of distinct words and the weighted probability 
    # from one word to another in the form of a numpy matrix
    # It's time to process a chain:
    processChain(markov, d_allwords)
    

    
# Read the specified input file and return the list of all words 
# as well as distinct words
def cleanInput(rawinput):
    # -----stats to keep track of-----
    nTotalWords = 0
    nDistinctWords = 0
    # --------------
        
    
    # given an input file name, get the full path to the input file
    # residing in the raw input file directory
    infile_path = Util.getPath(rawinput)

    # Get a 'list' of all the words in the raw_input file.  Each of these words are 
    # filtered as such: must be a string -> must contain only letters and 
    # numbers (alphanumeric) -> must only be upper and lower case letters
    allwords = Util.getWords(infile_path)       # will contain list of all 'words' in file
    nTotalWords = len(allwords)

    # Our list of words is not necessaraly distinct, we want it to be.
    # we get the list of distinct words this way
    allwords_distinct = Util.uniqueafy(allwords)
    nDistinctWords = len(allwords_distinct)


    print '-- Processed: {0} -- \n Total Words: {1} \n Distinct Words: {2}'.format(rawinput, nTotalWords, nDistinctWords)
    
    return allwords, allwords_distinct


# take the number of distinct words, list of all words, and the 
# list of all distinct words.  Determine the probability distibution 
# for each word following each word.
def createModel(all_w, dist_w):
    n = len(dist_w)
        
    # this 2D matrix represents the frequency of 'hits' one words has against other words
    A = np.matrix(np.zeros(n*n).reshape((n,n)))
    
    # now loop through each distinct word and
    # find the index of each word that follows it and
    # increas the count in our matrix, A
    for i in xrange(n):
        count = 0                               # count:= |{words following this word}|
        
        for j in xrange(len(all_w) - 1):        # -1 because the last word has nothing after it
            if dist_w[i] == all_w[j]:
                A[i, dist_w.index(all_w[j+1])] += 1
                count += 1
               
        for k in xrange(n):
            if count > 0:
                A[i,k] = A[i,k] / count         # replace the 'hits' with the probability (ex 5 -> 5/10 = .5)
    

    return A


def processChain(A, dist_w):
    weightlist = []     # will contain a list of weights to choose from
    n = len(dist_w)

    # first choose a starting word randomly
    rindex = [random.randint(0,n-1)]
    start = dist_w[rindex[0]]
    print start

    for i in xrange(50):           # chain 10x
        # pick our next state
        rindex = weightedPick([A[rindex[0],e] for e in xrange(n)], 1)
        print dist_w[rindex[0]]

# use numpy functions to make a weighted random selection
# returns indexs of choices
def weightedPick(weights, nPicks):
    t = np.cumsum(weights)
    s = np.sum(weights)
    return np.searchsorted(t,rand(nPicks)*s)




if __name__ == '__main__':
    main()



























