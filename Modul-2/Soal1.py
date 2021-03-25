class Pesan(object):
    def __init__(self, kata):
        self.itu = kata

    def apakahTerkandung(self, ini):
        if ini in self.itu:
            return True
        else :
            return False

    def hitungKonsonan(self):
        hurufVokal = "AIUEOaiueo"
        a = 0
        for i in self.itu:
            if i not in hurufVokal:
                a += 1
        print(a)

    def hitungVokal(self):
        hurufVokal = "AIUEOaiueo"
        a = 0
        for i in self.itu:
            if i in hurufVokal:
                a += 1
        print(a)

        
