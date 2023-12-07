class IPK:
     def __init__ (self, nama, nilai, sks):
          self.nama = nama
          self.nilai = nilai
          self.sks = sks
          self.listbbt = []
          self.listsks = []
          self.listbobobtsks = []
     def matkul (self):
          print ("Daftar Mata Kuliah")
          print ("1. Matematika & Statistika")
          print ("2. Pemrograman Wen & Mobile")
          pilih = int (input ("Inputkan nomor Mata Kuliah"))
          if pilih == 1:
               nama_matkul = "Matematika & Statistika"
          elif pilih == 2:
               nama_matkul = "Pemrograman Wen & Mobile"
          nama_matkul = self.nama
          return nama_matkul
     def bobot (self):
          bobot_nilai = int (input ("Silahkan inputkan nilai anda: "))
          if bobot_nilai >= 81:
               bbt = 4
          elif 81 < bobot_nilai >= 61:
               bbt = 3
          elif 61 < bobot_nilai >= 41:
               bbt = 2
          elif 41 < bobot_nilai >= 21:
               bbt = 1
          elif 21 < bobot_nilai >= 0:
               bbt = 0
          else:
               print ("Nilai yang anda inputkan salah!")
          list_bbt = []
          list_bbt = self.listbbt
          self.listbbt.append(bbt)
          return bobot_nilai
     def bobot_sks (self):
          sks = int (input ("Silahkan inputkan jumlah SKS anda: "))
          sks = self.listsks
          lix = self.listbbt
          print (self.listbbt)
          if sks == 1:
               list_bbt = lix * 1
               sks.appand(1)
          elif sks == 2:
               list_bbt = lix * 2
               sks.appand(2)
          elif sks == 3:
               list_bbt = lix * 3
               sks.appand(3)
          list = []
          list = self.listbobobtsks
          list.append(list_bbt)
          return list_bbt
     def total_bs(self):
          bs = sum (self.listbobobtsks)
          return bs
     def total_sks(self):
          sks = sum (self.listsks)
          return sks

main = IPK (0,0,0)
def hasil_akhir ():
     hasil = main.total_bs()/main.total_sks()
     print (hasil)

main.matkul()
main.bobot()
main.bobot_sks()
hasil_akhir()
     
# # nama = 'alpro'
# # nama2 = 'mtk'
# nilai = 90
# # nilai2 = 80
# sks = 3
# # sks2 = 2

# nilai_akhir = IPK (nilai, sks,)
# print ("IPK anda pada semester ini adalah: ", nilai_akhir.hasil (nilai_akhir.nama, nilai, sks))