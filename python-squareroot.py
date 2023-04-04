# weekday.py
# Author: Linda Grealish
# This program takes a positive floating-point number as input 
# and outputs an approximation of its square root
# week 6 task

n = float (input("Enter a positive number: "))
#format_n = "{:.2f}".format(n)
approx_sqrt = 0.5*n
print(f"Approximate square root of {n} is : {approx_sqrt}")


def newtonSqrt(n):
    approx=0.5*n
    better=0.5*(approx+n/approx)
    while better!=approx:
        approx=better
        better=0.5*(approx+n/approx)
    return approx


result = {newtonSqrt(n)}


print (f"The square root of {n} is : ", round (newtonSqrt(n),3) )


