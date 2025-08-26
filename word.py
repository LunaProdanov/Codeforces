s = input()
a = 0
b = 0
for x in s:
 if x.isupper():
  a = a + 1

for x in s:
 if x.islower():
  b = b + 1

if a > b:
 print(s.upper())

if b > a:
 print(s.lower())

if a == b:
 print(s.lower())


