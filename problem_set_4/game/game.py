import random
def main():
    num_goal = obtian_num()
    compare(num_goal)
def obtian_num():
    while True:
        try:
            n = int(input('Level:'))
            if n > 0:
                break
        except ValueError:
            continue
    num_goal = random.randint(1, n)
    return num_goal
def compare(num_goal):
    while True:
        try:
            num_input = int(input('Guess:'))
            if num_input > 0:
                if num_input > num_goal:
                    print('Too large!')
                elif num_input < num_goal:
                    print('Too small!')
                else:
                    print('Just right!')
                    break
        except ValueError:
            continue
if __name__ == "__main__":
    main()
