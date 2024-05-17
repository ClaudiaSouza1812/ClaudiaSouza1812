class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Type a positive integer")
        self._capacity = capacity
        self._size = 0


    def __str__(self):
        return self.size * "🍪"


    def deposit(self, n):
        if n > self.capacity:
            raise ValueError("Exceed capacity")
        if self.size + n > self.capacity:
            raise ValueError("Exceed capacity")
        self._size += n


    def withdraw(self, n):
        if n > self._size:
            raise ValueError("Exceed capacity")
        self._size -= n


    @property
    def capacity(self):
        return self._capacity


    @property
    def size(self):
        return self._size

def main():

    jar = Jar()
    jar._capacity = 20
    jar._size = 10
    jar.deposit(5)
    jar.withdraw(10)

    print(str(jar))

main()