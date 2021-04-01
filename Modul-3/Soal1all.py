#NOMOR 1-A ###########################################################
def cekKonsisten(n):
    baris = len(n)
    kolom = len(n[0])

    if kolom == baris:
        print("Isi dan Ukuran matrix konsisten.")
    else:
        print("Isi dan Ukuran matrix tidak konsisten.")

def cekTipeData(n):
    for i in n:
        for j in i:
            if type(j) != int:
                return "False : Tipe data berbeda"
        return "True : Tipe data sama"
    

#NOMOR 1-B ###########################################################
def ambilUkuran(n):
    baris = len(n)
    kolom = len(n[0])
    return "Ukuran matrix = " + str(baris) + " x " + str(kolom)


#NOMOR 1-C ###########################################################
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


#NOMOR 1-D ###########################################################
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


#NOMOR 1-E ###########################################################
def determinan(d):
    baris = len(d)
    kolom = len(d[0])

    for i in range(2):
        if i == 0:
            ad = d[i][i] * d[i+1][i+1]
        elif i == 1:
            bc = d[i-1][i] * d[i][i-1]
    return ad-bc


p =[[7,1],[4,8],[0,0]]
q =[[0,1],[9,8]]
r =[[2,4],[6,7]]
s =[[1,'a'],[2,'b']]
