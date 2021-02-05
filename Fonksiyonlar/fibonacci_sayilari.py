
def fibonacci(n):

    n1, n2 = 0,1
    sonuc = 0
    liste = []
    for i in range(0,n):
        if i == 1:
            liste.append(1)
        else:
            sonuc = n1 + n2
            liste.append(sonuc)
            n1 = n2
            n2 = sonuc


    print(liste)



fibonacci(10)
