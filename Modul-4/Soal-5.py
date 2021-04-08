class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.next = link
        
    def cari(self, yang_dicari):
        posisi = 1
        p = self
        while p is not None:
            if p.data == yang_dicari:
                print(yang_dicari, " berada pada posisi ", posisi)
                return True
            
            else:
                posisi += 1
                p = p.next
        print(yang_dicari, " tidak ditemukan dalam list")
        return False

c = Node(9, Node(8, Node(1, Node(5))))

