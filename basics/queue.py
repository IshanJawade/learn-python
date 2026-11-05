# How to impliment queues in python

from collections import deque

# Initialize a queue
que = deque()
print(type(que))

# Putting things in the queue
que.append(10)  # bydefalut add from the right end
que.appendleft(5)   # specifically adds from the left
que.append("String")
# you can add anythin, no type checking 
user = {"name" : "someone", "age": 34}
que.append(user)

print("que: ", que)
