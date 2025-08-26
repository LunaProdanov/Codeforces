n = int(input())
counter = 0
for i in range(n):
 a = input()
 if "--" in a:
   counter -= 1
 if "++" in a:
   counter +=1
print(counter)
 

