# This file contains utility methods used to help clean up 
# the contents of the rest of the project's code.

import os
import sys
import re


# This method's job is to look to the input directory for 
# the specified file name and return the full path name
def getPath(filename):
    cwd = os.path.dirname(__file__)     # path to cwd
    infile_relitive = '../inputs/inputFiles_raw/' + filename
    inputfilepath = os.path.join(cwd, infile_relitive)
    return inputfilepath



# This method expects the full path to the raw input file
# returns the list of all words in the input file
def getWords(infile_path):
    allwords = []

    with open(infile_path, 'r') as infile:
        validWord = re.compile("[A-Za-z]+")         
        for line in infile:
            words = line.split()                # seperate out strings by spaces
            
            for string in words:
                word = ''.join(c for c in string if c.isalnum())     # remove non-alphanumeric characters, join string
                if validWord.match(word):       # use words composed of only letters
                    allwords.append(word)       # add to the collection (list)

    return allwords



# given a list of words this method returns the list of 
# distinct words
def uniqueafy(bunchowords):
    setofwords = set(bunchowords)
    listofuniquewords = list(setofwords)
    return listofuniquewords



