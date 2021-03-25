from LatOOP3 import Manusia

class SiswaSMA(Manusia):
    def __init__(self, nama, kelas, nisn):
        self.nama = nama
        self.kelas = kelas
        self.nis = nisn

    def __str__(self):
        info = self.nama + ', kelas ' + str(self.kelas) \
               + '- NISN ' + str(self.nisn)
        return info

    def ambilKelas(self):
        return self.kelas
    def ambilNama(self):
        return self.nama
    def ambilNISN(self):
        return self.nisn
    def pindahKelas(self, kelasBaru):
        self.kelas = kelasBaru
