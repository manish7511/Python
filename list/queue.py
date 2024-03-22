# Queue is a linear data strcture.
# stores items in first in first out(FIFO) manner

#  queue operations

# 1.Enqueue:Adds an item to the queue.
# 2.Dequeue:Removes an item from the queue.
# 3.front:get the front item from queue.
# 4.Rear: get the front item from queue.


l=[]
while True:
  c=int(input('''

              1 push element
              2 pop first element
              3 front element
              4 last element
              5 display stack
              6 exit


'''))
  if c==1:
    n=input("enter the value")
    l.append(n)
    print(l)
  elif c==2:
    if len(l)==0:
      print("empty stack")
    else:
      del l[0]
     
      print(l)
  elif c==3:
    if len(l)==0:
      print("empty queue")
    else:
      print("first queue value",l[0])
  elif c==4:
    if len(l)==0:
      print("empty queue")
    else:
      print("last queue value",l[-1])
  elif c==5:
    print("Display queue",l)
  elif c==6:
    break
    
