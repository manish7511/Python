# del

l=[20,30,40,50]
del l[1]
print(l)

# pop() pass index value

list=[10,20,30,40]
print(list.pop(2))
print(list)

# remove() pass value of list for remove
list1=[60,70,80,90]
list1.remove(70)
print(list1)

# clear() clear element and put the value through indexing

list2=[60,70,80,90,100]
list2[0]=50
print(list2)

# insert()  put value of indexing postion
list3=[11,12,13,14,15,16]
list3.insert(0,10)
print(list3)

# append() put value of last postion
list4=[21,22,23,24,25]
list4.append(29)
print(list4)

z=[20,30,40]
x=[90,80]
z.append(x)
print(z)


# extend()
list5=[41,42,43,44,45]
list6=[50,60]
list5.extend(list6)
print(list5)