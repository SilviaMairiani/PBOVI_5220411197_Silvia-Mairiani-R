print("=====================================================")
nama = str(input("Masukkan Nama Anda: "))
nomor=int(input("Masukkan Nomor Kamar Anda: "))
def kos():
    print("============================")
    print("        KATEGORI KOS        ")
    print("============================")
    print("1. Premium")
    print("2. Exclusive")
    print("3. Reguler")
    print("============================")
    kategori=int(input("Pilih Kategori Kos Anda: "))
    if kategori==1:
        print("Kategori Kos Yang Anda Pilih Adalah Premium")
        print("Metode pembayaran Dengan Cicilan 3x 1 tahun")
        for i in range(3):
            cicilan=int(input("Masukkan Jumlah Pembayaran Anda: "))
            a= cicilan
            b= cicilan
            c= cicilan
            print(f"cicilan ke-{i+1}")
            total= a+b+c
        print("total pembayaran: ",total)
    elif kategori==2:
        print("Kategori Kos Yang Anda Pilih Adalah Exclusive seharga 6.000.000")
        print("Metode pembayaran Dengan Cicilan 4x 1 tahun")
        for i in range(4):
            cicilan=int(input("Masukkan Jumlah Pembayaran Anda: "))
            a= cicilan
            b= cicilan
            c= cicilan
            d= cicilan
            print(f"cicilan ke-{i+1}")
            total= a+b+c+d
        print("total pembayaran: ",total)
    elif kategori==3:
        print("Kategori Kos Yang Anda Pilih Adalah Reguler seharga 3.000.000")
        print("Metode pembayaran Dengan Cicilan 6x 1 tahun")
        for i in range(6):
            cicilan=int(input("Masukkan Jumlah Pembayaran Anda: "))
            a= cicilan
            b= cicilan
            c= cicilan
            d= cicilan
            e= cicilan
            f= cicilan
            print(f"cicilan ke-{i+1}")
            total= a+b+c+d+e+f
        print("total pembayaran: ",total)
    else:
        print("Kategori Yang Anda Pilih Tidak Tersedia")
kos()