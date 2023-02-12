# bank.py
# Author: Linda Grealish
# This program adds 2 money amounts as input by the user, and prints out the    
# answer with a € symbol and decimal point
# week 2 task

amount1 = int(input('Please enter amount1 (in cent):'))

amount2 = int(input('Please enter amount2 (in cent):'))

sum = float((amount1 + amount2) / 100)

print (f"The sum of these is €" + format(format(sum, ',.2f')))