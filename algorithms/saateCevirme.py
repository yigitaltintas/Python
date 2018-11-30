#Dakikayi saate ceviren fonksiyon
def saateCevirme(num):
    saat = int(num // 60)
    dakika = num % 60
    return str(saat) + " saat, " + str(dakika) + " dakika"


print("119 dakika => ", saateCevirme(119))
