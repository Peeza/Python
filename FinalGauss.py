import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from math import pi
from pylab import scatter,xlabel,ylabel,xlim,ylim,show

#Mean
mu = 100         
sigma = 15
#Sample Number
N = 1000     
z = np.random.randint(1,10000, N)
x = np.linspace(mu - (3*sigma), mu + (3*sigma), N)
gaussian = np.random.normal(mu, sigma, N)

plt.plot(x, scipy.stats.norm.pdf(x, mu, sigma))
plt.hist(gaussian, 50, normed=1)
plt.show()

#Sorting Gussian Values
sorted_values = np.sort(gaussian)      
#Cal Lower Error
lower_error = np.median(sorted_values) - sorted_values[50]    
#Cal Upper Error
upper_error = np.median(sorted_values) - sorted_values[950]     

#Print all results
print("Length of the sorted values of the Gaussian distribution:", len(sorted_values))                  
print("The lower 5% of the sorted:", 0.05*len(sorted_values))
print("The upper 5% of the sorted:", 0.95*len(sorted_values))
print("The median of the sorted:", 0.50*len(sorted_values))
print("The lower 5% is at value", sorted_values[50])
print("The upper 5% is at value", sorted_values[950])
print("The median of the sorted is", np.median(sorted_values))
print("The median with error is", np.median(sorted_values), "+", lower_error, "or", upper_error)