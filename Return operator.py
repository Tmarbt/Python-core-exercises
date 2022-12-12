#tasks from: https://younglinux.info/python/return
#1st task
def string():
        a = str(input('Write first word: '))
        b = str(input('Write second word: '))
        if any(char.isdigit() for char in a and b):
            return("Mistake, should be only letters")
        else:
            result = f'{a} {b}'
        return result
print(string())  

#2nd task
def numbers():
    number = float(input("Ente number here: "))
    if number == 0:
        return 0
    answer = 1
    while number != 0:
        answer *= number
        number = float(input("Ente number here: "))
    return answer
print(numbers())
    