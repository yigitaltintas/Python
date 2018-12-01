"""
input  => 2x + 5 = 25
output => 0

input  => x - 2 = 7
output => 9

"""

def kayipBasamak(islem):

    for i in range(10):
        c = islem.replace("x", str(i))
        x = islem.index("=")

        if eval(c[:x]) == eval(c[x+1:]):
            return i


print(kayipBasamak("2x + 5 = 25"))
print(kayipBasamak("x - 2 = 7"))