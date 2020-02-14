from math import sin,cos,pi

#Begin
print("This is for Converting Polar Coordinates to Cartesian!")

#Inputs radius & degrees
print("Enter r:")
r=float(input())
print("Enter theta in degrees:")
d=float(input())

#Declaration of statements 

theta = d*pi/180
x= r*cos(theta)
y= r*sin(theta)

# Print statement 
print ("x=",x, "y=",y)