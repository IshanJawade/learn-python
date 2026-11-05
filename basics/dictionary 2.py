car1 = {
    'brand' : 'bmw',
    'model' : 'f80 m3',
    'year' : 2015
}

car2 = {
    'brand' : 'nissan',
    'model' : 'skyline gtr v-spec',
    'year' : 2001
}

car3 = {
    'brand' : 'honda',
    'model' : 'civic si',
    'year' : 2023
}

inventory = {
    'car1000' : car1,
    'car1001' : car2,
    'car1002' : car3
}

# print(inventory)


# looping throught the inventory

for x, obj in inventory.items():
    print('x: ', x)
    for y in obj.items():
        print('y: ', y)
