def binSe(kumpulan, target):
    low = 0
    high = len(kumpulan) - 1
    find = False

    while(low <= high) and not find:
        mid = (low+high)//2       
        if target == kumpulan[mid]:
            find = True
            print('Data', target, 'ditemukan di posisi ke-')
        elif target < kumpulan[mid]:
            high = mid - 1
        else:
            low = mid + 1
            
    if not find:
        print('Data tidak ditemukan')

    lis = []
    for i in range(len(kumpulan)):
        if kumpulan[i] == target:
            lis.append(mid)
            mid+=1
    return lis

kumpulan = [10, 20, 30, 40, 20, 20, 50, 60, 70]

