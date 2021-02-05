
#cokuz = (1,2,'a') elemanlar değiştirilemezler yeni atama olmaz
def en_kucuk_deger(*vargs):

    cokuz = (vargs)

    if cokuz == ():
        return None
    else:


        for varg in cokuz:
            en_kucuk = 0
            if varg > en_kucuk:
                en_kucuk = varg
        return en_kucuk

        #return min(cokuz)



print(en_kucuk_deger())



