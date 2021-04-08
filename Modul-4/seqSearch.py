def seqSearch(data, key):
    pos = []
    for i in range(len(data)):
        if data[i] == key:
            pos.append(i+1)
    if len(pos) > 0:
        print('data', key, 'sebanyak', len(pos), 'ditemukan di posisi', pos)
    else:
        print('data tidak ditemukan')
    return pos

data = [30, 20, 60, 80]
seqSearch(data, 20)


def cariLurus( wadah, target ):
    n = len( wadah )
    for i in range( n ):
        if wadah[i] == target:
            return True
    return False

A = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
#cariLurus(A,31)
