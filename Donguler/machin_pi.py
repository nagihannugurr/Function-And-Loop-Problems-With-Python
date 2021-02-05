import math

def machin_pi(x):

    arctanx = x
    xli_terim = x
    i = -1
    tol = math.pow(10,-10)



    for a in range(1,1000):

        xli_terim = xli_terim * math.pow(x,2)
        son_terim =( math.pow(i,a) * xli_terim ) / (a + 2)
        arctanx = arctanx + son_terim

        if math.fabs(son_terim) < tol:
            break
    return arctanx

def pi_bul():

    pi = 16 * machin_pi(1/5) - 4 * machin_pi(1/239)
    return pi

print(pi_bul())




















