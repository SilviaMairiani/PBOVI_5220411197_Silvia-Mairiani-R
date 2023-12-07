#overriding --> penggunaan nama function yang sama antara kelas induk dan turunan
class Matakuliah:
     def __init__(self, nama, semester):
          self.nama = nama
          self.sem = semester

     def tampil(self):
          print("Nama mhs: ", self.nama, "semester", self.sem)

     #overloading  --> penggunaan nama function yang sama dalam satu kelas
     def tampil(self, modul = None):
          if modul != None:
               harga = modul
               print("Nama mhs: ", self.nama, "semester", self.sem, "Harga modul Rp", harga, "Pembayaran lunas")
          else:
               harga = modul
               print("Nama mhs: ", self.nama, "semester", self.sem, "Harga modul Rp", harga, "Pembayaran belum lunas")

class Dosen(Matakuliah):
     def __init__(self, nama, semester, dosen):
          super().__init__(nama, semester)
          self.dosen = dosen

     def tampil(self, modul = None):
          if modul != None:
               harga = modul
               print("Nama mhs: ", self.nama, "Dosen pengampu", self.dosen, "semester", self.sem, "Harga modul Rp", harga, "Pembayaran lunas")
          else:
               harga = modul
               print("Nama mhs: ", self.nama, "Dosen pengampu", self.dosen, "semester", self.sem, "Harga modul Rp", harga, "Pembayaran belum lunas")

obj = Matakuliah("PBO", 3)
obj2 = Dosen("Alpro", 1, "Enny")
obj.tampil()
obj.tampil(60000)
obj2.tampil()