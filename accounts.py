# accounts.py
# Author: Linda Grealish
# This program reads in a 10 character account
# number and outputs the account number with
# only the last 4 digits showing
# week 3 task

account = input('Please enter 10 digit account number: ')

# add validation to make sure it's a 10 digit number - if length 
# of account number input does not equal 10 digits the user is prompted to input again.
while (len(account) != 10):
    account = input('Try again\nPlease enter 10 digit account number: ')
 
# if the input is the correct length the code below uses splicing 
# # python uses negative index to start from the last item.  In this case -4 for last 4 digits  
# w3school.com tutorial provided inspiration for the use of rjust() function for right aligning a string
 else:
    
s = account[-4:].rjust(len(account), 'X') 
print (s)

# as the code in line 17 simply replaces the last 4 dgigits in a string of integers this 
# code will work with any length of account number by also removing
# the validation in line 12 and 13.
