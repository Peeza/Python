import numpy as np
import matplotlib.pyplot as plt
from pylab import scatter,xlabel,ylabel,xlim,ylim,show
import matplotlib.mlab as mlab

N = 10 #Number of uniform random samples
a = 10000 #number of samples
SUM = [] #Placeholder list to be filled with sums of samples

for x in range(0,a): #for loop to gather samples
    i = np.random.uniform(0,2,N)
    SUM.append(sum(i)) #Summing all random samples and putting them into SUM list

mu = np.mean(SUM) #Calculating mean of sums
sigma = np.std(SUM) #calculating standard deviation
median = np.median(np.sort(SUM)) #Calculating median


#printing all results
print("Mean =", mu)
print("Standard Deviation =", sigma)
print("Median =", median)
print("Confidence Interval:", median-sigma, "to", median+sigma)

#printing graph with gaussian overlay
s = np.linspace(mu + sigma,mu - sigma, N)
plt.hist(SUM, 100, normed=1)
plt.plot(s, mlab.normpdf(s, mu, sigma))
xlabel("Sum of Variables")
ylabel("PDF of Sum")
plt.show()
