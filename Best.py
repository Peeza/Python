from scipy.optimize import curve_fit
from scipy.stats import chi2
import numpy as np
import matplotlib.pyplot as plt

#X,Y Data & Y Error
xdata = [0,2,3,4,5]
ydata = [0,4,11,14,23.5]
yerr = [1,2,1,1.5,2.5]

#def function to use curve_fit the function is the line equation
def func(x,a,b):
    return a + b * x

#y array for the for loop
y = [0,0,0,0,0]

#the use of curve_fit into the variables line and var
line, var = curve_fit(func,xdata,ydata, sigma = yerr )
#var was 2 arrays while line was only 1
print("a = \n",line[0],"+-",var[0][0])
print("b = \n",line[1],"+-",var[1][1])

#for loop to get the 5 values for y[i]
for i in range(5):
    y[i] = line[0]+line[1]*xdata[i]


#write the value for chi^2 minimum 6.76
#the higher chi^2 is the worse the fit
chi = 0
for i in range(5):
     chi = chi+((ydata[i]-y[i])/yerr[i])**2
print("Chi2 = ",chi)

#the critical value of chi with 3 degrees of freedom
crit = chi2.ppf(0.99,3)
print("Critical value: ",crit)

#plots
plt.plot(xdata,ydata)#get a line between the points
plt.scatter(xdata,ydata)#get the points
plt.plot(xdata,y)#plot for the curve_fit
plt.errorbar(xdata,ydata,yerr, fmt = 'x')#graphing the yerr which was given 
plt.xlabel("X")
plt.ylabel("Y")
plt.show()