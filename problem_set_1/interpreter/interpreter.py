x,z,y = input('Express:').split(' ')
x = int(x)
y = int(y)
match z:
    case '+':
        result = x + y
    case '-':
        result = x - y
    case '*':
        result = x * y
    case '/':
        if y == 0:
            result = 'Error: Division by zero'
        else:
            result = x / y
print(f"{result:.1f}")
