def binSearch(data, key):
    awal = 1
    akhir = len(data) + 1
    ketemu = False

    while(awal <= akhir) and not ketemu:
        tengah = int((awal+akhir)/2)
        
        if key == data[tengah]:
            ketemu = True
            print('data', key, 'ditemukan di posisi', tengah + 1)
        elif key < data[tengah]:
            akhir = tengah - 1
        else:
            awal = tengah + 1
            
    if not ketemu:
        print('data tidak ditemukan')


data = [10, 20, 30, 40, 50, 60, 70]
binSearch(data, 20)
