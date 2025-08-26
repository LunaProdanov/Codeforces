a, b= map(int,input().split())
counter = 0
if a * 3 > b * 2:
 counter += 1
elif a * 9 > b * 4:
 counter += 2
elif a * 27 > b * 8:
 counter += 3
elif a * 81 > b * 16:
 counter += 4
elif a * 243 > b * 32:
 counter += 5
elif a * 729 > b * 64:
 counter += 6
elif a * 2187 > b * 128:
 counter += 7
print(counter)

