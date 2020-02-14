from numpy import ones,copy,cos,tan,pi,linspace

#Creating & defining gauss cause importing it wasn't working out. 


def gaussxw(N):

    # Initial approximation
    a = linspace(3,4*N-1,N)/(4*N+2)
    x = cos(pi*a+1/(8*N*N*tan(a)))

    # Finding roots using Newton's method
    epsilon = 1e-15
    delta = 1.0
    while delta>epsilon:
        p0 = ones(N,float)
        p1 = copy(x)
        for k in range(1,N):
            p0,p1 = p1,((2*k+1)*x*p1-k*p0)/(k+1)
        dp = (N+1)*(p0-x*p1)/(1-x*x)
        dx = p1/dp
        x -= dx
        delta = max(abs(dx))

    # Calculate the weights
    w = 2*(N+1)*(N+1)/(N*N*(1-x*x)*dp*dp)

    return x,w

def gaussxwab(N,a,b):
    x,w = gaussxw(N)
    return 0.5*(b-a)*x+0.5*(b+a),0.5*(b-a)*w

# Function  
def f(x):
    return x**4 + 2*x + 1
    
# Getting N input from user
N = int(input("Enter N:\n"))
a = 0.0
b = 2.0

x,w = gaussxw(N)
xp = 0.5*(b-a)*x + 0.5*(b+a)
wp = 0.5*(b-a)*w

#integration
s = 0.0
for k in range(N):
    s += wp[k]*f(xp[k])

print("The integration is", round(s,5))