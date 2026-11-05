# Positional Arguments 
def positionalArg(name, lastname, city):
    print('Welcome ', name,' ', lastname, ' to the city of ', city)

positionalArg('Ishan', 'Jawade', 'fullerton')
positionalArg('Fullerton', 'Jawade', 'Ishan')

# Arguments with keywords
def keywordArg(name, lastname, city):
    print('Welcome ', name,' ', lastname, ' to the city of ', city)

keywordArg(city='Fullerton', name='Ishan', lastname='Jawade')

#  Unexpected arguments 
def listArguments(*arg):
    print("First argument:", arg[0])
    print("Second argument:", arg[1])
    print("Third argument:", arg[2])
    print("All argument:", arg)

listArguments('ishan', 23, True)

# Combination 
def GreetNewEmployees(greetings, *names):
    print('Greetings: ', greetings)
    print('Names: ', names)

    for name in names:
        print(greetings, name)

GreetNewEmployees('Welcome', 'Ishan', 'Abhishek', 'Puppy', 'Cyndrela')

# Lambda functions
sum = lambda a, b, c : a + b + c
print('Answer for for lambda function: ', sum(89, 65, 33))

# Generator function
def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)