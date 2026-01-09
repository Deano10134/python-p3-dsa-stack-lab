class Stack:

    def __init__(self, items=None, limit=100):
        # Support Stack(5) where 5 is the limit
        if isinstance(items, int) and limit == 100:
            self.items = []
            self.limit = items
        else:
            self.items = list(items) if items is not None else []
            self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def empty(self):
        return self.isEmpty()

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            return None

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise Exception("Stack underflow")

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        for i in range(len(self.items) - 1, -1, -1):
            if self.items[i] == target:
                return (len(self.items) - 1) - i  # 0-based from top
        return -1
