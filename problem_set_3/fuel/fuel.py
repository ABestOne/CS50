def main():
    x, y = read_two_num()
    cul(x, y)
def read_two_num():
    while True:
        try:
            x, y = input("Fraction: ").strip().split("/")
            if int(x) > int(y) or int(y) <= 0 or int(x) < 0:
                continue
            return int(x), int(y)
        except (ValueError, ZeroDivisionError):
            pass
def cul(x, y):
    a = round((x / y) * 100)
    if  a <= 1:
        print('E')
    elif a >= 99:
        print('F')
    else:
        print(f'{a}%')
if __name__ == '__main__':
    main()



