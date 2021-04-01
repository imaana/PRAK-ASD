class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
            
    def akhir(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    def awal(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def cetakDariDepan(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def cetakDaribelakang(self):
        temp = None
        cur = self.head
        while cur:
            temp = curl.prev
            cur.prev = cur.next
            cur.next = temp
            cur = cur.prev
        if temp:
            self.head = temp.prev
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            
d = DoublyLinkedList()
print(d.akhir(1))
print(d.awal(2))
##d.cetakDariDepan(3)
##d.cetakDariBelakang(4)
