import cmath

def kök_bul(a, b, c):
    x1 , x2 = 0, 0
    liste = []

    if a == 0:
        x1 = - c / b
        liste.append(x1)

    else:
        x1 = (-b + cmath.sqrt(b * b - 4 * a * c)) / 2 * a
        x2 = (-b + cmath.sqrt(b * b - 4 * a * c)) / 2 * a
        liste.append(x1)
        liste.append(x2)

    kokler = tuple(liste)
    return kokler

print(kök_bul(1,0,-4))
