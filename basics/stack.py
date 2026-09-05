# How stack can be implemented in python

# Initializing Stack, Stack is a list 
stack : int = [10, 20, 30, 40 , 50]
print(stack)

# pop() removes the last element 
x : int = stack.pop()
stack.pop()

print(x)
print(stack)

# peek() in python you can iterate from the back with -1, -2, index numbers to -1 should be the top
top = stack[-1]
print(top)


