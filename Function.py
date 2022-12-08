# tasks from: https://younglinux.info/python/function
#1st task
def positive():
print("Positive")
def negative():
print("Negative")

def test():
number = int(input("Enter an enteger: "))
if number > 0:
positive()
else:
negative()
test()