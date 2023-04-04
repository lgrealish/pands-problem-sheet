# python-squareroot.py
# Author: Linda Grealish
# This program takes a positive floating-point number as input 
# and outputs an approximation of its square root using Newtons Method
# week 6 task
# https://stackoverflow.com/questions/28733759/python-square-function-using-newtons-algorithm
# https://www.youtube.com/watch?v=xdlIFw5EM4w

# set input to float type
n = float (input("Enter a positive number: "))

# if n < 0:
    #print ("Try again! \nEnter a positive number: ")


def newtonSqrt(n):
    # start by assuming approx square root is half the number
    approx=0.5*n
    # find a better value by using the following calculation
    better=0.5*(approx+n/approx)
    # while the better value found is not equal to the approxassumed approx then 
    # recalculate the better value using calculation better=0.5*(approx+n/approx)
    while better!=approx:
        approx=better
        better=0.5*(approx+n/approx)
    return approx

result = {newtonSqrt(n)}

# print the reult and round the result to 3 decimal places using the round() function
print (f"The square root of {n} is : ", round (newtonSqrt(n),3) )



