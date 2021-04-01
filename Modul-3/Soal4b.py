class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def awal(self, new_data):
        print("Menambah simpul di awal  ",new_data)
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
        
    def akhir(self,new_data):
        print("Menambah simpul di akhir ",new_data)
        new_node = Node(new_data)
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        last = self.head
        while(last.next is not None):
            last = last.next
        last.next = new_node
        new_node.prev = last
        return
    
    def cetakList(self,node):
        print("\nMencetak data dari depan :")
        while (node is not None):
            print (" %d "%(node.data))
            last = node
            node = node.next
        print ("\nMencetak data dari belakang :")
        while (last is not None):
            print (" %d "%(last.data))
            last = last.prev

##d = DoublyLinkedList()
##d.awal(1)
##d.awal(9)
##d.akhir(8)
##d.akhir(0)
##d.cetakList(d.head)
