x = int(input())
counter = 0
a = x // 5 
counter += a
b = x % 5
if b < 5 and b != 0:
 counter += 1
print(counter)
