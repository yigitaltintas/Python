class Node(object):

    def __init__(self, data):
        """
        Node olustur
        """
        self.data = data
        self.next = None


# Linked list class
class LinkedList(object):

    def __init__(self):
        """
        head initializer
        """
        self.head = None

    def push(self, new_data):
        """
        linked list basina node ekle
        """

        # node olustur ve icerisindeki veriyi belirle
        new_node = Node(new_data)

        # yeni node kendisinden sonra gelen node`u isaret etsin
        new_node.next = self.head

        # head yeni node`u isaret etsin
        self.head = new_node

    def printLinkedList(self):
        """
        linked list print eder
        """

        temp = self.head
        print(" Linked List : ")
        while temp:
            print(temp.data)
            temp = temp.next


linked_list = LinkedList()
linked_list.push(15)
linked_list.push(25)
linked_list.push("ilk eleman")
linked_list.printLinkedList()
