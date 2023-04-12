# es.py
# Author: Linda Grealish
# This program reads in a text file called week07.txt and outputs the number of e's it contains
# week 7 task


# importing sys so it can take in a command line argument
import sys

# sys.argv[1] allows the user to input a file name from the command line rather than 
# hardcoding the name into the coding program
filename = sys.argv[1]

with open(filename, 'r') as f:
    es = f.read()
    # counting "e" character in the file
    count = es.count("e") + es.count("E")

    print (f"There are {count} e's in that file")