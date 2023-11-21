#NAMA ADITYA FAJRIAN ARYADEVA
#NIM 065002000315

while True:
    bulan = int(input("Masukkan bulan 1-12: "))
    tahun = int(input("Masukkan tahun: "))

    hari_dalam_bulan = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        hari_dalam_bulan[2] = 29

    while bulan < 1 or bulan > 12:
        bulan = int(input("Masukkan bulan 1-12: "))

    print("Jumlah hari di bulan", bulan, "tahun", tahun, "adalah", hari_dalam_bulan[bulan], "hari")
    
    lagi = input("ketik apapun untuk lanjut (ketik 't' untuk berhenti): ")
    if lagi.lower() == 't':
        break

