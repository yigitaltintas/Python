# input = [5.6.6.5,3,3]
# output = "3,3"
# input = [7,8,8,7]
# output = "ok"

def arrayCouple(array):
    new = ""

    for i in range(len(array)):
        new += str(array[i]) + " "

        if i % 2 == 1:
            new += ","

    new = new.split(" ,")

    depo = []
    for i in new:
        if i[::-1] not in new:
            for l in i.split():
                depo.append(l)
        elif i == i[::-1] and new.count(i) < 2:
            for l in i.split():
                depo.append(l)

    if depo == []:
        return "ok"

    return ",".join(depo)


print(arrayCouple([2, 3, 3, 2, 2, 2]))
