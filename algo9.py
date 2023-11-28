def buat_file(nama_file):
    with open(nama_file, "w") as file:
        file.write("")

def baca_file(nama_file):
    with open(nama_file, "r") as file:
        return file.read()

def tambah_text(nama_file, text):
    with open(nama_file, "a") as file:
        file.write(text)    

def main():
    print("===== Program File Handling =====")
    print("1. Membuat dan Menulis File")
    print("2. Membaca File")
    print("3. Menambahkan Text Pada File")
    print("4. Keluar Dari Program")

    while True:
        pilihan = input("Masukkan Pilihan Berupa Angka (1/2/3/4): ")

        if pilihan == "1":
            nama_file = input("Masukkan Nama File: ")
            buat_file(nama_file)

        elif pilihan == "2":
            nama_file = input("Masukkan Nama File: ")
            text = baca_file(nama_file)
            print(text)

        elif pilihan == "3":
            nama_file = input("Masukkan Nama File: ")
            nama_teman = input("Masukkan Nama Sahabatmu: ")
            catatan_tambahan = input("Masukkan Catatan Tambahan kamu: ")
            tambah_text(nama_file, f"Nama Sahabatku: {nama_teman}\nCatatan Tambahan: {catatan_tambahan}")
            print("Data Berhasil Ditambahkan")

        elif pilihan == "4":
            break

        else:
            print("Pilihan tidak valid!")
main()
