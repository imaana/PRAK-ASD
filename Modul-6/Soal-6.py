from mhs import *

a=[]
for i in Daftar:
    a.append(i.nama)

def cetak ():
    for i in a:
        print (i)

def quickSort(arr):
    kurang = []
    pivotList = []
    lebih = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                kurang.append(i)
            elif i > pivot:
                lebih.append(i)
            else:
                pivotList.append(i)
        kurang = quickSort(kurang)
        lebih = quickSort(lebih)
        return kurang + pivotList + lebih

print ('Nama sebelum diurutkan :')
cetak()
print ('\nNama yang telah urut :')
a=quickSort(a)
cetak()
