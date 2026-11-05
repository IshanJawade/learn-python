name = 'Ishan Jawade'
for i in name:
    print(i)

fruits = ['banana', 'apple', 'cherry', 'orange']
for fruit in fruits:
    print(fruit)
    for i in fruit:
        # print(i)
        for z in i:
            print(z)

# patterns 

for i in range(5):
    for j in range(i):
        print('*', end=' ')
    print('')


num = 10
for i in range(num):
    count = num-i
    for j in range(num):
        if count < 0:
            print('*', end=' ')
        else: 
            print('', end=' ')
        count -= 1
    print('')

for i in range(2, 21, 2):
    print(i, end=' ')
else:
    print('')

for i in range(5):
    # if i == 4:
    #     break
    print(i, end=' ')
else:
    print("Loop is over successfuly!")
print('Loop ran!')