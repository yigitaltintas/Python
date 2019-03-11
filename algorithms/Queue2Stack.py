class Queue2Stack(object):
    def __init__(self):
        """
        initialize 2 stacks
        """
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        """
        stact'e item eklemek queue olusturmak icin
        :param item:
        """
        self.stack1.append(item)

    def dequeue(self):
        """
        stack1'in icinden pop yaparak stack2 nin icine item eklemek
        """
        if not self.stack2:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()


queue = Queue2Stack()
queue.enqueue("1")
queue.enqueue("2")
queue.enqueue("3")
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
