class RentalKamera:
    jenis = None
    _harga = None
    __lama = None

    def __init__(self, jenis, harga, lama):
        self.jenis = jenis
        self._harga = harga
        self.__lama = lama

class Pembayaran(RentalKamera):
    def __init__(self, jenis, harga, lama):
        super().__init__(jenis, harga, lama)

    def hitung_biaya_sewa(self):
        harga = 0
        if self.jenis == 1:
            harga = 200000
        elif self.jenis == 2:
            harga = 300000
        elif self.jenis == 3:
            harga = 350000
        else:
            print ("Nomor yang anda inputkan salah!")
        return harga
        
    def main (self):
        total_keseluruhan = 0
        while True:
            print("Menu Rental Kamera")
            print("------------------")
            print("Daftar Jenis Kamera")
            print("1. DSLR")
            print("2. Mirrorless")
            print("3. Action Cam")
            jenis = int (input ("Silahkan masukkan jenis kamera yang anda inginkan: "))
            lama = int (input ("Silahkan masukkan lama hari sewa anda: "))

            kamera = Pembayaran(jenis, 0, lama)  # Menginisialisasi objek Pembayaran

            total_biaya_sewa = kamera.hitung_biaya_sewa() * kamera._RentalKamera__lama
            total_keseluruhan += total_biaya_sewa
            print("Total biaya sewa: ", total_biaya_sewa)

            lagi = input("Ingin merental kamera lagi? (ya/tidak): ")
            if lagi.lower() != "ya":
                break

        print("\nTotal keseluruhan harga sewa: ", total_keseluruhan)
        print("Terimakasih telah menggunakan program ini.")

if __name__ == "__main__":
    mulai = Pembayaran(0,0,0)
    mulai.main()