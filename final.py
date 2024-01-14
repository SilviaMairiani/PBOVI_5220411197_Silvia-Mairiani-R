import mysql.connector
import os

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="5220411197"
)

class LoketTiket:
    def __init__(self, nama_loket, lokasi):
        self.nama_loket = nama_loket
        self.lokasi = lokasi

    def tambah():
        connect = db.cursor()
        nama_loket = input("Masukkan nama loket penjualan tiket: ")
        lokasi = input("Masukkan lokasi loket: ")
        sql = "INSERT INTO loket(nama_loket, lokasi) VALUES (%s, %s)"
        val = (nama_loket, lokasi)
        connect.execute(sql, val)
        db.commit()
        print("Data berhasil di tambahkan".format(connect.rowcount))

    def cetak():
        connect= db.cursor()
        sql= "SELECT * FROM loket"
        connect.execute(sql)
        results= connect.fetchall()
        if connect.rowcount < 0:
            print("Tidak ada data")
        else:
            for data in results:
                print(data)

    def ubah():
        connect = db.cursor()
        id= input("pilih id data yang akan diubah>")
        nama_loket = input("Masukkan nama baru: ")
        lokasi = input("Masukkan lokasi baru: ")
        sql = "UPDATE loket SET nama_loket=%s, lokasi=%s WHERE id=%s"
        val = (nama_loket, lokasi, id)
        connect.execute(sql, val)
        db.commit()
        print("Data berhasil di ubah".format(connect.rowcount))

    def hapus():
        connect= db.cursor()
        LoketTiket.cetak()
        id=input("pilih id loket>")
        sql="DELETE FROM loket WHERE id=%s"
        val=(id,)
        connect.execute(sql,val)
        db.commit()
        print("Data berhasil di hapus".format(connect.rowcount))

class TiketPesawat(LoketTiket):
    def __init__(self, nama_loket, lokasi, keberangkatan, tujuan, kelas, harga):
        super().__init__(nama_loket, lokasi)
        self.keberangkatan = keberangkatan
        self.tujuan = tujuan
        self.kelas = kelas
        self.harga = harga

    def tambah():
        connect = db.cursor()
        nama_loket = input("Masukkan nama loket penjualan tiket: ")
        lokasi = input("Masukkan lokasi loket: ")
        keberangkatan = input("Masukkan keberangkatan: ")
        tujuan = input("Masukkan tujuan: ")
        kelas = input("Masukkan kelas: ")
        harga = int(input("Masukkan harga: "))
        sql = "INSERT INTO tiket_pesawat(nama_loket, lokasi, keberangkatan, tujuan, kelas, harga) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (nama_loket, lokasi, keberangkatan, tujuan, kelas, harga)
        connect.execute(sql, val)
        db.commit()
        print("Data berhasil di tambahkan".format(connect.rowcount))

    def cetak():
        connect= db.cursor()
        sql= "SELECT * FROM tiket_pesawat"
        connect.execute(sql)
        results= connect.fetchall()
        if connect.rowcount < 0:
            print("Tidak ada data")
        else:
            for data in results:
                print(data)

    def ubah():
        connect = db.cursor()
        id= input("pilih id data yang akan diubah>")
        nama_loket = input("Masukkan nama baru: ")
        lokasi = input("Masukkan lokasi baru: ")
        keberangkatan = input("Masukkan kota keberangkatan baru: ")
        tujuan = input("Masukkan kota tujuan baru")
        kelas = input("Masukkan kelas baru: ")
        harga = int(input("Masukkan harga baru: "))
        sql = "UPDATE tiket_pesawat SET nama_loket=%s, lokasi=%s, keberangkatan=%s, tujuan=%s, kelas=%s, harga=%s WHERE id=%s"
        val = (nama_loket, lokasi, keberangkatan, tujuan, kelas, harga, id)
        connect.execute(sql, val)
        db.commit()
        print("Data berhasil di ubah".format(connect.rowcount))

    def hapus():
        connect = db.cursor()
        TiketPesawat.cetak()
        id = input("pilih id loket>")
        sql = "DELETE FROM tiket_pesawat WHERE id=%s"
        val = (id,)
        connect.execute(sql,val)
        db.commit()
        print("Data berhasil di hapus".format(connect.rowcount))

class Penjualan:
    def __init__(self, no_ktp, nama, keberangkatan, tujuan, kelas, harga, banyak, total_harga, nama_loket):
        self.no_ktp = no_ktp
        self.nama = nama
        self.keberangkatan = keberangkatan
        self.tujuan = tujuan
        self.kelas = kelas
        self.harga = harga
        self.banyak = banyak
        self.total_harga = total_harga
        self.nama_loket = nama_loket

    def pembelian_tiket():
        connect = db.cursor()
        no_ktp = int(input("Masukkan no ktp anda: "))
        nama = input("Masukkan nama penumpang: ")
        nama_loket = input("Masukkan nama loket: ")
        keberangkatan = input("Masukkan kota keberangkatan: ")
        tujuan = input("Masukkan kota tujuan: ")
        kelas = input("Masukkan kelas: ")
        harga = int(input("Masukkan harga: "))
        banyak = int(input("Masukkan banyak tiket yang anda beli: "))
        total_harga = harga * banyak
        val = (no_ktp, nama, nama_loket, keberangkatan, tujuan, kelas, harga, banyak)
        sql = "INSERT INTO penjualan(no_ktp, nama, nama_loket, keberangkatan, tujuan, kelas, harga, banyak) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        connect.execute(sql, val)
        db.commit()
        print("Data berhasil disimpan".format(connect.rowcount))
        print('\n----------------------------------------------')
        print('\n                PEMBAYARAN                    ')
        print('\n----------------------------------------------')
        uang=int(input("Masukkan jumlah uang yang dibayarkan: "))
        bayar=(uang-total_harga)
        print("Kembalian: ",bayar)

    def cetak():
        connect = db.cursor()
        sql= "SELECT * FROM penjualan"
        connect.execute(sql)
        results= connect.fetchall()
        if connect.rowcount < 0:
            print("Tidak ada data")
        else:
            for data in results:
                print(data)

    def cari():
        connect = db.cursor()
        keyword=input("Kata kunci:")
        sql="SELECT * FROM penjualan WHERE no_ktp LIKE %s OR nama LIKE %s OR tujuan LIKE %s"
        val=("%{}%".format(keyword), "%{}%".format(keyword), "%{}%".format(keyword))
        connect.execute(sql, val)
        results = connect.fetchall()
        if connect.rowcount < 0:
            print("Tidak ada data")
        else:
            for data in results:
                print(data)

while True:
    print('\n===== MENU UTAMA =====')
    print("1. Loket Tiket")
    print("2. Tiket Pesawat")
    print("3. Penjualan")
    print("0. Keluar")
    print('\n----------------------')
    pilih=int(input("Masukkan Pilihan: "))
    if pilih==1:
        print('\n===== MENU LOKET TIKET =====')
        print("1. Tambah Loket")
        print("2. Lihat Loket")
        print("3. Ubah Loket")
        print("4. Hapus Loket")
        print("0. Kembali ke Menu Utama")
        print('\n----------------------')
        sub_pilih = int(input("Masukkan Pilihan: "))
        if sub_pilih == 1:
            LoketTiket.tambah()
        elif sub_pilih == 2:
            LoketTiket.cetak()
        elif sub_pilih == 3:
            LoketTiket.ubah()
        elif sub_pilih == 4:
            LoketTiket.hapus()
        elif sub_pilih == 0:
            break
        else:
            print("Nomor yang anda inputkan salah!")
    elif pilih == 2:
        while True:
            print('\n===== MENU TIKET PESAWAT =====')
            print("1. Tambah Tiket Pesawat")
            print("2. Lihat Tiket Pesawat")
            print("3. Ubah Tiket Pesawat")
            print("4. Hapus Tiket Pesawat")
            print("0. Kembali ke Menu Utama")
            print('\n----------------------')
            sub_pilih = int(input("Masukkan Pilihan: "))
            if sub_pilih == 1:
                TiketPesawat.tambah()
            elif sub_pilih == 2:
                TiketPesawat.cetak()
            elif sub_pilih == 3:
                TiketPesawat.ubah()
            elif sub_pilih == 4:
                TiketPesawat.hapus()
            elif sub_pilih == 0:
                break
            else:
                print("Nomor yang anda inputkan salah!")
    elif pilih == 3:
        while True:
            print('\n===== MENU PENJUALAN =====')
            print("1. Pembelian Tiket")
            print("2. Lihat Penjualan")
            print("3. Cari Penjualan")
            print("0. Kembali ke Menu Utama")
            print('\n----------------------')
            sub_pilih = int(input("Masukkan Pilihan: "))
            if sub_pilih == 1:
                Penjualan.pembelian_tiket()
            elif sub_pilih == 2:
                Penjualan.cetak()
            elif sub_pilih == 3:
                Penjualan.cari()
            elif sub_pilih == 0:
                break
            else:
                print("Nomor yang anda inputkan salah!")
    elif pilih == 0:
        break
    else:
        print("Nomor yang anda inputkan salah!")
    os.system("pause")