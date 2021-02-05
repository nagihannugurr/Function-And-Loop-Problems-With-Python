def sir_salgin():

    s = 0.99
    i = 0.01
    r = 0.00

    a = 0.6
    b = 0.2

    toplam = 0

    print("t         s            i              r                 toplam")
    print("----      ----         -----        ------            --------------")
    for t in range(0,100):

        s = s - a * i * s
        i = i + a * i * s - b * i
        r = r + b * i

        toplam = s + i + r

        if i < 1/1000:
            break
        print(f"{t}        {s}          {i}           {r}         {toplam}")



sir_salgin()
