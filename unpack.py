def f(*args, **kwargs):
    if args:
        print("Positional arguments:", args)
    if kwargs:
        print("Keyword arguments:", kwargs)



f(100, 50, 25, 5)
f({"gallons":100, "sickels":50, "knuts":25})
coins0 = [100, 50, 25]
f(*coins0)


def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]
#use astericks (*) to unpack list of coins and pas them to total function
print(total(*coins), " knuts")

coins2 = [100, 50, 25, 100, 50, 25, 125]
#use unpacking and sum() to calculate sum of all unique in coins2 list
print("SUM: ", sum(set(coins2)))

coins3 = {"sickles": 50, "galleons": 100, "knuts": 25}
#use unpacking to unpack coins3 dictionary and pass it to total function
print(total(**coins3), " knuts")


