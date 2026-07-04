class Laundry:
    def __init__(self, kode, nama, noHp, layanan, berat):
        self.kode = kode
        self.nama = nama
        self.noHp = noHp
        self.layanan = layanan
        self.berat = berat

        if layanan.lower() == "express":
            self.harga_perkg = 10.000
            self.prioritas = 1
        else:
            self.harga_perkg = 7.000
            self.prioritas = 2

        self.total_harga = self.berat * self.harga_perkg
        self.status = "Menunggu"

    def __str__(self):
        return (
            f"Kode    : {self.kode}\n"
            f"Nama    : {self.nama}\n"
            f"No. HP  : {self.noHp}\n"
            f"Layanan : {self.layanan}\n"
            f"Berat   : {self.berat} kg\n"
            f"Total   : Rp{self.total_harga:,.3f}".replace(",", ".") + "\n"
            f"Status  : {self.status}"
        )