class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
        
    def cari(self, yang_dicari):
        posisi = 1
        p = self.head
        while p is not None:
            if p.data == yang_dicari:
                print(yang_dicari, " berada pada posisi ", posisi)
                return True
            posisi += 1
            p = p.next
        else:
            print(yang_dicari, " tidak ditemukan dalam list")
            return False
                
    
    def tambahDepan(self, head):
        tambahan = Node(head)
        tambahan.next = self.head
        self.head = tambahan

        
    def tambahAkhir(self, head):
        tambahan = Node(head)
        if self.head is None:
            self.head = tambahan
            return

        p = self.head
        while p.next is not None:
            p = p.next
        p.next = tambahan


    def tambah(self, head, posisi):
        sekarang = 0
        tambah = Node(head)
        x = self.head
        
        while x != None:
            if sekarang == posisi-2:
                tambah.next = x.next
                x.next = tambah
            elif posisi == 1:
                tambah.next = self.head
                self.head = tambah
                break
            elif x == None:
                break
            else:
                x = x.next
            sekarang +=1

    def hapus(self, posisi):
        if self.head is None:
            print("List kosong")
            return

        if self.head.data == posisi:
            self.head = self.head.next
            return

        d = self.head
        while d.next is not None:
            if d.next.data == posisi:
                break
            d = d.next

        if d.next is None:
            print("Angka ", posisi, " tidak ada dalam list")
        else:
            d.next = d.next.next

    def display_list(self):
        if self.head is None:
            print("Data tidak tersedia.")
            return
        else:
            print("Isi Data adalah : ")
            p = self.head
            while p is not None:
                print(p.data, " ", end=' ')
                p = p.next
            print()

s = SingleLinkedList()

        
