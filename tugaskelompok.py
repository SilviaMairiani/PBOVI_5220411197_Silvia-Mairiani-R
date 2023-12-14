# KELOMPOK 5
# 1. Syaafi'atul Faatihah (5220411175)
# 2. Silvia Mairiani R (5220411197)
# 3. Glanes Cindy T (5220411219)

import os

class KendaraanDarat:
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang):
        self.TahunKeluaran = tahun_keluaran
        self.Nama = nama
        self.Warna = warna
        self.Kecepatan = kecepatan
        self.BahanBakar = bahan_bakar
        self.JumlahRoda = jumlah_roda
        self.KapasitasPenumpang = kapasitas_penumpang

    def informasi(self):
        print(
            f"{self.Nama} ({self.TahunKeluaran}), Warna: {self.Warna}, Kecepatan: {self.Kecepatan} km/h, Bahan Bakar: {self.BahanBakar}, Jumlah Roda: {self.JumlahRoda}, Kapasitas Penumpang: {self.KapasitasPenumpang}")


class Kereta(KendaraanDarat):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang,
                 gerbong, jumlah_kursi, jenis_layanan_kereta, rute):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang)
        self.Gerbong = gerbong
        self.JumlahKursi = jumlah_kursi
        self.JenisLayananKereta = jenis_layanan_kereta
        self.Rute = rute

    def tambahRute(self, rute):
        self.Rute.append(rute)

    def kurangiRute(self, rute):
        if rute in self.Rute:
            self.Rute.remove(rute)

    def informasi(self):
        super().informasi()
        print(
            f"Gerbong: {self.Gerbong}, Jumlah Kursi: {self.JumlahKursi}, Layanan: {self.JenisLayananKereta}, Rute: {', '.join(self.Rute)}")


class Mobil(KendaraanDarat):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang,
                 jenis_mobil):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang)
        self.JenisMobil = jenis_mobil
        self.MesinAktif = False

    def startEngine(self):
        if not self.MesinAktif:
            print(f"{self.Nama} engine dihidupkan.")
            self.MesinAktif = True
        else:
            print(f"{self.Nama} engine aktif.")

    def stopEngine(self):
        print(f"{self.Nama} engine mati.")
        self.MesinAktif = False

    def Arah(self, arah):
        if self.MesinAktif:
            print(f"{self.Nama} bergerak {arah}.")
        else:
            print(f"ERROR: {self.Nama} tidak dapat bergerak karena mesin belum menyala.")


class MobilBalap(Mobil):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang,
                 jenis_mobil, front_wing, rear_wing):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang,
                         jenis_mobil)
        self.FrontWing = front_wing
        self.RearWing = rear_wing

    def race(self):
        if self.MesinAktif and self.Kecepatan > 100:
            print(f"{self.Nama} sedang balapan di lintasan dengan kecepatan {self.Kecepatan} km/h.")
        elif not self.MesinAktif:
            print(f"{self.Nama} tidak dapat balapan karena mesin belum menyala.")
        else:
            print(f"{self.Nama} tidak dapat balapan karena kecepatan tidak mencukupi.")

    def tambahKecepatan(self, kecepatan):
        if self.MesinAktif:
            self.Kecepatan += kecepatan
            print(f"{self.Nama} kecepatan ditambahkan menjadi {self.Kecepatan} km/h.")
        else:
            print(f"ERROR: {self.Nama} tidak dapat meningkatkan kecepatan karena mesin belum menyala.")
    
    def informasi(self):
        super().informasi()
        print(f"Jenis Mobil : {self.JenisMobil}, Front Wing : {self.FrontWing}, Rear Wing : {self.RearWing}")
    

class MobilCrossroad(Mobil):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang,
                 jenis_mobil, sunroof_type, shock_breaker):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang,
                         jenis_mobil)
        self.SunroofType = sunroof_type
        self.ShockBreaker = shock_breaker

    def sunroofTerbuka(self):
        if self.MesinAktif:
            print(f"{self.Nama} sunroof terbuka.")
        else:
            print(f"ERROR: {self.Nama} tidak dapat membuka sunroof karena mesin belum menyala.")

    def sunroofTertutup(self):
        print(f"{self.Nama} sunroof tertutup.")
    def informasi(self):
        super().informasi()
        print(f"Jenis Mobil : {self.JenisMobil}, sunroofType : {self.SunroofType}, ShockBreaker : {self.ShockBreaker}")
    

def menu_mobil_balap(mobil_balap):
    while True:
        print("\nKendaraan Mobil Balap >> ")
        print("1. Tampilkan Informasi Mobil Balap")
        print("2. Aksi Mobil Balap")
        print("3. Kembali ke Menu Mobil")

        choice_balap = input("Pilih tindakan untuk Mobil Balap (1-3): ")
        os.system("cls")

        if choice_balap == "1":
            mobilBalap1.informasi()
        elif choice_balap == "2":
            print("Aksi Mobil Balap:")
            if not mobil_balap.MesinAktif:
                start_engine_choice = input(f"Apakah {mobil_balap.Nama} menyala? (ya/tidak): ")
                if start_engine_choice.lower() == "ya":
                    mobil_balap.startEngine()
                    #menentukan arah mobil setelah mesin dinyalakan dan dijalankan
                    list_arah = []
                    while True:
                        arah = input("Masukkan arah untuk Mobil Balap: ")
                        list_arah.append(arah)
                        lanjut_input = input("Ingin menginputkan lagi? (ya/tidak): ")
                        if lanjut_input.lower() != "ya":
                            break
                    #penggunaan fungsi arah dalam perulangan
                    for arah in list_arah:
                        mobil_balap.Arah(arah)

                    kecepatan_tambahan = int(input("Masukkan penambahan kecepatan untuk balapan: "))
                    mobil_balap.tambahKecepatan(kecepatan_tambahan)
                    mobil_balap.race()
                else:
                    print(f"ERROR: {mobil_balap.Nama} tidak dapat balapan karena mesin belum menyala.")
            else:
                print("Aksi Mobil Balap:")
                mobil_balap.tampilkan_aksi()
        elif choice_balap == "3":
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")


def menu_mobil_Crossroad(mobil_offroad):
    while True:
        print("="*30)
        print("\nKendaraan Mobil Crossroad >> ")
        print("1. Tampilkan Informasi Mobil Crossroad")
        print("2. Aksi Mobil Crossroad")
        print("3. Kembali ke Menu Mobil")
        print("="*30)

        choice_offroad = input("Pilih tindakan untuk Mobil Crossroad (1-3): ")
        os.system("cls")
        if choice_offroad == "1":
            mobilCrossroad1.informasi()
        elif choice_offroad == "2":
            print("Aksi Mobil Crossroad:")
            if not mobil_offroad.MesinAktif:
                start_engine_choice = input(f"Apakah {mobil_offroad.Nama} menyala? (ya/tidak): ")
                if start_engine_choice.lower() == "ya":
                    mobil_offroad.startEngine()
                    sunroof_action = input("Pilih aksi untuk sunroof (buka/tutup): ")
                    if sunroof_action.lower() == "buka":
                        mobil_offroad.sunroofTerbuka()
                    elif sunroof_action.lower() == "tutup":
                        mobil_offroad.sunroofTertutup()
                    else:
                        print("Pilihan tidak valid.")
                else:
                    print(f"ERROR: {mobil_offroad.Nama} tidak dapat mengoperasikan sunroof karena mesin belum menyala.")
            else:
                sunroof_action = input("Pilih aksi untuk sunroof (buka/tutup): ")
                if sunroof_action.lower() == "buka":
                    mobil_offroad.sunroofTerbuka()
                elif sunroof_action.lower() == "tutup":
                    mobil_offroad.sunroofTertutup()
                else:
                    print("Pilihan tidak valid.")
        elif choice_offroad == "3":
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")
            os.system("cls")


def menu_mobil(mobil_balap, mobil_offroad):
    while True:
        print("\nKendaraan Mobil >> ")
        print("1. Menu Mobil Balap")
        print("2. Menu Mobil Crossroad")
        print("3. Kembali ke Menu Utama")

        choice_mobil = input("Pilih jenis kendaraan (1-3): ")
        os.system("cls")

        if choice_mobil == "1":
            menu_mobil_balap(mobil_balap)
        elif choice_mobil == "2":
            menu_mobil_Crossroad(mobil_offroad)
        elif choice_mobil == "3":
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")


# Contoh penggunaan objek
kereta1 = Kereta(2020, "Kereta Api Express", "Merah", 250, "Solar", 16, 200, "Eksekutif", 50, "Pariwisata",
                ["Jakarta", "Bandung"])
mobilBalap1 = MobilBalap(2022, "Ferrari", "Merah", 0, "Bensin", 4, 2, "Mobil Balap", "Force India VJM09", "SubaruWRX STI S209")
mobilCrossroad1 = MobilCrossroad(2021, "Jeep Wrangler", "Hitam", 0, "Bensin", 4, 5, "Mobil Crossroad", "Wrangler Electric Sunroof", "Kayaba Ultra")

while True:
    print("<< Menu Utama >>")
    print("1. Informasi Keseluruhan Kendaraan Darat")
    print("2. Kendaraan Kereta")
    print("3. Kendaraan Mobil")
    print("4. Keluar")

    choice_main = input("Pilih jenis kendaraan (1-3): ")
    os.system("cls") 

    if choice_main == "1":
        print("\nInformasi Keseluruhan Kendaraan Darat:")
        kereta1.informasi()
        mobilBalap1.informasi()
        mobilCrossroad1.informasi()

    elif choice_main == "2":
        while True:
            print("\nKendaraan Kereta >>")
            print("1. Tampilkan Informasi Kereta")
            print("2. Tambah Rute Kereta")
            print("3. Kurangi Rute Kereta")
            print("4. Kembali ke Menu Utama")

            choice_kereta = input("Pilih tindakan (1-4): ")
            os.system("cls")
            if choice_kereta == "1":
                kereta1.informasi()
            elif choice_kereta == "2":
                rute_baru = input("Masukkan rute baru untuk Kereta: ")
                kereta1.tambahRute(rute_baru)
            elif choice_kereta == "3":
                rute_diambil = input("Masukkan rute yang akan dihapus dari Kereta: ")
                kereta1.kurangiRute(rute_diambil)
            elif choice_kereta == "4":
                break
            else:
                print("Pilihan tidak valid. Silakan pilih lagi.")
            

    elif choice_main == "3":
        menu_mobil(mobilBalap1, mobilCrossroad1)

    elif choice_main == "4":
        print("Program berakhir.")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")