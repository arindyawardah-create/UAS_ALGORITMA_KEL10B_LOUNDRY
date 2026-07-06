#stack
class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
    def is_empty(self):
        return self.top is None
    def push(self, data):
        new_node = StackNode(data)
        new_node.next = self.top
        self.top = new_node

        print(f"\n{data.nama} berhasil masuk ke riwayat laundry.")
    def pop(self):
        if self.is_empty():
            print("\nRiwayat laundry masih kosong.")
            return None

        removed = self.top
        self.top = self.top.next

        return removed.data
    def peek(self):
        if self.is_empty():
            print("\nRiwayat laundry masih kosong.")
            return None

        return self.top.data
    def display(self):
        if self.is_empty():
            print("\nBelum ada riwayat laundry.")
            return

        current = self.top
        nomor = 1

        print("\n========== RIWAYAT LAUNDRY ==========")

        while current:
            print(f"\nRiwayat ke-{nomor}")
            print(current.data)
            print("-" * 40)

            current = current.next
            nomor += 1
    def count(self):
        jumlah = 0
        current = self.top

        while current:
            jumlah += 1
            current = current.next

        return jumlah
    def clear(self):
        self.top = None
        print("\nRiwayat laundry berhasil dikosongkan.")