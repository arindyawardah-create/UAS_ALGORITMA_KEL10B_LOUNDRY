class MinHeap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def get_priority(self, data):
        if data.layanan.lower() == "express":
            return 1
        return 2

    def insert(self, data):
        self.heap.append(data)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self.get_priority(self.heap[index]) < self.get_priority(self.heap[parent]):
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def delete_root(self):
        if self.is_empty():
            print("Heap kosong.")
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]

        self.heap[0] = self.heap.pop()

        self.heapify_down(0)

        return root

    def heapify_down(self, index):
        size = len(self.heap)

        while True:

            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and self.get_priority(self.heap[left]) < self.get_priority(self.heap[smallest]):
                smallest = left

            if right < size and self.get_priority(self.heap[right]) < self.get_priority(self.heap[smallest]):
                smallest = right

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break

    def peek(self):
        if self.is_empty():
            print("Heap kosong.")
            return None

        return self.heap[0]

    def display(self):
        if self.is_empty():
            print("\nBelum ada laundry yang diproses.")
            return

        print("\n===== PRIORITAS LAUNDRY =====")

        nomor = 1

        for data in self.heap:
            print(f"\nPrioritas {nomor}")
            print(data)
            print("-" * 35)
            nomor += 1

    def count(self):
        return len(self.heap)
    def clear(self):
        self.heap.clear()

        