from typing import List


class MaxHeapq:
    """
    This class implements properties and methods that support a max priority queue data structure

    Attributes:
        heap: key values in the max heap are stored here
        heap_size: An integer counter of the number of keys present in the max heap

    Example:
        Class initialization:
            heapq_var = MaxHeapq()
    """

    def __init__(self):
        self.heap: List = []
        self.heap_size: int = 0

    def max_key(self):
        """Gets the highest key in the priority queue"""
        return self.heap[0]

    def heappush(self, key):
        """
        Inserts the value of key onto the priority queue, maintaining the max heap invariant.
        """
        self.heap.append(-float("inf"))
        self.increase_key(self.heap_size, key)
        self.heap_size += 1

    def increase_key(self, i, key):
        """
        This method implements the INCREASE_KEY operation, which modifies the value of a key
        in the max priority queue with a higher value.
        """
        if key < self.heap[i]:
            raise ValueError('new key is smaller than the current key')
        self.heap[i] = key
        while i > 0 and self.heap[MaxHeapq.parent(i)] < self.heap[i]:
            j = MaxHeapq.parent(i)
            holder = self.heap[j]
            self.heap[j] = self.heap[i]
            self.heap[i] = holder
            i = j

    def heapify(self, i: int) -> None:
        """
        This method implements the MAX_HEAPIFY operation for the max priority queue.
        :param i: The array index of the root node of the subtree to heapify
        """
        l = MaxHeapq.left(i)
        r = MaxHeapq.right(i)
        heap = self.heap
        if l <= (self.heap_size - 1) and heap[l] > heap[i]:
            largest = l
        else:
            largest = i
        if r <= (self.heap_size - 1) and heap[r] > heap[largest]:
            largest = r
        if largest != i:
            heap[i], heap[largest] = heap[largest], heap[i]
            self.heapify(largest)

    def heappop(self):
        """
        This method implements the EXTRACT_MAX operation. It returns the largest key in
        the max priority queue and removes this key from the max priority queue.
        :return: the largest key
        """
        if self.heap_size < 1:
            raise ValueError('Heap underflow: There are no keys in the priority queue ')
        max_key = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heap_size -= 1
        self.heapify(0)
        return max_key

    @staticmethod
    def left(i: int) -> int:
        """
        Takes as input the array index of a parent node in the binary tree and
        returns the array index of its left child.
        :param i: Current node's index
        :return: Left child index
        """
        return 2 * i + 1

    @staticmethod
    def right(i: int) -> int:
        """
        Takes as input the array index of a parent node in the binary tree and
        returns the array index of its right child.
        :param i: Current node's index
        :return: right child index
        """
        return 2 * i + 2

    @staticmethod
    def parent(i):
        """
        Takes as input the array index of a node in the binary tree and returns the array index of its parent
        :param i: Current node's index
        :return: Parent index
        """
        return (i - 1) // 2
