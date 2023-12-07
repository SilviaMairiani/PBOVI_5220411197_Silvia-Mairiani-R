def presiden():
    print("Selamat Datang Di Menu Pemilihan Presiden")
    print("-----------------------------------------")
    nama= str(input("Silahkan inputkan nama anda: "))
    nik= int(input("Silahkan inputkan NIK anda: "))
    print("\n=====================")
    print(" DAFTAR CALON PRESIDEN ")
    print("-----------------------")
    print(" 1. Naruto")
    print(" 2. Sasuke")
    print(" 3. Ryoma")
    print("=======================")
    pilih= int(input("\nMasukkan Nomor Calon Presiden Yang Akan Anda Pilih: "))
    if pilih==1:
        print("Anda telah memilih calon nomor 1. Naruto sebagai Presiden")
    elif pilih==2:
        print("Anda telah memilih calon nomor 2. Sasuke sebagai Presiden")
    elif pilih==3:
        print("Anda telah memilih calon nomor 3. Ryoma sebagai Presiden")
    else:
        print("Nomor yang anda masukkan salah")

presiden()