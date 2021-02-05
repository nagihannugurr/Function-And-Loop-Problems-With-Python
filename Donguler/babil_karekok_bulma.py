import math

def babil():

    karekok_alinacak_sayi = float(input("Karekökü alınacak sayı: "))
    x = int(input("İlk tahmin: "))

    tol = math.pow(10,-10)
    iterasyon = 0
    hata = 0

    while True:

        x = 0.5 * ( x + karekok_alinacak_sayi / x)

        hata = math.pow(x,2) - karekok_alinacak_sayi
        if math.fabs(hata) < tol:
            break

        iterasyon += 1

    print(f"Karekök ~ {x}")
    print(f"{iterasyon} iterasyon")

babil()


