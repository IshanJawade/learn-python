# ArrayList
# allows duplicate
# Keeps order
# Can modify anytime

fruits = ["apple", "banana", "cherry", "orange"]

print(type(fruits))
print(fruits)

print(fruits[2])

numList = [0, 1, 2, 3, 4, 5, 6, 7]

# for this slicing function count indices from 1 and exclude the given numebers 
print(numList[2:5])
print(numList[:4])
print(numList[3:])

# changing lists

fruits.append("mango")
print(fruits)

fruits[3] = "persimmon"
print(fruits)

# fruits[1:2:3] = ["blackcurrant", "watermelon", "water chesnut"]
# print(fruits, )

fruits.insert(2, "Puppy")
print(fruits)

# copy one list into another rippedFruits -> fruits
rippedFruits = ["guava", "papaya", "berry"]
fruits.extend(rippedFruits)
print(fruits)

del rippedFruits


# lopping into the list

# for loop
for i in range (len(fruits)):
    print(fruits[i])

# for each loop
for i in fruits:
    print(i)

# while loop 
i = 0
while i < (len(fruits)):
    print(fruits[i])
    i = i+1
