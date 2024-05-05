class MaxHeap:
    def __init__(self):
        self.heap = []


    def insert(self, value):
        self.heap.append(value)
        self._heapify_up()  # Fix the Max Heap property by moving the new value up

    def remove(self):
        heap_size = len(self.heap)
        if heap_size > 1:
            self.heap[0], self.heap[heap_size - 1] = self.heap[heap_size - 1], self.heap[0]
            popped = self.heap.pop()
            self._heapify_down()
        elif heap_size == 1:
            popped = self.heap.pop()
        else:
            raise IndexError("Pop from an empty heap")
        return popped

        

    def _heapify_up(self):
        """
        Move the last element up to its correct position in the Max Heap.
        """
        index = len(self.heap) -1
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] > self.heap[parent_index]:  # If the child is greater than the parent
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break # Stop if the Max Heap property is satisfied


    def _heapify_down(self):
        """
        Move the root element down to its correct position in the Max Heap.
        """

        index = 0 # Start from the root
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            largest = index

            if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
                largest = left_child_index

            if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
                largest = right_child_index

            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break  # Stop if the Max Heap property is satisfied

maxheap = MaxHeap()

maxheap = MaxHeap()
maxheap.insert(5)
maxheap.insert(9)
maxheap.insert(1)
maxheap.insert(3)
maxheap.insert(9)
maxheap.insert(11)
maxheap.insert(31)
# maxheap.remove()

print(maxheap.heap)