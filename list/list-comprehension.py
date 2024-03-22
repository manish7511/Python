# List comprehension is an elegant way to define and create lists based on existing lists

#  list comprehension is generally more compactt and faster than normal functions and loops for creating lists.

#   syntax

#   [expressions for item in list]

l=[]
for a in range(1,11):
  l.append(a)
print(l)

#  list comprehension

n=[h for h in range(1,31) if h%2==0 ]
print(n)

s="hello"
d=[g for g in s]
print(d)