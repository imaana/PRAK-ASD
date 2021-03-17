def cetakSiku(x):
    string = ""
    baris = 1
    while baris <= x:
        kolom = baris
        while kolom > 0:
            string = string + "*"
            kolom = kolom - 1
        string = string + "\n"
        baris = baris + 1
    print (string)
