"""
input = kkwcccddee
output = 2k1w3c2d2e
"""


def harfTekrar(kelime):

    i = 0
    final_string = ""

    while i < len(kelime):

        c = kelime[i]

        j = i + 1

        compressed = [1, c]

        while j < len(kelime):

            if kelime[j] == c:
                compressed[0] += 1
            else:
                break
            j += 1

        final_string += "".join(map(str, compressed))

        i = j

    return final_string


print(harfTekrar("kkwcccddee"))