# stack is a liner data structure

#  stores in a Last-in/first-out or first-in/last-out


# stack operations

# 1.push-> inserting an elements
# 2.pop->deletion an element
# 3.peek->display he last element
# 4.display->display list


l=[]
while True:
  c=int(input('''

              1 push element
              2 pop element
              3 peek element
              4 display stack
              5 exit


'''))
  if c==1:
    n=input("enter the value")
    l.append(n)
    print(l)
  elif c==2:
    if len(l)==0:
      print("empty stack")
    else:
      p=l.pop()
      print(p)
      print(l)
  elif c==3:
    if len(l)==0:
      print("empty stack")
    else:
      print("last stack value",l[-1])
  elif c==4:
    print("display stack",l)
  elif c==5:
    break
