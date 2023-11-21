def perpangkatan(angka, pangkat):
    if pangkat < 0:
        return 1 / (angka ** pangkat)
    else:
        return angka ** pangkat

angka = int(input("Masukkan Angka: "))
pangkat = int(input("Masukkan Pangkatnya: "))

hasil_perpangkatan = perpangkatan(angka, pangkat)

print("Hasilnya adalah:", hasil_perpangkatan)
