from pylab import scatter,xlabel,ylabel,xlim,ylim,show
from numpy import loadtxt
#loading the stars txt file w/ values
data = loadtxt("stars.txt",float)
x = data[:,0]
y = data[:,1]
scatter(x,y)
xlabel("Temperature")
ylabel("Magnitude")
xlim(0,13000)
ylim(-5,20)
#displaying the graph 
show()
