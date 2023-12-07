print("=====================================================")
nama = str(input("Masukkan Nama Anda: "))
npm=int(input("Masukkan NPM Anda: "))
ipk = float(input("Masukkan Nilai IPK Anda: "))
def pengambilanMatkul():
    matkul = ["Matematika", "Fisika", "Kimia", "Biologi", "Ekonomi", "Manajemen"]
    if 3.5 <= ipk <= 4.0:
        jumlah_matkul = 6
     #    for i in range (6):
     #        pilihMatkul= int(input("Masukkan Mata Kuliah Pilihan Anda: "))
    elif 3.0 <= ipk < 3.5:
        jumlah_matkul = 4
    elif 2.5 <= ipk < 3.0:
        jumlah_matkul = 3
    else:
        jumlah_matkul = 2


    print(f"Anda dapat mengambil {jumlah_matkul} mata kuliah.")
    print("=================================")
    print("    MATA KULIAH YANG TERSEDIA    ")
    print("1. Matematika")
    print
    print("=================================")
    
    for i, item in enumerate(matkul, start=1):
        print(f"{i}. {item}")

pengambilanMatkul()
