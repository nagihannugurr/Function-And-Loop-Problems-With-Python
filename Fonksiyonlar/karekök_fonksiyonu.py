import math

def karekök_bul(N, x0):

    maxiter = 15
    tol = math.pow(10,-10)
    sayac = 0

    while True:


        x0 =  0.5 * (x0 + N / x0)

        if math.fabs(x0 * x0 - N) < tol and sayac > maxiter:
            print("10 iterasyonda sonuca ulaşılamadı. 'hata' veya 'maxiter' değerlerini değiştirin")
            break
        sayac += 1





    print(x0)

karekök_bul(10000,0.1)


"""

 if math.fabs(x0 * x0 - N) < tol and sayac > maxiter:
            print("10 iterasyonda sonuca ulaşılamadı. 'hata' veya 'maxiter' değerlerini değiştirin")
"""
