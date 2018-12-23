# input [2,3,4,5]
# output 4523

def rotateArray(array):
    eski_baslangic = array[0]

    yeni_baslangic = [str(array[eski_baslangic])]

    count = eski_baslangic + 1

    length = len(array)

    while count % length != eski_baslangic:
        yeni_baslangic.append(str(array[count % length]))
        count += 1

    return "".join(yeni_baslangic)


print(rotateArray([2, 3, 4, 5]))
