# plottask.py
# Author: Linda Grealish
# This a histogram of a normal distribution of a 1000 values with a mean of 5 
# and standard deviation of 2, and plot of the function  h(x)=x3 in the range [0, 10], 
# week 8 task

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

mean_x = 5
std_x = 2
values_x = 1000

x = np.random.normal(mean_x, std_x, size=values_x)
sns.histplot(x, color='r')

h = x^3
plt.plot (x, h, "r.", label="h(x) = x^3")

plt.show()