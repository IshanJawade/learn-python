
# def calculator():
#     ch = -1
#     while ch != 0:
#         print('Enter number infront of the operation')
#         print('1) Add \n 2) Sub 3) Mul \n 4) Div \n 0) Exit')
#         print('->', end=' ')
# calculator()

def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    if a > b:
        return a/b
    else:
        return b/a

num1 = 7; num2 = 89

print("Addition: ", add(num1, num2))
print("Subtraction: ", sub(num1, num2))
print("Multiplication: ", mul(num1, num2))
print("Division: ", div(num1, num2))