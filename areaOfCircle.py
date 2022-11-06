from math import pi

def calculateRadius():
    radius = float(input ("Enter the radius of the circle : "))
    print ("The area of the circle with radius " + str(radius) + " is: " + str(pi * radius**2))


calculateRadius()
