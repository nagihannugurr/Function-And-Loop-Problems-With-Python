def mukemmel_sayi(sayi):

    toplam = 0


    for i in range(1,sayi):
        if sayi%i == 0:
            toplam += i
    if toplam == sayi:
        return True
    else:
        return False

#print(mukemmel_sayi(6))

def mukemmel():
    liste = []

    for i in range(1,10000):
        if mukemmel_sayi(i) == True:
            liste.append(i)
    print(liste)

mukemmel()









