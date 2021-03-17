def apakahKabisat(tahun):
    tahun = int(tahun)
    if (tahun % 4) == 0:
        if (tahun % 100) == 0:
            if (tahun % 400) == 0:
                print ("True")
            else:
                print ("False")
        else:
            print ("True")
    else:
        print ("False")
