from laundry import Laundry
from queue import Queue
from bst import BST
from heap import MinHeap
from stack import Stack

# Inisialisasi Struktur Data
antrian = Queue()
dataLaundry = BST()
prioritas = MinHeap()
riwayat = Stack()


def tampilkan_menu():
    print("\n" + "=" * 45)
    print("       SISTEM MANAJEMEN LAUNDRY")
    print("=" * 45)
    print("1. Tambah Pesanan Laundry")
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


while True:

    tampilkan_menu()
    pilihan = input("Pilih Menu : ")

    # 1. Tambah Laundry
    if pilihan == "1":

        kode = input("Kode Laundry : ")
        nama = input("Nama Pelanggan : ")
        noHp = input("No HP : ")
        layanan = input("Layanan (Express/Reguler) : ")
        berat = float(input("Berat (Kg) : "))

        data = Laundry(kode, nama, noHp, layanan, berat)

        antrian.enqueue(data)

    # 2. Lihat Antrean
    elif pilihan == "2":

        antrian.display()

    # 3. Proses Antrean
    elif pilihan == "3":

        data = antrian.dequeue()

        if data:

            data.status = "Diproses"

            dataLaundry.insert(data)

            prioritas.insert(data)

            print("\nLaundry berhasil diproses.")

    # 4. Lihat Data Laundry
    elif pilihan == "4":

        print("\n===== DATA LAUNDRY =====")
        dataLaundry.inorder()

    # 5. Cari Laundry
    elif pilihan == "5":

        kode = input("Masukkan Kode Laundry : ")

        hasil = dataLaundry.search(kode)

        if hasil:
            print("\nData ditemukan\n")
            print(hasil)
        else:
            print("\nData tidak ditemukan.")

    # 6. Hapus Laundry
    elif pilihan == "6":

        kode = input("Masukkan Kode Laundry : ")

        if dataLaundry.search(kode):

            dataLaundry.delete(kode)

            print("\nData berhasil dihapus.")

        else:

            print("\nData tidak ditemukan.")

    # 7. Statistik Data Laundry
    elif pilihan == "7":

        print("\n===== STATISTIK DATA =====")
        print("Tinggi BST :", dataLaundry.height())

    # 8. Jumlah Laundry Aktif
    elif pilihan == "8":

        print("\nJumlah Laundry Aktif :", dataLaundry.node_count())

    # 9. Lihat Prioritas
    elif pilihan == "9":

        prioritas.display()

    # 10. Selesaikan Laundry
    elif pilihan == "10":

        selesai = prioritas.delete_root()

        if selesai:

            selesai.status = "Selesai"

            riwayat.push(selesai)

            print("\nLaundry berhasil diselesaikan.")
            print(selesai)

        else:

            print("\nTidak ada laundry yang sedang diproses.")

    # 11. Lihat Riwayat
    elif pilihan == "11":

        riwayat.display()

    # 12. Undo Riwayat
    elif pilihan == "12":

        batal = riwayat.pop()

        if batal:

            batal.status = "Diproses"

            prioritas.insert(batal)

            print("\nUndo berhasil.")
            print("Laundry kembali ke daftar prioritas.")

        else:

            print("\nRiwayat kosong.")

    # Keluar
    elif pilihan == "0":

        print("\nTerima kasih telah menggunakan Sistem Laundry.")
        break

    else:

        print("\nPilihan tidak tersedia.")