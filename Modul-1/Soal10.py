def selesaikanABC(a,b,c) :
    angka = 0
    angka = (b**2) - (4*a*c)

    if angka == 0 :
        print("Determinannya nol. Persamaan mempunyai satu akar kembar.")
    elif angka > 0 :
        print("Determinannya positif. Persamaan mempunyai akar real dan berlainan.")
    elif angka < 0 :
        print("Determinannya negatif. Persamaan tidak mempunyai akar real.")
