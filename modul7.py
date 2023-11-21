def is_prima(bilangan):
    return bilangan > 1 and all(bilangan % i != 0 for i in range(2, int(bilangan**0.5) + 1))

bilangan = int(input("Masukkan angka: "))

if is_prima(bilangan):
    print("{} adalah bilangan prima.".format(bilangan))
else:
    print("{} bukan bilangan prima.".format(bilangan))
