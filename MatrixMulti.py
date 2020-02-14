from numpy import array, zeros, dot
import time

#Matrix Array (Wasnt sure how to make it an input)
N = 5
A = array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])
B = array([[2, 3, 4, 5, 6], [2, 3, 4, 5, 6], [2, 3, 4, 5, 6], [2, 3, 4, 5, 6], [2, 3, 4, 5, 6]])
C = zeros([N,N],int)

start = time.clock()
#Matrix Multi
for i in range(N):
    for j in range(N):
        for k in range(N):
            C[i,j] += A[i,k]*B[k,j]
end = time.clock()
#matrix multi print
print("A =", A)
print("B =", B)
print("C =", C)

#Time
start2 = time.clock()
d = dot(A,B)
end2 = time.clock()
#Time 
time = (end2 - start2)
print(d)
print("time =", time)