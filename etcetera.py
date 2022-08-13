#mypy catches intended type and the fact that function returns nothing
def meow(n: int) -> str:
    """
    Meow n times.

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string n meowa, one per line
    :rtype: str
    """
    return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meow, end="")


# balance = 0

# def main():
#     deposit(100)
#     withdraw(50)
#     print(f"Balance: {balance}")

# def deposit(n):
#     global balance
#     balance +=  n

# def withdraw(n):
#     global balance
#     balance -= n

# if __name__ == "__main__":
#     main()