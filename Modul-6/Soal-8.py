class Node():
    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode


def cetak(head):
    curr = head
    while curr is not None:
        try:
            print (curr.data)
            curr = curr.nextNode
        except:
            pass

a = Node(1)
b = Node(3)
c = Node(5)
d = Node(7)
e = Node(6)
f = Node(4)
g = Node(2)

a.nextNode = b
b.nextNode = c
c.nextNode = d
d.nextNode = e
e.nextNode = f
f.nextNode = g

def mergeSortLinkedList(A):
    linked = A
    try:
        daftar = []
        curr = A
        while curr:
            daftar.append(curr.data)
            curr = curr.nextNode
        A = daftar
        #print (A)
    except:
        A = A

    if len(A) > 1:
        mid = len(A)//2
        separuhKiri = A[:mid]
        separuhKanan = A[mid:]
        mergeSortLinkedList(separuhKiri)
        mergeSortLinkedList(separuhKanan)

        i=0 ; j=0 ; k=0
        while i < len(separuhKiri) and j < len(separuhKanan):
            if separuhKiri[i] < separuhKanan[j]:
                A[k] = separuhKiri[i]
                i = i + 1
            else:
                A[k] = separuhKanan[j]
                j = j + 1
            k=k+1

        while i < len(separuhKiri):
            A[k] = separuhKiri[i]
            i = i + 1
            k = k + 1
        while j < len(separuhKanan):
            A[k] = separuhKanan[j]
            j = j + 1
            k = k + 1

    for x in A:
        try:
            linked.data = x
            linked = linked.nextNode
        except:
            pass

mergeSortLinkedList(a)
cetak(a)
