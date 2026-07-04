from laundry import Laundry
from queue import Queue

antrian = Queue()

while True:
    print("\n" + "=" * 40)
    print("      SISTEM MANAJEMEN LAUNDRY")
    print("=" * 40)
    print("1. Tambah Laundry")
    print("2. Lihat Antrean")
    print("3. Proses Antrean")
    print("0. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        kode = int(input("Kode            : "))
        nama = input("Nama Pelanggan  : ")
        noHp = input("No. HP          : ")
        layanan = input("Layanan (Express/Reguler): ")
        berat = float(input("Berat (kg)      : "))

        data = Laundry(kode, nama, noHp, layanan, berat)
        antrian.enqueue(data)

    elif pilihan == "2":
        antrian.display()

    elif pilihan == "3":
        data = antrian.dequeue()

        if data:
            print("\nLaundry yang diproses:")
            print(data)

    elif pilihan == "0":
        print("\nTerima kasih telah menggunakan sistem laundry.")
        break

    else:
        print("\nPilihan tidak valid!")