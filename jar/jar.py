class Jar:
    def __init__(self, capacity=12):
        if capacity > 0:
            self._capacity = capacity
        else:
            raise ValueError("Capacity should be a positive number")
        self.cookie = "🍪"
        self.cookies = 0

    def __str__(self):
        return f"{self.cookie * self.cookies}"

    def deposit(self, n):
        if self.cookies + n <= self.capacity:
            self.cookies += n
        else:
            raise ValueError("Too many cookies. Not enough capacity to store them.")

    def withdraw(self, n):
        if self.cookies - n >= 0:
            self.cookies -= n
        else:
            raise ValueError("Not enough cookies. Try a lesser number.")

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies

jar = Jar()
jar.deposit(7)
print(jar)
jar.withdraw(6)
print(jar)
print(jar.capacity)
