class Node(object):
    def __init__(self, value):
        """
       Node olustur
       """
        self.value = value
        self.nextnode = None

    def setNextNode(self, node):
        """
       nect node`un ne oldugunu set eder
       """
        self.nextnode = node

    def getNextNode(self):
        """
        bir sonraki node`u return eder
        """
        return self.nextnode

    def getNodeValue(self):
        """
        node icerisinde yer alana degeri return eder
        """
        return self.value


# node sehir , node value plaka

ankara = Node("06")
bolu = Node("14")
istanbul = Node("34")

# ankara => bolu
ankara.setNextNode(bolu)
print(ankara.getNextNode().getNodeValue())

# ankara => bolu => istanbul
bolu.setNextNode(istanbul)
print(bolu.getNextNode().getNodeValue())
