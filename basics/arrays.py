from array import array

val=array('i', [1,2,3,4,5,6,7])

char=array('w', ['a','b','c','d','e','f'])

print(char)

# copy of val
copyVal = array(val.typecode, (a for a in val))
print(copyVal)

# squars of values in val
squr = array(val.typecode, (a**2 for a in val))
print(squr)

# -------- Looping ---------

# for loop
for i in squr:
    print(i, end=" ")
print()

# while loop
i = 0
while i < len(val):
    print(val[i], end=" ")
    i=i+1
print()
