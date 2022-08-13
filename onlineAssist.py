def main():


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
            m, d, y = date.split("/")
            if (int(m) > 0 and int(m) < 13) and (int(d) > 0 and int(d) < 32):
                break

        except:
            try:
                alt_m, alt_d, y = date.split(" ")
                for month in range(len(months)):
                    if alt_m == months[month]:
                        m = month + 1

                d = alt_d.replace(",", "")

                if (int(m) > 0 and int(m) < 13) and (int(d) > 0 and int(d) < 32):
                    break
            except:
                print()
                pass

    print(f"{y}-{int(m):02}-{int(d):02}")

main()
