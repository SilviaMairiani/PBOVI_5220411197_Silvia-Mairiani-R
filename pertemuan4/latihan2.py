class IPK:
    def __init__(self, nama, nilai, sks):
        self.nama = nama
        self.nilai = nilai
        self.sks = sks

    def hitung_bobot(self):
        bobot = 0 # Inisialisasi bobot dengan 0
        if 81 <= self.nilai <= 100:
            bobot = 4
        elif 61 <= self.nilai <= 80:
            bobot = 3
        elif 41 <= self.nilai >= 60:
            bobot = 2
        elif 21 <= self.nilai >= 40:
            bobot = 1
        elif 0 <= self.nilai >= 20:
            bobot = 0
        else:
            print ("Nilai yang anda inputkan salah!")
        return bobot
    
    def hitung_bobot_sks(self):
        bobot = self.hitung_bobot()
        if bobot >= 0:
            return bobot * self.sks
        else:
            return 0
        
    def main (self):
        matkul = []
        total_sks = 0
        jumlah_matkul = int(input("Masukkan jumlah mata kuliah: "))
        total_bobot_sks = 0

        for i in range (jumlah_matkul):
            nama = str (input ("Silahkan Inputkan Nama Mata Kuliah Anda: "))
            nilai = int (input ("Silahkan Inputkan Nilai Anda: "))
            sks = int (input ("Silahkan Inputkan SKS Anda: "))
            total_sks += sks
            matkul.append(IPK(nama, nilai, sks))
            total_bobot_sks += matkul[-1].hitung_bobot_sks()
        
        ipk = total_bobot_sks / total_sks
        print ("IPK Anda Adalah: ",ipk)   
       
if __name__ == "__main__":
    mulai = IPK("",0,0)
    mulai.main()