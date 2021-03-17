def formatRupiah(uang):
    n = str(uang)
    if len(n) <= 3 :
        return 'Rp ' + n     
    else :
        p = n[-3:]
        q = n[:-3]
        return   formatRupiah(q) + '.' + p
        print ('Rp ' +  formatRupiah(q) + '.' + p)
