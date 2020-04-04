class MaxBinaryHeap:
    def __init__(self, elements):
        self.list = elements
        self.heapSize = len(self.list)
        self.build_max_heap(self.heapSize)

    @staticmethod
    def parent(i):
        return (i / 2) - 1

    @staticmethod
    def left(i):
        return (2 * i) + 1

    @staticmethod
    def right(i):
        return (2 * i) + 2

    # check if parent is larger than its both children
    # if child/children found larger than swap the larger child with its parent
    def heapyfy(self, i):
        left = self.left(i)
        right = self.right(i)
        if left <= self.heapSize-1 and self.list[left] > self.list[i]:
            largest = left
        else:
            largest = i
        if right <= self.heapSize-1 and self.list[right] > self.list[largest]:
            largest = right
        if largest != i:
            self.list[i], self.list[largest] = self.list[largest], self.list[i]
            self.heapyfy(largest)

    # we will go from half of the array to starting index in list
    # and build the heap => inplace building
    # looping from half of size of array, as it will make the leaves in heap data structure format automatically
    def build_max_heap(self, heap_size):
        for i in range(int(heap_size-1 / 2), -1, -1):
            self.heapyfy(i)

    def extract_max(self):
        max_element = self.list[0]
        self.list[0] = self.list[self.heapSize - 1]
        self.heapSize = self.heapSize - 1
        self.list = self.list[0:self.heapSize]
        self.heapyfy(0)
        return max_element

    def change_heap_value(self, i, value):
        self.list[i] = value
        self.heapyfy(i - 2)


# Driven code for testing heap function
arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
heap = MaxBinaryHeap(arr)
print(heap.list)
print(heap.extract_max())
print(heap.list)
heap.change_heap_value(2, 56)
print(heap.list)
