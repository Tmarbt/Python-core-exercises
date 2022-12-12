task from: https://younglinux.info/python/local-global
#1st task
result = 0
p = 3.14
def cylinder(): 
    h = int(input("Insert the hieght of cylinder: "))
    r = int(input("Insert the radius of the circle: "))
    global result
    result = 2*p*r*h
def circle():
    r = int(input("Insert1 the radius of the circle: "))
    global result
    result = (p * r)**2 * 2 + result
a = int(input("1-the area of the lateral surface of the cylinder, 2- total area of cylinder: "))
if a == 1: 
    cylinder()
elif a == 2:
  circle()
print("Area: %.2f" % result)
