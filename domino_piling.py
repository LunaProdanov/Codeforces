m, n = map(int,input().split())
x = m * n
if x % 2 == 0:
 print(int(x / 2))
else:
 print(int((x - 1) / 2))
 
