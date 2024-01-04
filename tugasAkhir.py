class PerjalananLuarAngkasa:
    def __init__(self, nama, hari, harga):
        self._nama = nama
        self._hari = hari
        self._harga = harga

    def get_nama(self):
        return self._nama

    def get_hari(self):
        return self._hari

    def get_harga(self):
        return self._harga

    def hitung_biaya(self):
        return self._harga

class TurSantai(PerjalananLuarAngkasa):
    def __init__(self, nama, hari):
        harga_per_hari = 50000000
        super().__init__(nama, hari, harga_per_hari)
        self._tempat_wisata = "Bulan"

    def get_tempat_wisata(self):
        return self._tempat_wisata

    def hitung_biaya(self):
        return super().hitung_biaya()

class TurPetualangan(PerjalananLuarAngkasa):
    def __init__(self, nama, hari):
        harga_per_hari = 100000000
        super().__init__(nama, hari, harga_per_hari)
        self._tempat_wisata = "Mars"

    def get_tempat_wisata(self):
        return self._tempat_wisata

    def hitung_biaya(self):
        return super().hitung_biaya()

class TurPetualanganPremium(TurPetualangan):
    def __init__(self, nama, hari):
        self._biaya_tambahan = 80000000
        super().__init__(nama, hari)

    def get_biaya_tambahan(self):
        return self._biaya_tambahan

    def tambah_biaya_tambahan(self):
        self._harga += self._biaya_tambahan

    def hitung_biaya(self):
        return super().hitung_biaya() + self._biaya_tambahan

# Fungsi untuk membuat objek perjalanan baru
def buat_objek_perjalanan():
    print("Pilih jenis perjalanan:")
    print("1. Tur Santai")
    print("2. Tur Petualangan")
    print("3. Tur Petualangan Premium")

    pilihan = input("Masukkan nomor pilihan: ")
    nama = input("Masukkan nama anda: ")

    if pilihan == "1":
        hari = int(input("Masukkan jumlah hari: "))
        return TurSantai(nama, hari)

    elif pilihan == "2":
        hari = int(input("Masukkan jumlah hari: "))
        return TurPetualangan(nama, hari)

    elif pilihan == "3":
        hari = int(input("Masukkan jumlah hari: "))
        return TurPetualanganPremium(nama, hari)

    else:
        print("Pilihan tidak valid.")
        return None

# Main menu
daftar_perjalanan = []

while True:
    print("\nMain Menu:")
    print("1. Tambah Perjalanan Baru")
    print("2. Tampilkan riwayat Perjalanan")
    print("3. Keluar")

    pilihan_menu = input("Masukkan nomor pilihan: ")

    if pilihan_menu == "1":
        perjalanan_baru = buat_objek_perjalanan()
        if perjalanan_baru:
            daftar_perjalanan.append(perjalanan_baru)
            print("Perjalanan baru telah ditambahkan.")

    elif pilihan_menu == "2":
        if not daftar_perjalanan:
            print("Belum terdapat riwayat perjalanan.")
        else:
            print("\nRiwayat Perjalanan:")
            for idx, perjalanan in enumerate(daftar_perjalanan, start=1):
                total_biaya = perjalanan.hitung_biaya() * perjalanan.get_hari()
                print(f"{idx}. {perjalanan.get_nama()} melakukan perjalanan selama {perjalanan.get_hari()} hari ke {perjalanan.get_tempat_wisata()} dengan total biaya {total_biaya}")

    elif pilihan_menu == "3":
        print("Terima kasih. Keluar dari program.")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih kembali.")