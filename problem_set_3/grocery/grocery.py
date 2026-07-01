shopping_list = {}
while True:
    try:
        shop_item = input().strip().upper()
    except EOFError:
        break
    if shopping_list.get(shop_item, None) is None:
        shopping_list[shop_item] = 1
    else:
        shopping_list[shop_item] += 1
for item in sorted(shopping_list):
    print(f"{shopping_list[item]} {item}")
