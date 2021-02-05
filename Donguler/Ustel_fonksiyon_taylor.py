import math

def taylor_serisi():

    x = float(input("Bir x değeri giriniz: "))
    tol = math.pow(10,-5)
    kacinci_terim = 1
    xli_terim = 1
    seri =  1
    son_terim = 0
    sayac = 0


    while True:
        xli_terim = xli_terim * x
        son_terim = xli_terim / math.factorial(kacinci_terim)
        seri = seri + son_terim
        kacinci_terim += 1
        sayac += 1
        if math.fabs(son_terim) < tol:
            break



    print(f"e^x ~ {seri}")
    print(f"{sayac} terim kullanıldı.")
    print(f"Son terim = {son_terim}")

taylor_serisi()










