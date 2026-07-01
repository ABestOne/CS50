input_string = input('Greeting:').lower().strip()
if input_string.startswith('hello'):
    print('$0')
elif input_string.startswith('h'):
    print('$20')
else:
    print('$100')
