class MinHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    # HEAP HELPER METHODS
    # DO NOT CHANGE!
    def parent_idx(self, idx):
        return idx // 2

    def left_child_idx(self, idx):
        return idx * 2

    def right_child_idx(self, idx):
        return idx * 2 + 1

    def child_present(self, idx):
        return self.left_child_idx(idx) <= self.count

    # END OF HEAP HELPER METHODS

    def add(self, element):
        self.count += 1
        self.heap_list.append(element)
        self.heapify_up()

    def heapify_up(self):
        idx = self.count
        while self.parent_idx(idx) > 0:
            child = self.heap_list[idx]
            parent = self.heap_list[self.parent_idx(idx)]
            if parent > child:  # Change comparison to maintain min heap property
                self.heap_list[idx] = parent
                self.heap_list[self.parent_idx(idx)] = child
            idx = self.parent_idx(idx)

    def retrieve_min(self):  # Changed the method name to retrieve_min
        if self.count == 0:
            return None
        min_value = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.count]
        self.count -= 1
        self.heap_list.pop()
        self.heapify_down()
        return min_value

    def heapify_down(self):
        idx = 1
        while self.child_present(idx):
            smaller_child_idx = self.get_smaller_child_idx(idx)  # Changed the method name
            child = self.heap_list[smaller_child_idx]
            parent = self.heap_list[idx]
            if parent > child:  # Change comparison to maintain min heap property
                self.heap_list[idx] = child
                self.heap_list[smaller_child_idx] = parent
            idx = smaller_child_idx

    def get_smaller_child_idx(self, idx):  # Changed the method name to get_smaller_child_idx
        if self.right_child_idx(idx) > self.count:
            return self.left_child_idx(idx)
        else:
            left_child = self.heap_list[self.left_child_idx(idx)]
            right_child = self.heap_list[self.right_child_idx(idx)]
            if left_child < right_child:  # Change comparison to find the smaller child
                return self.left_child_idx(idx)
            else:
                return self.right_child_idx(idx)


def heapsort(lst):
    min_heap = MinHeap()  # Changed the class name to MinHeap
    for idx in lst:
        min_heap.add(idx)

    sorted_list = []
    while min_heap.count > 0:  # Changed to use min_heap.count
        min_value = min_heap.retrieve_min()  # Changed to use min_heap.retrieve_min()
        sorted_list.append(min_value)

    return sorted_list  # Removed the reverse operation to get ascending order

my_list = [99, 22, 61, 10, 21, 13, 23]
sorted_list = heapsort(my_list)
print(sorted_list)
