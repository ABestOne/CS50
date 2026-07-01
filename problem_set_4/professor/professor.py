import random

def main():
    answer_right = 10
    level = get_level()
    for _ in range(10):
        flag = 0
        x = generate_integer(level)
        y = generate_integer(level)
        for _ in range(3):
            try:
                answer_input = int(input(f'{x} + {y} = '))
            except (ValueError):
                print('EEE')
                flag += 1
                continue
            if answer_input != x + y:
                print('EEE')
                flag += 1
                continue
            else:
                break
        if flag == 3:
            answer_right -= 1
            print(f"{x} + {y} = {x + y}")
    print(f'Score: {answer_right}')

def get_level():
    while True:
        try:
            level = int(input('Level: '))
        except ValueError:
            continue
        if level in [1, 2, 3]:
            return level

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
