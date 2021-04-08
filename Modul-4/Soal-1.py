from mhs import*

def cariIndex(x):
    index = []
    for i in range(len(Daftar)):
        if x == Daftar[i].kotaTinggal:
            index.append(i)
    print(index)

##cariIndex('Klaten')
##cariIndex('Surakarta')
        
