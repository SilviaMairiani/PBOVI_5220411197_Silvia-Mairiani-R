class Kucing:
     def __init__(self, nama, jenis, usia):
          self.nama = nama
          self.jenis = jenis
          self.usia = usia

     def tampil(self):
          print("Nama hewan: ", self.nama, "jenis", self.jenis, "usia", self.usia)

     #overloading  --> penggunaan nama function yang sama dalam satu kelas
     def tampil(self, harga):
          if harga > 0:
               print("Data Hewan")
               print("Nama: ", self.nama)
               print("jenis: ", self.jenis)
               print("usia:", self.usia)
               print("Harga Rp", harga)
          else:
               print("Data Hewan")
               print("Nama: ", self.nama)
               print("jenis: ", self.jenis)
               print("usia:", self.usia)
               print("Harga Rp", harga)

class Pembeli(Kucing):
     def __init__(self, nama, jenis, usia, pembeli):
          super().__init__(nama, jenis, usia)
          self.pem = pembeli

     def tampil(self, harga):
          if harga > 0:
               print("Data Pembelian")
               print("Nama Pembeli: ", self.pem)
               print("Nama kucing: ", self.nama)
               print("jenis: ", self.jenis)
               print("usia: ", self.usia)
               print("Harga Rp", harga)
               print("Pembayaran lunas")
          else:
               print("Data Pembelian")
               print("Nama Pembeli: ", self.pem)
               print("Nama kucing: ", self.nama)
               print("jenis: ", self.jenis)
               print("usia: ", self.usia)
               print("Harga Rp", harga)
               print("Pembayaran belum lunas")
               
obj = Kucing("kitty", "anggora", 3)
obj2 = Pembeli("kitty", "anggora", 3, "Bella")
obj.tampil(harga=300000)
obj2.tampil(harga=0)