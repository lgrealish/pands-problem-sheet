# weekday.py
# Author: Linda Grealish
# This program outputs whether today is a weekday or weekend.
# week 5 task

# use Python's datetime module
from datetime import datetime

 # use the datetime function to determine todays date and the corresponding 
 # day of the weekday list which contains 7 items
weekday = datetime.today().weekday()
 
 # if the weekday is between 1 and 5 then it is a weekday
if weekday < 5:
    print("Yes, unfortunately today is a weekday")
# if the weekday is 5 or 6 on the list then it is the weekend.
else:  
    # 5 Sat, 6 Sun
    print("It is the weekend, yay!")