a = input()
b = input()
a = a.lower()
b = b.lower()
counter = 0
if a < b:
 counter  -= 1
if a > b:
 counter += 1
if a == b:
 counter = 0
print(counter)

