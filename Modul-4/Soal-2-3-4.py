from mhs import*

def uangKecil(Daftar):
    uang = Daftar[0].uangSaku
    for i in Daftar:
        if i.uangSaku < uang:
            uang = i.uangSaku
    print('Uang saku terkecil mahasiswa adalah Rp.', uang)


def uangKecilMhs(Daftar):
    uang = Daftar[0].uangSaku
    for i in Daftar:
        if i.uangSaku < uang:
            uang = i.uangSaku
            if i.uangSaku == uang:
                nama = i.nama
    print('Mahasiswa yang memiliki uang saku terkecil adalah', nama, ', yaitu sebesar : Rp.', uang)


def under250(Daftar):
    nama = []
    for i in Daftar:
        if i.uangSaku < 250000:
            nama.append(i.nama)
    print('Mahasiswa yang memiliki uang saku dibawah Rp. 250000 :')
    for x in nama:
        print(x)

##uangKecil(Daftar)
##uangKecilMhs(Daftar)
##under250(Daftar)
