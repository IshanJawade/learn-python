import mymodule as mymod 

print('name: ', mymod.__name__)
print('file: ', mymod.__file__)

modules_dir = dir(mymod)
for mod in modules_dir:
    print(mod)


print(mymod.cal_average(5, 10))
print(mymod.addition(5, 10))

print('ID : ', mymod.user1['userId'])
print('Username : ', mymod.user1['userName'])
print('Email : ', mymod.user1['userEmail'])
print('Phone : ', mymod.user1['userPhone'])
print('Age : ', mymod.user1['userAge'])
print('Verified : ', mymod.user1['status'])