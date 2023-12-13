class Mahasiswa:
    def __init__(self, nama=None, nilai=None):
        self.nama = nama
        self.nilai = nilai

    def get_nama(self):
        return self.nama

    def set_nama(self, nama):
        self.nama = nama

    def get_nilai(self):
        return self.nilai

    def set_nilai(self, nilai):
        self.nilai = nilai

def tampilkan_menu():
    print("=== Program OOP===")
    print("1. Mendeklarasikan Objek")
    print("2. Menampilkan Objek")
    print("3. Merubah Nilai Objek")
    print("4. Menghapus Objek")
    print("5. Keluar Dari Program")

def deklarasi_objek():
    nama = input("Masukkan Namamu: ")
    nilai = input("Masukkan Nilaimu: ")
    mahasiswa = Mahasiswa(nama, nilai)
    print("Data Berhasil Ditambahkan \n")
    return mahasiswa

def tampilkan_objek(mahasiswa):
    if mahasiswa is not None:
        print("Nama:", mahasiswa.get_nama())
        print("Nilai:", mahasiswa.get_nilai())
        print()
    else:
        print("Objek belum dideklarasikan. Harap deklarasikan objek terlebih dahulu.")

def merubah_data(mahasiswa):
    apa_diubah = input("Apa yang ingin diubah (Nama/Nilai): ")
    
    if apa_diubah.lower() == "nama":
        new_nama = input("Masukkan Nama Baru: ")
        mahasiswa.set_nama(new_nama)
        print("Data Nama Berhasil Dirubah \n")
    elif apa_diubah.lower() == "nilai":
        new_nilai = input("Masukkan Nilai Baru: ")
        mahasiswa.set_nilai(new_nilai)
        print("Data Nilai Berhasil Dirubah \n")
    else:
        print("Pilihan tidak valid. Silakan pilih 'Nama' atau 'Nilai'.")

def hapus_objek(mahasiswa):
    mahasiswa.set_nama(None)
    mahasiswa.set_nilai(None)
    print("Objek berhasil dihapus \n")

mahasiswa = None

pilihan = 0
while pilihan != 5:
    tampilkan_menu()
    pilihan = int(input("Masukkan Pilihan Berupa Angka (1/2/3/4/5): "))

    if pilihan == 1:
        mahasiswa = deklarasi_objek()
    elif pilihan == 2:
        tampilkan_objek(mahasiswa)
    elif pilihan == 3:
        if mahasiswa is not None:
            merubah_data(mahasiswa)
        else:
            print("Objek belum dideklarasikan. Harap deklarasikan objek terlebih dahulu.")
    elif pilihan == 4:
        if mahasiswa is not None:
            hapus_objek(mahasiswa)
        else:
            print("Objek belum dideklarasikan. Harap deklarasikan objek terlebih dahulu.")
    elif pilihan == 5:
        print("Keluar dari program")
    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")
