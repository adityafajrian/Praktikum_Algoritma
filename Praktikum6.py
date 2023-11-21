def hitung_rata_rata_nilai(nilai_A, nilai_C):
    return (nilai_A + nilai_C) / 2

nilai_A, nilai_C = 0, 0

while True:
    kategori_huruf = input("Masukkan Huruf: ").upper()
    if not kategori_huruf:
        break
    nilai = int(input("Nilai = "))
    if kategori_huruf == 'A':
        nilai_A += nilai
    elif kategori_huruf == 'C':
        nilai_C += nilai

rata_rata = hitung_rata_rata_nilai(nilai_A, nilai_C)
print("Rata-ratanya adalah:", rata_rata)
