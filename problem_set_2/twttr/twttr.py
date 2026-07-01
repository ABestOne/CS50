input_string = input('string').strip()
replace_alp = ['a','e','i','o','u','A','E','I','O','U']
for str in replace_alp:
    if str in input_string:
        input_string = input_string.replace(str, '')
print(input_string, end='')


