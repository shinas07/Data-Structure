class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, itme):
        self.queue.append(itme)

    def dequeue(self):
        if self.queue is not None:
            return self.queue.pop(0)

    def dispaly(self):
        print(self.queue)
        

queue = Queue()
queue.enqueue(88)
queue.enqueue(1)
queue.enqueue(21)
queue.enqueue(311)
queue.dispaly()
print(queue.dequeue())