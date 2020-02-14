#Defining the integral fcn
def f(x):
    return x**4+2*x+1
#Input for N Value
N = int (input("Enter your value for N: ")) 
#Range 0 to 2 being put & subtracted
a = 0.0 
b = 2.0
h = (b-a)/N

s = 0.5*f(a) + 0.5*f(b)
for k in range(1,N):
    s += f(a+k*h)
    #Printing Result
print(h*s)

