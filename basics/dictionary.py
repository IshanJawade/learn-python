record = {
    "name" : "ishan",
    "email" : "ishanjawade@gmail.com",
    "age" : "34"
}

print(record)

x = record["name"]

name = record.get("name")

print(name, x)

print(record.keys())

newName = "Advait"

record["name"] = newName

print(record)

# print values
for i in record:
    print(record[i])

# print values (2)
for i in record.values():
    print(i)

# print keys
for i in record.keys():
    print(i)

# print both keys and vlues
for i, j in record.items():
    print("\""+ i + "\"" + " : " + "\"" + j + "\"")