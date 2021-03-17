def jumlahHurufVokal(kata):
    hurufVokal = "AIUEOaiueo"
    a = 0
    for i in kata:
        if i in hurufVokal:
            a += 1
    hasil = (len(kata), a)
    print(hasil)

def jumlahHurufKonsonan(kaata):
    hurufVokal = "AIUEOaiueo"
    b = 0
    for j in kaata:
        if j not in hurufVokal:
            b += 1
    hasill = (len(kaata), b)
    print(hasill)

