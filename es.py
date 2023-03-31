# es.py
# Author: Linda Grealish
# This program reads in a text file and outputs the number of e's it contains
# week 7 task


import sys
filename = sys.argv[-1]


# explicit function to return the letter count
def letterFrequency(fileName, letter):
	# open file in read mode
	file = open(fileName, 'r')

	# store content of the file in a variable
	text = file.read()

	# using count()
	return text.count(letter)


# call the function and display the letter count
print(letterFrequency('week07.txt', 'e'))
