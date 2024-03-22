# mutable [] seprated by comma[1,2,3,4,5]
# indexing are allowed and slicing also

l=[1,2,3,4,5]
print(type(l))

print(l[2])

l=[1,2,3,[4,5,6]]
# index only 3
print(l[3][1])

# mixed data types

l=[2,3,"hello",[3,4,5,6]]
print(l[2])
print(l[-2])

print(l[0:2])

l=[9,8,7,6,5]
print(l[0::2])

print(l[-1::-2])

list=["manish",25,35,40,[30,"sinku"]]
print(list[1:])
l=[10,20,30,40,50]
print(l[-1::-2])