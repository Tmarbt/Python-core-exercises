#tasks from: https://younglinux.info/python/exceptions
#1st task
n1 = input("Please, write 1 value: ")
n2 = input("Please, write 2 value: ")
try:
    n1 = float(n1)
    n2 = float(n2)
    print(n1 + n2)
except ValueError:
    print(str(n1 + n2))
else:
    print(f"Correct, you insert both numbers {n1} and {n2}")
finally:
    print("Program completed")
