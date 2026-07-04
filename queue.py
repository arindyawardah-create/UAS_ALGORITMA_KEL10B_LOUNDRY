class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print(f"\n{data.nama} berhasil masuk ke antrean.")

    def dequeue(self):
        if self.is_empty():
            print("\nAntrean masih kosong.")
            return None

        removed = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return removed.data

    def peek(self):
        if self.is_empty():
            print("\nAntrean kosong.")
            return None

        return self.front.data

    def display(self):
        if self.is_empty():
            print("\nAntrean masih kosong.")
            return

        current = self.front
        nomor = 1

        print("\n===== DAFTAR ANTREAN =====")

        while current:
            print(f"\nAntrean ke-{nomor}")
            print(current.data)
            print("-" * 35)

            current = current.next
            nomor += 1