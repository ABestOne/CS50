def main():
    time_number = convert(input('Time Now:').strip())
    if 7 <= time_number <= 8:
        print('breakfast time')
    elif 12 <= time_number <= 13:
        print('lunch time')
    elif 18 <= time_number <= 19:
        print('dinner time')

def convert(time):
    hours, minutes = time.split(":")
    time_number = int(hours) + int(minutes) / 60
    return time_number
if __name__ == "__main__":
    main()
