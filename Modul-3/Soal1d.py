from Soal1b import *
c = []
def kali(a,b):
    baris = len(a)
    kolom = len(a[0])
    if ambilUkuran(a) == ambilUkuran(b):
        for x in range(0, baris):
            row = []
            for y in range(0, kolom):
                total = 0
                for z in range(0, baris):
                    total = total + (a[x][z] * b[y][z])
                row.append(total)
            c.append(row)
            
        for x in range(0, len(c)):
            for y in range(0, len(c[0])):
                print (c[x][y], end= '')
            print()
    else:
        return "Ukuran matrix berbeda"

p=[[0,1],[9,8],[0,0]]
q=[[0,1],[9,8]]
r=[[2,4],[6,8]]
