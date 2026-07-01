need_money = 50
while need_money > 0:
    while True:
        print(f"Amount Due: {need_money}")
        input_coin = int(input('Insert Coin:'))
        if input_coin in [5, 10, 25]:
            break
    need_money -= input_coin
print(f'Change Owed: {abs(need_money)}')
