
#r ilk değerler için periyodik  bir döngüye girer
def lojistik():
    # xt 0 ile 1 arasında
    # r 0 ile 4 arasında parametre
    # parametre belirlendikten sonra dizi içinde değişmez
    i = 0
    j = 0
    x = 0.1
    y = 0.10001
    r = float(input("r parametresi: "))

    while i < 100 and j < 100:
        x = x + (r * x * (1 - x))
        y = y + (r * y * (1 - y))

        i += 1
        j += 1
        print(f" x degeri : {x}         y degeri: {y}")









lojistik()

# r = 3.5 için yarıdan itibaren -inf
# r =4 için uzun süreli -inf
#