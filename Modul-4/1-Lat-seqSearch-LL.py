from mhs import*

def uangKecil(Daftar):
    uang = Daftar[0].uangSaku
    for i in Daftar:
        if i.uangSaku < uang:
            uang = i.uangSaku
            if i.uangSaku == uang:
                nama = i.nama
    print('\nMahasiswa yang memiliki uang saku terkecil adalah', nama, ', yaitu sebesar :', uang)


def uangBesar(Daftar):
    uang = Daftar[0].uangSaku
    for i in Daftar:
        if i.uangSaku > uang:
            uang = i.uangSaku
            if i.uangSaku == uang:
                nama = i.nama
    print('\nMahasiswa yang memiliki uang saku terbesar adalah', nama, ', yaitu sebesar :', uang)

def under250(Daftar):
    nama = []
    for i in Daftar:
        if i.uangSaku < 250000:
            nama.append(i.nama)
    print('\nMahasiswa yang memiliki uang saku dibawah Rp.250.000 :')
    for x in nama:
        print(x)

def upto250(Daftar):
    nama = []
    for i in Daftar:
        if i.uangSaku > 250000:
            nama.append(i.nama)
    print('\nMahasiswa yang memiliki uang saku diatas Rp.250.000 :')
    for x in nama:
        print(x)


##uangKecil(Daftar)
##uangBesar(Daftar)
##under250(Daftar)
##upto250(Daftar)
