# tradistional way
file = open("text.txt", "r")
contents = file.read()
file.close()

print(contents)

for i in items:
    print(i, end=", ")
print()

#### "with" context handler no need to close the file

# reading a file
with open("groceries.txt", "r") as f:
    print(f.read())

# writing a file if not available creating new file
with open("groceries.txt", "w") as f:
    f.write("honye\nmilk\ncookie\nbananas")

# appending into laready available file
with open("groceries.txt", "a") as f:
    f.write("\napple")
