from laundry import Laundry
from queue import Queue
from bst import BST
from heap import MinHeap
from stack import Stack

# Inisialisasi Struktur Data
antrian = Queue()
data_laundry = BST()
prioritas = MinHeap()
riwayat = Stack()

# Menu
def tampilkan_menu():
    print("\n" + "=" * 45)
    print("        SISTEM MANAJEMEN LAUNDRY")
    print("=" * 45)
    print("1. Tambah Laundry")
    print("2. Lihat Antrean")
    print("3. Proses Antrean")
    print("4. Lihat Data Laundry")
    print("5. Cari Laundry")
    print("6. Hapus Data Laundry")
    print("7. Statistik Data Laundry")
    print("8. Jumlah Laundry Aktif")
    print("9. Lihat Prioritas Laundry")
    print("10. Selesaikan Laundry")
    print("11. Lihat Riwayat Laundry")
    print("12. Undo Riwayat")
    print("0. Keluar")
    print("=" * 45)

# Program Utama
while True:

    tampilkan_menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        kode = input("Kode          : ")
        nama = input("Nama          : ")
        noHp = input("No. HP        : ")
        layanan = input("Layanan (Express/Reguler): ")
        berat = float(input("Berat (kg)    : "))
        data = Laundry(kode, nama, noHp, layanan, berat)
        antrian.enqueue(data)
        print("\nLaundry berhasil ditambahkan ke antrean.")

    elif pilihan == "2":
        antrian.display()

    elif pilihan == "3":
        data = antrian.dequeue()

        if data:
            data.status = "Diproses"
            data_laundry.insert(data)
            prioritas.insert(data)
            print("\nLaundry yang diproses:")
            print(data)
        else:
            print("\nAntrean kosong.")

    elif pilihan == "4":
        print("\n===== DATA LAUNDRY =====")
        data_laundry.inorder()
    elif pilihan == "5":
        kode = input("Masukkan kode: ")
        hasil = data_laundry.search(kode)
        if hasil:
            print("\nData ditemukan")
            print(hasil)
        else:
            print("\nData tidak ditemukan.")

    elif pilihan == "6":
        kode = input("Masukkan kode: ")
        if data_laundry.search(kode):
            data_laundry.delete(kode)
            print("\nData berhasil dihapus.")
        else:
            print("\nData tidak ditemukan.")

    elif pilihan == "7":
        print("\n===== STATISTIK =====")
        print("Tinggi BST :", data_laundry.height())
    elif pilihan == "8":
        print("\nJumlah Laundry Aktif :", data_laundry.node_count())

    elif pilihan == "9":
        prioritas.display()

    elif pilihan == "10":
        selesai = prioritas.delete_root()
        if selesai:
            selesai.status = "Selesai"
            riwayat.push(selesai)
            print("\nLaundry berhasil diselesaikan.")
            print(selesai)
        else:
            print("\nTidak ada laundry yang sedang diproses.")

    elif pilihan == "11":
        riwayat.display()

    elif pilihan == "12":
        batal = riwayat.pop()
        if batal:
            batal.status = "Diproses"
            prioritas.insert(batal)
            print("\nUndo berhasil.")
            print(batal)
        else:
            print("\nRiwayat kosong.")

    elif pilihan == "0":
        print("\nTerima kasih telah menggunakan Sistem Manajemen Laundry.")
        break
    else:
        print("\nMenu tidak tersedia.")