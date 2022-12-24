#tasks from: https://younglinux.info/python/builtin-functions
#task 1
while True:
    symbol = int(input())
    if symbol == 0:
        break
print(chr(symbol))

#task 2
input()
if len(s)>10:
    print("String is too long")
else :
   for i in range (len(s),10):
      s+="*"
   print(s)

#task 3
arr = []
for i in range(6):
    arr.append(float(input("Enter real numbers -> ")))
 
maxx = arr[0]
minn = arr[0]
 
for i in arr:
    if maxx > i:
        maxx = i
    else:
        minn = i
 
print(f"Max: {round(maxx, 2)} | Min: {round(minn, 2)}")
