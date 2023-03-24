# weekday.py
# Author: Linda Grealish
# This program takes a positive floating-point number as input 
# and outputs an approximation of its square root
# week 6 task

n = float (input("Enter a positive number: "))
#format_n = "{:.2f}".format(n)
approx_sqrt = 0.5*n
print(f"Approximate square root of {n} is : {approx_sqrt}")

#def newtonSqrt(n, base):
    #approx_root = 0.5 * n
    #for i in range(base):
       # betterapprox = 0.5 * (approx_root + n/approx_root)
        #approx_root = betterapprox
   # return betterapprox




def newtonSqrt(n):
    approx=0.5*n
    better=0.5*(approx+n/approx)
    while better!=approx:
        approx=better
        better=0.5*(approx+n/approx)
    return approx


result = {.2f}.{newtonSqrt(n)}
#print (f"The square root of {n} is :{newtonSqrt(n)}")

print (f"The square root of {n} is : " + format(result, ',.2f'))

#print((round(n,2) "The square root of {n} is : {newtonSqrt(n)}"))
