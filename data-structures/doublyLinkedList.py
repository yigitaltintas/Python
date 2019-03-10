class doublyLinkedListNode(object):
    def __init__(self, value):
        """
        Node olustur
        """
        self.value = value
        self.nextnode = None
        self.prevnode = None

    def setNextNode(self, node):
        """
        Next node`un ne oldugunu set eder
        """
        self.nextnode = node

    def setPrevNode(self, node):
        """
        Prev node`un ne oldugu set eder
        """

        self.prevnode = node

    def getNextNode(self):
        """
        Bir sonraki node`u dondur
        """
        return self.nextnode

    def getPrevNode(self):
        """
        Bir onceki node`u dondur
        """
        return self.prevnode

    def getNodeValue(self):
        """
        Node`un degerini dondur
        """
        return self.value


# node isimleri sehir, node value plaka
# ankara , bolu, istanbul

ankara = doublyLinkedListNode("06")
bolu = doublyLinkedListNode("14")
istanbul = doublyLinkedListNode("34")

# ankara => bolu
ankara.setNextNode(bolu)
# bolu => ankara
bolu.setPrevNode(ankara)

print(ankara.getNextNode().getNodeValue())
print(bolu.getPrevNode().getNodeValue())

# bolu => istanbul
bolu.setNextNode(istanbul)
# istanbul => bolu
istanbul.setPrevNode(bolu)

print(bolu.getNextNode().getNodeValue())
print(istanbul.getPrevNode().getNodeValue())

# istanbul => bolu => ankara
print(istanbul.getPrevNode().getPrevNode().getNodeValue())