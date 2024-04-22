class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_value(self,value):
        current = self.head
        if current and current.data == value:
            self.head = current.next
            return 
        prev = None
        current = self.head 
        while current.next:
            if current.data == value:
                current.next = current.next.next
                return 
            current = current.next




    def display(self):
        current = self.head
        while current is not None:
            print(current.data,end=" -> ")
            current = current.next
        print()


ll = LinkedList()
ll.append(8)
ll.append(99)
ll.append(22)
ll.prepend(99)
ll.prepend(229)
ll.display()
