class Stack:
    def __init__(self, items=None, limit=100):
        self._items = list(items) if items is not None else []
        self._limit = limit

    @property
    def items(self):
        return self._items

    def isEmpty(self):
        return len(self._items) == 0

    def push(self, item):
        if len(self._items) >= self._limit:
            raise OverflowError("Stack is full")
        self._items.append(item)

    def pop(self):
        if self.isEmpty():
            raise IndexError("Pop from empty stack")
        return self._items.pop()

    def peek(self):
        if self.isEmpty():
            raise IndexError("Peek from empty stack")
        return self._items[-1]

    def size(self):
        return len(self._items)

    def full(self):
        return len(self._items) == self._limit

    def search(self, target):
        # Distance from the top (0 if at the top)
        try:
            reverse_index = self._items[::-1].index(target)
            return reverse_index
        except ValueError:
            return -1