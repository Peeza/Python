from math import exp
print("Enter KT:")

#Set Values
KT = float(input())
x = 1000
Beta = 1/KT
s = 0
z = 0
#Loop for math
for n in range(x):
	e = n + 0.5
	weight = exp(-Beta*e)
	s += weight*e
	z += weight

print("The average energy for KT =" , KT, "is", round(s/z, 5))
