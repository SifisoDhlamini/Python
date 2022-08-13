def main():
    time = input("What time is it? ").strip()
    if(time.endswith("p.m.") and int(time[0:-8]) < 12):
        hours = int(time[0:-8]) + 12
        mins = int(time[-7:-5])
        print(hours)
        print(mins)
        time = f"{hours}:{mins}"
    time.removesuffix(" p.m.")
    time.removesuffix(" a.m.")
    convert(time)


def convert(time):
    hours, minutes = (int(time[0:-3]), int(time[-2:]))
    match hours:
        case 7 | 8:
            if(hours == 7 or minutes == 0):
                print("breakfast time")
        case 12 | 13:
            if(hours == 12 or minutes == 0):
                print("lunch time")
        case 18 | 19:
            if(hours == 18 or minutes == 0):
                print("dinner time")



if __name__ == "__main__":
    main()
