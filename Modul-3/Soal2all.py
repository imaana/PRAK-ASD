#membangkitkan matrix berisi nol semua, dengan diberikan ukurannya
def buatNol (m, n):
    x = [[0 for i in range(m)] for j in range(n)]
    print(x)

#memberikan matrix bujursangkar ukuran m × m
def buatNoll (m):
    x = [[0 for i in range(m)] for j in range(m)]
    print(x)

#membangkitkan matrix identitas, dengan diberikan ukurannya
def buatIdentitas(m):
    x = [[1 if j == i
            else 0 for j in range(m)] for i in range(m)]
    print(x)
    
a=[[0,1],[9,8]]
