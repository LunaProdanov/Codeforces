k, n, w = map(int,input().split())
for i in range(1, w + 1):
 a = k * (w * (w + 1)) / 2
 b = a - n
if b > 0:
 print(int(b))
if b <= 0:
 print(0)
