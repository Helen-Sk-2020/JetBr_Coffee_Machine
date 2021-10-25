class Stack():

    def __init__(self):
        self.item = []

    def push(self, el):
        self.item.append(el)

    def pop(self):
        return self.item.pop()

    def peek(self):
        return self.item[len(self.item) - 1]

    def is_empty(self):
        return self.item == []
      