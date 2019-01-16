class Queue:
    def __init__(self):
        """
        initialize
        """

        self.items = []

    def isEmpty(self):
        """
        Bos olup olmadi[ini kontrol ettim
        :return: bool
        """
        return self.items == []

    def enqueue(self, item):
        """
        Queue item ekleme
        """
        self.items.insert(0, item)

    def dequeue(self):
        """
        Queue item cikarma
        """
        self.items.pop()

    def size(self):
        """
        length of items(queue)
        """
        return len(self.items)

queue = Queue()

print(queue.isEmpty())

queue.enqueue('1')
queue.enqueue('2')

print('size', queue.size())

queue.dequeue()
print('size', queue.size())

queue.dequeue()
print('size', queue.size())

print(queue.isEmpty())