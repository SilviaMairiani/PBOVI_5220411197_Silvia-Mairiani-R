def konsentrasi():
    print("  Selamat Datang Di Menu Pemilihan Konsentrasi  ")
    print("================================================")
    nama= str(input("Silahkan inputkan nama anda: "))
    npm= int(input("Silahkan inputkan NPM anda: "))
    print("======================")
    print("  DAFTAR KONSENTRASI  ")
    print("----------------------")
    print("  1. Sistem Cerdas")
    print("  2. Web & Mobile")
    print("======================")
    nilai= int(input("Silahkan inputkan nilai matematika anda: "))
    if 0 <= nilai < 75:
        print("Berdasarkan nilai matematika anda, anda mendapatkan konsentrasi Sistem Cerdas")
    elif 75 <= nilai <= 100:
        print("Berdasarkan nilai matematika anda, anda mendapatkan konsentrasi Web & Mobile")
    else:
        print("Nilai yang anda inputkan salah")

konsentrasi()