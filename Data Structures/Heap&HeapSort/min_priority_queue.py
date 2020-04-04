class MinBinaryHeap:
    def __init__(self, elements):
        self.list = elements
        self.heapSize = len(self.list)
        self.build_min_heap(self.heapSize)

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
        if left <= self.heapSize-1 and self.list[left] < self.list[i]:
            smaller = left
        else:
            smaller = i
        if right <= self.heapSize-1 and self.list[right] < self.list[smaller]:
            smaller = right
        if smaller != i:
            self.list[i], self.list[smaller] = self.list[smaller], self.list[i]
            self.heapyfy(smaller)

    # we will go from half of the array to starting index in list
    # and build the heap => inplace building
    # looping from half of size of array, as it will make the leaves in heap ds format automatically
    def build_min_heap(self, heap_size):
        for i in range(int((heap_size-1) / 2), -1, -1):
            self.heapyfy(i)

    def extract_min(self):
        min_element = self.list[0]
        self.list[0] = self.list[self.heapSize - 1]
        self.heapSize = self.heapSize - 1
        self.list = self.list[0:self.heapSize]
        self.heapyfy(0)
        return min_element

    def change_heap_value(self, key, value):
        self.list[key] = value
        self.heapyfy(key)


# Driven code for testing heap function
arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
heap = MinBinaryHeap(arr)
print(heap.list)
print(heap.extract_min())
print(heap.list)
heap.change_heap_value(2, 56)
print(heap.list)
heap.change_heap_value(3, 32)
print(heap.list)
for i in range(len(heap.list)):
    print(heap.extract_min())
