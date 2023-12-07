print("=====================================================")
nama = str(input("Masukkan Nama Anda: "))
npm=int(input("Masukkan NPM Anda: "))
ipk = float(input("Masukkan Nilai IPK Anda: "))
def pengambilanMatkul():
    if 3.5 <= ipk <= 4.0:
        jumlah_matkul = 6
        matkul = ["Matematika", "Fisika", "Kimia", "Biologi", "Ekonomi", "Manajemen "]
    elif 3.0 <= ipk < 3.5:
        jumlah_matkul = 4
        matkul = ["Matematika", "Fisika", "Kimia", "Biologi"]
    elif 2.5 <= ipk < 3.0:
        
        jumlah_matkul = 3
        matkul = ["Matematika", "Fisika", "Kimia"]
    else:
        jumlah_matkul = 2
        matkul = ["Matematika", "Fisika"]


    print(f"Anda dapat mengambil {jumlah_matkul} mata kuliah.")
    print("Berikut adalah pilihan mata kuliah yang dapat Anda ambil:")
    for i, item in enumerate(matkul, start=1):
        print(f"{i}. {item}")

pengambilanMatkul()