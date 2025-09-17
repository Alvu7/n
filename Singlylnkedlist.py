class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def prepend(self, data):
     new_node = Node(data)
     new_node.next = self.head
     self.head = new_node 
    def append(self, data):
      new_node = Node(data)
      if not self.head:
        self.head = new_node
        return
      current = self.head
      while current.next:
        current = current.next
      current.next = new_node   

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next  # referencia al siguiente nodo

    def __repr__(self):
        return f"Node({self.data!r})"

def find(self, target):
    current = self.head
    index = 0
    indices=[]
    while current:
        if current.data == target:
          indices.append(index)
        current = current.next
        index += 1
    return -1
    SinglyLinkedList
    Sll(Node)
    print(n)