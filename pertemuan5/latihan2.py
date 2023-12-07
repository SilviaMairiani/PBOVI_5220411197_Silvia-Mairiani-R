class Matkul:
     matkul1 = None
     _matkul2 = None
     __matkul3 = None
     __matkul4 = None

     def __init__(self, matkul1, matkul2, matkul3, matkul4):
          self.matkul1 = matkul1
          self._matkul2 = matkul2
          self.__matkul3 = matkul3
          self.__matkul4 = matkul4

     def __display(self):
          print("Ini menampilkan variabel 3:", self.__matkul3)
          print("Ini menampilkan variabel 4:", self.__matkul4)

     def akses(self):
          self.__display()

# y = Matkul("Matematika", "Fisika", "Biologi", "Kimia")
# print("Ini Mata Kuliah kesatu: ", y.matkul1)
# print("Ini Mata Kuliah kedua: ", y._matkul2)
# print("Ini Mata Kuliah ketiga: ", y._Matkul__matkul3)
# y.akses()

class MatkulDihindari(Matkul):
     def __init__(self, matkul1, matkul2, matkul3, matkul4, matkul5):
          super().__init__(matkul1, matkul2, matkul3, matkul4)
          self.matkul5 = matkul5

y = MatkulDihindari("Matematika", "Alpro", "Kalkulus", "Biologi", "Kimia")
print("Matkul yang dihindari: ", y.matkul1)
print("Matkul yang dihindari kedua: ", y._matkul2)
y.akses()
print("Matkul yang dihindari kelima: ", y.matkul5)