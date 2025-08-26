t= int(input())
for i in range(t):
 a = input()
 if len(a)> 10:
    x = a[0]
    y = len(a[1:-1])
    z = a[-1]
    print(x + str(y) + z)
 else:
    print(a)
