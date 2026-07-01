def main():
    string_1 = input()
    print(convert(string_1))

def convert(string_2 = ''):
    string_2 = string_2.replace(':)', '🙂')
    string_2 = string_2.replace(':(', '🙁')
    return string_2

main()
