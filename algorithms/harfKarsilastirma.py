# Iki kelimenin icin ayni harflerini var olup olmadigini kontrol eden fonksiyon
def harfKarsilastirma(str1, str2):
    for i in str1:
        if (i not in str2):
            return False

    return True


print(harfKarsilastirma('ankara', 'kran'))
print(harfKarsilastirma('trabzon', 'trbzn'))
