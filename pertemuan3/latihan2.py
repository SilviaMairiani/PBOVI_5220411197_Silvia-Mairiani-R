class Bidang:
     def __init__ (self, x, y, z):
          self.xx = x
          self.yy = y 
          self.zz = z
     def hitungLuas (self):
          luas = self.xx*self.yy*self.zz
          return luas
     def bintang ():
          print ("*"*15)

sisi = int (input ("Masukkan sisi atau lebar = "))
panjang = int (input ("Masukkan panjang = "))
jari = int (input ("Masukkan jari-jari = "))
Bidang.bintang()

persegi = Bidang(sisi,sisi,1)
persegipanjang = Bidang(panjang,sisi,1)
segi3 = Bidang(panjang,sisi,0.5)
lingkaran = Bidang(jari,jari,3.14)

print("Luas persegi",persegi.hitungLuas())
print("Luas persegi panjang",persegipanjang.hitungLuas())
print("Luas segitiga",segi3.hitungLuas())
print("Luas lingkaran",lingkaran.hitungLuas())