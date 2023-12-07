# inheritance/pewarisan
class Hewan:
     var1 = None #public
     _var2 = None #protected
     __var3 = None #private

     def __init__(self, var1, var2, var3):
          self.var1 = var1
          self._var2 = var2
          self.__var3 = var3

     def __display(self):
          print("Ini menampilkan variabel 3:", self.__var3)

     def akses(self):
          self.__display()


class HewanDilindungi(Hewan):
     def __init__(self, var1, var2, var3, var4):
          super().__init__(var1, var2, var3)
          self.var4 = var4

y = HewanDilindungi("Cendrawasih", "Anoa", "Badak Cula 1", "Harimau Sumatera")
print("Ini hewan yang dilindungi kesatu: ", y.var1)
print("Ini hewan yang dilindungi kedua: ", y._var2)
y.akses()
print("Ini hewan yang dilindungi keempat: ", y.var4)