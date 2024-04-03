class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        return '🍪' * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError('Capacity exceeded')
        self.size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError('No cookies left')
        self.size -= n

    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError('Capacity cannot ba a -ve number')
        self._capacity = capacity
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        self._size = size
