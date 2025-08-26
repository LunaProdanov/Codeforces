n, h = map(int,input().split())
niz = list(map(int,input().split()))
counter = 0
for x in niz:
 if x <= h:
  counter += 1
 if x > h:
  counter += 2
print(counter)
