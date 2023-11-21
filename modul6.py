def cek_kabisat(tahun):
    return tahun % 4 == 0 and (tahun % 100 != 0 or tahun % 400 == 0)

def jumlah_hari_dalam_bulan(bulan, tahun):
    daftar_bulan = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if bulan == 2 and cek_kabisat(tahun):
        return 29
    else:
        return daftar_bulan[bulan - 1]

while True:
    bulan = int(input("Masukkan bulan (1-12): "))
    
    if bulan == 0:
        break
    
    tahun = int(input("Masukkan tahun: "))
    
    jumlah_hari = jumlah_hari_dalam_bulan(bulan, tahun)

    print(f"{jumlah_hari} hari dalam sebulan")
    print("masukkan 0 untuk menghentikan program")
