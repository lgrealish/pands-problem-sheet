# bank.py
# Author: Linda Grealish
# This program adds 2 money amounts as input by the user, and prints out the    
# answer with a € symbol and decimal point
# week 2 task

import math

# user prompted to input an amount in cent
amount1 = int(input('Please enter amount1 (in cent):'))
# user prompted to input a second amount in cent
amount2 = int(input('Please enter amount2 (in cent):'))

# the sum function adds the 2 amounts input, divides the total by 100 to 
# convert to € and cent and returns the amount as a floating number
#sum = (((amount1 + amount2) // 100)+((amount1 + amount2) % 100))
sum =(amount1 + amount2)

# using floor division operator to extract the eoru value
euro =(sum //100)
# using the modulo operator to extract the cent value
cent =(sum % 100)

print (f"The sum of these is €{euro}.{cent}")