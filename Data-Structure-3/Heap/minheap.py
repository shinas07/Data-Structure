class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):

        self.heap.append(value)
        self._heapify_up()

    def remove(self):
        popped = []
        if len(self.heap) > 1:
            self.heap[0], self.heap[- 1] = self.heap[- 1], self.heap[0]
            self._heapify_down()
        elif len(self.heap) == 1:
            popped = self.heap.pop()
        else:
            raise IndexError("Heap is empty")
        return popped
        
    def _heapify_up(self):
        """
        Move the root element down to its correct position in the min heap.
        """
        index = len(self.heap) -1
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def _heapify_down(self):
        """
        Move the root element down to its correct position in the min heap.
        """
        index = 0
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest = index

            if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
                smallest = left_child_index
            if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
                smallest = right_child_index    


            if smallest != index:
                self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
                index = smallest
            else:
                break

heap = MinHeap()

heap.insert(14)
heap.insert(3)
heap.insert(81)
heap.insert(5)
heap.insert(7)
heap.insert(11)
heap.remove()

print(heap.heap)
