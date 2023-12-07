class karyawan:
     def __init__(self, nama, jabatan, gaji):
        self.nama = nama
        self.jabatan = jabatan
        self.gaji = gaji

     def hitung_gaji(self):
         return self.gaji
     
class karyawanFullTime(karyawan):
     def __init__(self, nama, jabatan,gaji):
         super().__init__(nama, jabatan, gaji)

     def hitung_gaji(self):
         return self.gaji
     
class karyawanPartTime(karyawan):
     def __init__(self, nama, jabatan, gaji, jam_kerja, jam_lembur):
         super().__init__(nama, jabatan, gaji)
         self.gaji_perjam = 15000
         self.jam_kerja = jam_kerja
         self.jam_lembur = jam_lembur

     def hitung_lembur(self, jam_lembur):
         tarif_lembur = 10000
         return jam_lembur * tarif_lembur

     def hitung_gaji(self):
         if self.jam_kerja <= 40:
             return self.jam_kerja * self.gaji_perjam
         else:
             gaji = 40 * self.gaji_perjam
             gaji_lembur = self.hitung_lembur(self.jam_lembur)
             return gaji + gaji_lembur
         
     # def hitung_lembur(self, jam_lembur):
     #     tarif_lembur = 10000
     #     return jam_lembur * tarif_lembur
     
karyawan_fulltime = karyawanFullTime("Niki", "Manager", 600000)
karyawan_parttime = karyawanPartTime("Sela", "kasir", 15000, 45, 5)
gaji_fulltime = karyawan_fulltime.hitung_gaji()
gaji_parttime = karyawan_parttime.hitung_gaji() 

print("Nama: ", karyawan_fulltime.nama)
print("Jabatan: ", karyawan_fulltime.jabatan)
print("Gaji: ", gaji_fulltime)

print("Nama: ", karyawan_parttime.nama)
print("Jabatan: ", karyawan_parttime.jabatan)
print("Gaji: ", gaji_parttime)