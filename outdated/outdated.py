def check(month, day, year):
    return (month > 0 and month <= 12) and (day > 0 and day <= 31)

months = [
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
    date = input("Date: ").strip()
    try:
        month, day, year = map(int, date.split('/'))
    except:
            try:
                month = int(months.index(date[0:-8])) + 1
                day = int(date[-7:-6])
                year = int(date[-4:])
            except:
                pass
            else:
               if check(month, day, year):
                    break
    else:
        if check(month, day, year):
            break



print(f"{year}-{month:02}-{day:02}")
