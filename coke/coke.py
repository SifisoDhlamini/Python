def main():
    valid = [25, 10, 5]
    due = 50
    while(due > 0):
        insert = validateCoin(valid, due)
        due -= insert
    print(f"Change owed: {due * - 1}")

def validateCoin(valid, due):
        print(f"Amount due: {due}")
        coin = int(input("Insert coin: "))
        if coin in valid:
            return coin
        return 0

main()