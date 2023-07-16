# Build a max-heap to store the data from an unsorted list.
# Extract the largest value from the heap and place it into a sorted list.
# Replace the root of the heap with the last element in the list. Then, rebalance the heap.
# Once the max-heap is empty, return the sorted list.

def max_heapify(arr, n, i):
    # Function to maintain the max heap property at a given node in the heap.
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # Compare the left child with the current node.
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    # Compare the right child with the current node.
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    # If the largest node is not the current node, swap them and recursively call max_heapify.
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)


def build_max_heap(arr):
    # Function to build the max heap from a given array.
    n = len(arr)

    # Start from the last non-leaf node and call max_heapify to rearrange the elements.
    # The nodes after n//2 - 1 are leaf nodes and already satisfy the max heap property,
    # so we only need to consider nodes up to n//2 - 1.
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)


def heap_sort(arr):
    # Function to perform heap sort on a given array.
    n = len(arr)

    # Build the max heap from the array.
    build_max_heap(arr)

    # Extract elements one by one from the max heap and place them at the end of the array.
    sorted_array = []
    for i in range(n - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap the root (max element) with the last element.
        sorted_array.insert(0, arr.pop())  # Insert the max element at the beginning of the sorted array.
        max_heapify(arr, i, 0)  # Maintain the max heap property for the remaining elements.

    return sorted_array

# Example usage:
input_list = [99, 22, 61, 10, 21, 13, 23]
sorted_array = heap_sort(input_list)
print("Sorted Array:", sorted_array)
