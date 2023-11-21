#NAMA ADITYA FAJRIAN ARYADEVA
#NIM 065002300015

nilai_huruf = {
    'A': 4.00,
    'A-': 3.75,
    'B+': 3.50,
    'B': 3.00,
    'B-': 2.75,
    'C+': 2.50,
    'C': 2.00,
    'C-': 1.75,
    'D': 1.50,
    'E': 1.25
}

total_nilai = 0
total_bobot = 0

while True:
    input_huruf = input("Masukkan nilai huruf (Enter untuk hitung rata-rata):")
    
    if input_huruf == "":
        break

    if input_huruf in nilai_huruf:
        nilai = nilai_huruf[input_huruf]
        total_nilai += nilai
        total_bobot += 1
        print("nilai =", nilai)
    else:
        print("Nilai tidak valid")

if total_bobot == 0:
    print("Tidak ada nilai yang dimasukkan.")
else:
    rata_rata = total_nilai / total_bobot
    print("Rata-rata nya adalah:", rata_rata)
