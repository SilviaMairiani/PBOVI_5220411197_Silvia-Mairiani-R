class Katalog:
     def cari(self, judul):
          #mencari informasi dalam katalog dengan kata kunci "judul"
          return f"Mencari informasi tentang '{judul}'..."

class PerpusItem:
     def __init__(self, judul, subjek):
          self.judul = judul
          self.subjek = subjek
          self.katalog = Katalog()

     def LokasiPenyimpanan(self):
          return "Rak A"
     
     def info(self):
          print(f"Judul: {self.judul}")
          print(f"Subjek: {self.subjek}")
          print(f"Lokasi Penyimpanan: {self.LokasiPenyimpanan()}")

     def cari_info(self, judul):
          return self.katalog.cari(judul)
     
class Pengarang:
     def __init__(self, nama):
          self.nama = nama

     def info(self):
          print(f"Nama Pengarang: {self.nama}")

     def cari(self, nama):
          return f"Mencari buku dengan pengarang bernama '{nama}'..."
     
class Buku(PerpusItem):
     def __init__(self, judul, subjek, isbn, pengarang, jumhal, ukuran):
          super().__init__(judul, subjek)
          self.isbn = isbn
          self.pengarang = Pengarang(pengarang)
          self.jumhal = jumhal
          self.ukuran = ukuran

     def info(self):
          super().info()
          self.pengarang.info()
          print(f"ISBN: {self.isbn}")
          print(f"Jumlah Halaman: {self.jumhal}")
          print(f"Ukuran: {self.ukuran}")

class Majalah(PerpusItem):
     def __init__(self, judul, subjek, volume, issue):
          super().__init__(judul, subjek)
          self.volume = volume
          self.issue = issue

     def info(self):
          super().info()
          print(f"Volume: {self.volume}")
          print(f"Issue: {self.issue}")

class DVD(PerpusItem):
     def __init__(self, judul, subjek, aktor, genre):
          super().__init__(judul, subjek)
          self.aktor = aktor
          self.genre = genre

     def info(self):
          super().info()
          print(f"Aktor: {self.aktor}")
          print(f"Genre: {self.genre}")

pengarang= Pengarang("John Arnold")
buku= Buku("Penerapan Aljabaar Linear", "Matematika", "199-1-14-777732-0", "John Arnold", 200, "A5")
majalah= Majalah("Tech Trand", "Technology", "vol.3", "issue 2")
dvd= DVD("Mission Impossible", "Film", "Tom Cruise", "Action")
# item= PerpusItem("Penerapan Aljabaar Linear", "Matematika")
# item.info()
# hasil_cari = item.cari_info("Penerapan Aljabaar Linear")
# print(hasil_cari)
buku.info()
print("\n")
pengarang.cari("John Arnold")

majalah.info()
print("\n")
dvd.info()