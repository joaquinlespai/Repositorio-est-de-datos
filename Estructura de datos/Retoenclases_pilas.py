class pilas():
    def __init__(self):
        self.top = None
        self.stack = [1,6]
    def push(self, item):
        self.top = item
        self.stack.append(item)
        return self.top
    def pop(self):
        if not self.is_empty():
            self.stack.pop()
            self.top = self.stack[-1]
            return self.top
        else:
            raise IndexError("el stack es vacio")
    def __str__(self):
        return str(self.stack)
    def is_empty(self):
        return len(self.stack == 0)
    def size(self):
        return len(self.stack)