def binSe(kumpulan, target):
    #mulai dari seluruh runtutan elemen
    low = 0
    high = len(kumpulan) - 1

    #secara berulang belah urutan jadi separuhnya
    #sampai targetnya ditemukan

    while low <= high:
        mid = (high + low)//2
        
        if kumpulan[mid] == target:
            return True
        
        elif target < kumpulan[mid]:
            high = mid - 1
        else:
            low = mid +1

    return False

kumpulan = [10, 20, 30, 40, 50, 60, 70]
