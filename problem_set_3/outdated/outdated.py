month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    data_string = input('Data: ')
    if '/' in data_string:
        month, day, year = data_string.split("/")
        try:
            month = int(month)
            day = int(day)
            year = int(year)
        except ValueError:
            continue
        if 1 <= month <= 12 and 1 <= day <= 31:
            print(f"{year}-{month:02d}-{day:02d}")
            break
    else:
        if len(data_string.split(',')) == 2:
            month, day, year = data_string.split(" ")
            if month in month_list:
                month = month_list.index(month) + 1
                day = int(day.strip(","))
                year = int(year)
                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{year}-{month:02d}-{day:02d}")
                    break

