# accounts.py
# Author: Linda Grealish
# This program reads in a 10 character account
# number and outputs the account number with
# only the last 4 digits showing
# week 3 task

account = input('Please enter 10 digit account number: ')

s = account[-4:].rjust(len(account), 'X') 
# splicing, python uses negative indes to start from the last item.  In this case -4 for last 4 digits  
# w3school.com tutorial provided inspiration for the use of rjust() function for right aligning a string

print(s)
