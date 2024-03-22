# Nested disctionary means putting dicionary inside anoher dictionary
# it is a collection of ditionaries into single dictionary

courses={
  'php':{'duration':'3 months','fees':'14000'},
  'python':{'duration':'4 months','fees':'16000'},
  'java':{'duration':'7 months','fees':'18000'},
  'sql':{'duration':'2 months','fees':'24000'}

}
courses['java']['fees']=20000
print(courses['python']['fees'])

for k,b in courses.items():
  print(k,b['duration'],b['fees'])