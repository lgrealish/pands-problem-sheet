# plottask.py
# Author: Linda Grealish
# This a histogram of a normal distribution of a 1000 values with a mean of 5 
# and standard deviation of 2, and plot of the function  h(x)=x3 in the range [0, 10], 
# week 8 task

# import the modules needed - numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt

# first we define the parameters for the histogram, mean, standard deviation and values
mean_x = 5
std_x = 2
values_x = 1000

# normData using the random generator from numpy to create a histogram of a normal distribution
normData = np.random.normal(mean_x, std_x, size=values_x)
# use plt.hist from matploylib.pyplot to plot the parameters 
plt.hist(normData, color = "b",label= "Normal Distribution")

# define the variable 'xpoints' in the range [0,10]
xpoints = np.array(range(0,10))
# define ypoints as xpoints^3
ypoints = xpoints**3
# use plt.plotfunction to display line plot of 'ypoints'
plt.plot(ypoints, color ="r", label = ("x^3"))

# assign plot title, labels to x and y axis and add legend
plt.title ("Week 8 task")
plt.xlabel ("x value")
plt.ylabel ("Function")
plt.legend()

# using plt.show() to return visual of the above input data
plt.show()