class matrix(object):
    def cekKonsisten(self, n):
        baris = len(n)
        kolom = len(n[0])

        if kolom == baris:
            print("Isi dan Ukuran matrix konsisten.")
        else:
            print("Isi dan Ukuran matrix tidak konsisten.")

    def cekTipeData(self, n):
        for i in n:
            for j in i:
                if type(j) != int:
                    return "False : Tipe data berbeda"
            return "True : Tipe data sama"
    
p=[[0,1],[9,8],[0,0]]
q=[[0,1],[9,8]]
r=[[1,'a'],[2,'b']]
m = matrix()

def ambilUkuran(n):
    baris = len(n)
    kolom = len(n[0])
    return "Ukuran matrix = " + str(baris) + " x " + str(kolom)


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
