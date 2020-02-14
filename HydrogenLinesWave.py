#Rydberg constant
R=1.097e-2
    #Array for m
for m in [1,2,3]:
    print("Series for m =",m)
    #Array for A
    for a in [1,2,3,4,5]:
        n = a + m
    
    #Formula
    beeplambda=R*((1/m**2-1/n**2))
    #Printed Result
    print(" ", 1/beeplambda," nm")

