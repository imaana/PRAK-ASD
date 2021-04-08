def binSe(kumpulan, target):
    low = 0
    high = len(kumpulan) - 1

    x = []
    while low <= high:
        mid = (high + low)//2
        
        if kumpulan[mid] == target:
            return 'Target ada pada indeks ke-' + str(mid)
        
        elif target < kumpulan[mid]:
            high = mid - 1
        else:
            low = mid +1

    return False

kumpulan = [10, 20, 30, 40, 50, 60, 70]
