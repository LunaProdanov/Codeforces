n, k= map(int,input().split())
counter = 0
arr = list(map(int,input().split()))
for x in arr:
 if x >= arr[k-1] and x > 0:
  counter += 1
print(counter)

