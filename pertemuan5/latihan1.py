#access modifier
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

x = Hewan("Singa", "Harimau", "Kucing")
print("Ini hewan: ", x.var1)
print("Ini hewan kedua: ", x._var2)
# print("Ini hewan ketiga: ", x._Hewan__var3)  #cara pemanggilan private (harus memperhatikan hierarki) diurutkan dari public ke protected baru private. jika menggunakan cara ini tidak perlu menggunakan function display dan akses. -->cara pertama
x.akses()  #cara pemanggilan private kedua. cara ini harus menggunakan function display dan akses.