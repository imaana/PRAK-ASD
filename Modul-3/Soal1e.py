def determinan(d):
    baris = len(d)
    kolom = len(d[0])

    for i in range(2):
        if i == 0:
            ad = d[i][i] * d[i+1][i+1]
        elif i == 1:
            bc = d[i-1][i] * d[i][i-1]
    return ad-bc

p=[[7,1],[4,8],[0,0]]
q=[[0,1],[9,8]]
r=[[2,4],[6,8]]
