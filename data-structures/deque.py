class Deque:
    def __init__(self):
        """
        initialize
        """

        self.items = []

    def isEmpty(self):
        """
        deque is empty ?
        """

        return self.items == []

    def addFront(self, item):
        """
        deque ya front kismindan item ekleme
        :param item:
        :return:
        """

        self.items.append(item)

    def addRear(self, item):
        """
        deque ya rear kismindan item ekleme
        :param item:
        :return:
        """

        self.items.insert(0, item)

    def removeFront(self):
        """
        deque front kismindan item cikarma
        :return:
        """

        return self.items.pop()

    def removeRear(self):
        """
        deque rear kismindan item cikarma
        :param item:
        :return:
        """

        return self.items.pop(0)

    def size(self):
        """
        size of deque
        :return:
        """

        return len(self.items)


deque = Deque()

print(deque.isEmpty())
deque.addFront('deep')
deque.addRear('learning')
print('size', deque.size())
deque.removeFront()
deque.removeRear()
print('size', deque.size())
