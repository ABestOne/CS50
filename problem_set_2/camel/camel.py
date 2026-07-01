""" import string
string_name = input('input').strip()
for str in string_name:
    if str in string.ascii_uppercase:
        print('_' + str.lower(),end="")
    else:
        print(str, end="")
 """
string_name = input('input').strip()
for str in string_name:
    if str.isupper():
        print('_' + str.lower(), end="")
    else:
        print(str, end="")
