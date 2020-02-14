
# Initial Height

print("What's the initial height of the ball in meters?")
h = float(input())

#How long the ball is in the air!
print("How long was the time interval for the ball?") 
t = int(input())

s = (9.8*t**2) /2 # 1/2gt^2 Formula!

#Result of math!
print("The height of the ball is",h-s, "meters")

#Just letting the user know if its negative, somethings wrong w/  the time interval.
print("If the value is negative it has passed through the ground.") 

