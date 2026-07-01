name_list = []
start_str = 'Adieu, adieu, to '
try:
    while True:
        input_name = input('Name: ')
        name_list.append(input_name)
except EOFError:
    pass
while True:
    if len(name_list) > 2:
        start_str += name_list.pop(0) + ', '
    elif len(name_list) == 2 and len(start_str.split(','))!= 3:
        start_str += name_list.pop(0) + ', and '
    elif len(name_list) == 2 and len(start_str.split(',')) == 3:
        start_str += name_list.pop(0) + ' and '
    elif len(name_list) == 1:
        start_str += name_list.pop(0)
        break

print()
print(start_str)
