# Markov-Literature
Creates a Markov model of words from text documents.
INPUT
Text document.  

PROCESSING
1) Parse the text file and clean it of any special characters and deal only with the words.

2) Create a Markov Model from the words.  For each word we want to know the frequency of each following word (1 word deep) in the entire text.  

For example, the word "apple" in a given text will be found to have the words "in", "was", "will", and "master" following it.  We find that "in" followed the word "apple" 3 times.  We find "was" follows 2 times, "will" follows 4 times, and "master" follows 1 time.  So, of the words that follow we have about a 30% change of "in", 20% of "was", 40% of "will", and 10% of "master".  

3) Build our chain.  Using our model we initially select a word at random and continue selecting words for an arbitrary amount of time (currently hard-coded at 50 words).  The next word selected is chosen at random from the weighted distrobution provided by the model.

Imports: numpy, sys, random

For the examples contained I took a pdf of 'The Old Man and the Sea' by Ernest Hemingway and 'One Flew Over the Cuckoo's Nest" by Ken Kesey and copy/pasted the content into a text file.  The text file was placed in the directory 'inputs/' and our application 'markov.py' has a variable 'filename' that contains the name of the file to read.  Output goes to stdout.  The output files in the directory 'outputs/' were created with CLI redirection.  
