day = 9

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid Input! Enter between 1-7")

choice = 2

match choice:
    case 1 | 2 | 3 | 4 | 5 :
        print('Weekdays')
    case 6 | 7 :
        print('Weekend')