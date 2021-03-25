from LatOOP3 import Manusia

class Mahasiswa(Manusia):
    def __init__ (self, nama, NIM, kota, us, matkul=[]):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
        self.matkul = matkul
    def __str__(self):
        s = self.nama + ', NIM' + str(self.NIM)\
            + '. Tinggal di ' + self.kotaTinggal\
            + '. Uang saku Rp. ' + str(self.uangSaku)\
            + ' tiap bulannya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self, s):
        print("Saya baru saja makan", s, "sambil belajar.")
        self.keadaan = 'kenyang'
    def ambilKotaTinggal(self):
        return self.kotaTinggal
    def perbaharuiKotaTinggal(self, kotabaru):
        self.kotaTinggal = kotabaru
    def tambahUangSaku(self, tambah):
        self.uangSaku += tambah
    def ambilKuliah(self, matkul):
        self.matkul.append(matkul)
    def listKuliah(self):
        return self.matkul
    def hapusMatkul(self, matkul):
        self.matkul.remove(matkul)
