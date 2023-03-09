# collatz.py
# Author: Linda Grealish
# This program asks the user to input any positive integer
# and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and, 
# if it is even, divide it by two, but if it is odd, multiply it by three and add one
# week 4 task


# user prompted to input a positive integer
number = int (input("Enter a positive integer: "))
# if a negative integer is input user is prompted again
while number < 0:
    number = int (input("Enter a positive integer: "))
else:
   # check if the value entered does not equal 0
    if number >= 0:
        # inspiration for lines 21 to 38 was taken from educative.io
        def collatz(number):
            # an empty list to store all the sequence values
            lst=[]
            lst.append(number)
            # while loop first checks if the number is not equal to 1 
            while(number!=1):
                # checks to see if number is odd or even
                if(number%2==0):
                    # if number is even then the number is divided by 2 and appended to the list
                    number=number//2
                    lst.append(number)
                else:
                    # if number is odd then the number is multiplied by 3, add one and result
                    # is appended to the list
                    number=number*3+1
                    lst.append(number)
            print(lst)
        collatz(number)

    