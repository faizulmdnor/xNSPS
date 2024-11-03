from math import pi

print("Pi is equal to : ", pi)
print("Area of Circle = Pi*r^2")

r = float(input("Input the radius(r) of the circle : "))
l = float(input("Panjang silinder? : "))
print("\tThe area of the circle with radius " + str(r) + " is: " + str(pi * r ** 2))
print("\tThe area of the circle with radius {0} is: {1}".format(str(r), str(pi * r ** 2)))
x = str(r)
y = str(pi * r ** 2)
print("\tThe area of the circle with radius {0} is: {1}".format(x, y))
print("\nIsipadu silinder = Pi*r^2*l")
print("\tisipadu bagi silinder yang berjejari " + str(r) + " dan panjangnya " + str(l) + " is: " + str(pi * r ** 2 * l))
