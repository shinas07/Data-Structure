class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.last = None

    def enqueue(self, data):
        new_ndoe = Node(data)
        if self.head is None:
            self.head = new_ndoe
            self.last = self.head 
        else:
            self.last.next = new_ndoe
            self.last = new_ndoe
        
    def duqueue(self):
        if self.head is None:
            print("Queue is empty")
            return None
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.last = None
        return data
    
    def peek(self):
        if self.head is None:
            print("Queue is empty")
            return None
        else:
            return self.head.data

queue = Queue()

queue.enqueue(22)
queue.enqueue(122)
queue.enqueue(31)
queue.enqueue(411)
queue.enqueue(59)

print(queue.peek())