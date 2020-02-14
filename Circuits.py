from numpy import array
from numpy.linalg import solve
import math
from numpy import pi
import numpy as np

np.set_printoptions(suppress=True)

V = 100
R1 = R2 = 1000
C = 10**(-6)
L = 1
w = 1000
I1 = I2 = I3 = 0

#Prompt user for type of circuit
x = str(input("Capacitor(C) or Inductor(L)?\n"))

#Solutions to be solved
print("\nLinear system to solve:\n")
print("\t(1+0j) I1 = 0j(-1+0j) I2 = 0j(-1+0j) I3 = 0j \n")
print("\t(1000+0j) I1 = (100+0j)(1000+0j) I2 = (100+0j)0j I3 = (100+0j)\n")
print("\t(1000+0j) I1 = (100+0j)0j I2 = (100+0j)-1000j I3 = (100+0j)\n")

Y = R1*((R2*w*C)*(R2*w*C)+1) - 1j*(R2*R2)*w*C + R2

#Capacitors
I1_1 = (2*V)/Y
I2_1 = I1_1*((-1j)/((R2*w*C) - 1j))
I3_1 = I1_1 - I2_1

#Inductors (Magnitude and Angle)
I1_2 = np.linalg.norm(I1_1)
I1_phase = np.angle(I1_1) * (180/pi)
I2_2 = np.linalg.norm(I2_1)
I2_phase = np.angle(I2_1) * (180/pi)
I3_2 = np.linalg.norm(I3_1)
I3_phase = np.angle(I3_1) * (180/pi)

#Part A
if(x=='C'):
    print("Solution:\n")
    print("I1 =", np.round(I1_1, 4))
    print("I2 =", np.round(I2_1, 4))
    print("I2 =", np.round(I3_1, 4))

#Part B
elif(x=='L'):
    print("Solution:\n")
    print("I1 =", round(I1_2, 3), "A with phase =", round(I1_phase, 3), "degrees")
    print("I2 =", round(I2_2, 3), "A with phase =", round(I2_phase, 3), "degrees")
    print("I3 =", round(I3_2, 3), "A with phase =", round(I3_phase, 3), "degrees")