d={"fname":"manish","lname":"kumar","age":23,"course":"btech"}

c=d.get('course')
print(c)

for a in d.keys():
  print(a)

for a in d.values():
  print(a)

for a,b in d.items():
  print(a,b)

print()

#  delete in dict
del d["fname"]
print(d)

a=d.pop('age')
print(a)
print(d)


a=dict(courses="python",fees=3500,)
print(a)

# update

d={
  "courses":"python",
  "fees":8000,
  "duration":"1 years"
}
d.update({'fees':10000})
print(d)

d['desc']="this is the python"
print(d)