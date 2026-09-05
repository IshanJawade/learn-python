# How to impliment queues in python

from collections import deque

# Initialize a queue
que = deque()
que2 : deque[int] = deque()     # typed 
print(type(que), type(que2))

# Putting things in the queue
que.append(10)  # bydefalut add from the right end
que.appendleft(5)   # specifically adds from the left

que2.append(13)
que2.append("apple")

print("que: ", que)
print("que2: ", que2)