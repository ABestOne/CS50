food_dict ={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total_money = 0
while True:
    try:
        food_name = input('Item: ').strip().lower().title()
    except EOFError:
        break
    flag = food_dict.get(food_name, -1)
    if flag == -1:
        continue
    else:
        total_money += flag
        print(f'Total: ${total_money:.2f}')
