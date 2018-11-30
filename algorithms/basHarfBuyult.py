#Bas harf buyulten fonksiyon
def basHarfBuyult(cumle):
    kelimeler = cumle.split(" ")
    for i in range(0, len(kelimeler)):
        kelimeler[i] = kelimeler[i][0].upper() + kelimeler[i][1:]

    return " ".join(kelimeler)


print( basHarfBuyult("Bas harfi buyuk yap") )