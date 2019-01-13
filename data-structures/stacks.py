class Stack:

    def __init__(self):
        """
        initialize
        """
        self.items = []

    def isEmpty(self):
        """
        is empty?
        """
        return self.items == []  # boolean operation

    def push(self, item):
        """
        stack'e item ekler
        """

        self.items.append(item)

    def pop(self):
        """
        stack'ten item cikarma
        """
        return self.items.pop()

    def top(self):
        """
        stack icerisindeki son itemi gosterir
        """
        return self.items[len(self.items) - 1]

    def size(self):
        """
        size of stack
        """

        return len(self.items)


stack = Stack()

print(stack.isEmpty())
stack.push("test")
print(stack.top())
stack.push("deneme")
print(stack.top())
print('Boyutu', stack.size())
print(stack.isEmpty())
stack.pop()
stack.pop()
print('Boyutu', stack.size())
print(stack.isEmpty())