"""
input ['deeplearning', 'de,el,lear,deep,learn,ar,learning']
output['deep,learning']
"""

def splitWord(liste):
    word = list(liste[0])
    d = liste[1].split(",")
    for i in range(1, len(word)):
        c = word[:]
        c.insert(i, " ")
        x, y ="".join(c).split()
        if x in d and y in d:
            return x + ", " + y

    return "No way"


print(splitWord(["deeplearning", "d,eeplearning,el,lear,deeplea,ning,ar"]))
