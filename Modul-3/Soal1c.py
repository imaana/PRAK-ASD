from Soal1b import *
def jumlah(a,b):
    baris = len(a)
    kolom = len(a[0])
    if ambilUkuran(a) == ambilUkuran(b):
        for x in range(0, baris):
            for y in range(0, kolom):
                print (a[x][y] + b[x][y], end = '')
            print()
    else:
        return "Ukuran matrix berbeda"

p=[[0,1],[9,8],[0,0]]
q=[[0,1],[9,8]]
r=[[2,4],[6,8]]
