def layanan():
    nama = str(input("Silahkan inputkan nama layanan yang anda inginkan: "))
    lama = str(input("Silahkan inputkan lama anda akan berlangganan layanan (perbulan/pertahun): "))
    print("---------------------------")
    print("Jenis Layanan Yang Tersedia")
    print("---------------------------")
    print("1. Layanan Tabungan")
    print("2. Layanan Kartu Kredit")
    print("3. Layanan Pinjaman")
    jenis = str(input("Silahkan inputkan nomor jenis layanan yang anda inginkan: "))
    print("Daftar Harga Layanan")
    print("1. perbulan seharga 200000")
    print("2. pertahun seharga 2400000")

def layanan_nasabah():
    print("Selamat Datang Di Menu Layanan Nasabah")
    print("======================================")
    penghasilan = int(input("Silahkan inputkan jumlah penghasilan anda: "))
    total = 0  # Inisialisasi total harga

    if penghasilan > 500000000:
        for i in range(3):
            layanan()
            harga = int(input("Silahkan inputkan harga layanan yang anda pilih: "))
            total += harga  # Akumulasi total harga

    elif 100000000 <= penghasilan <= 500000000:
        for i in range(2):
            layanan()
            harga = int(input("Silahkan inputkan harga layanan yang anda pilih: "))
            total += harga  # Akumulasi total harga

    elif 0 <= penghasilan < 100000000:
        for i in range(1):
            layanan()
            harga = int(input("Silahkan inputkan harga layanan yang anda pilih: "))
            total += harga  # Akumulasi total harga

    else:
        print("Penghasilan yang anda inputkan salah")

    print("Total harga yang harus anda bayarkan adalah sebesar RP.", total)

layanan_nasabah()