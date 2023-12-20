import pandas as pd

df = pd.DataFrame({
    "Ibu Kota": ["Jakarta", "Tokyo", "New Delhi", "Beijing", "Washington DC", "Brasilia", "Moscow", "Mexico City", "Abuja", "Berlin", "Algiers", "London"],
    "Benua": ["Asia", "Asia", "Asia", "Asia", "Amerika", "Amerika", "Asia", "Amerika", "Afrika", "Eropa", "Afrika", "Eropa"],
    "Luas": [1905, 377, 3287, 9597, 9834, 8515, 17098, 1964, 923, 357, 2381, 242],
    "Populasi": [264, 143, 1252, 1357, 329, 210, 146, 126, 200, 83, 43, 66]
})

mean = df.groupby("Benua").mean()[["Luas", "Populasi"]]
std = df.groupby("Benua").std()[["Luas", "Populasi"]]

mean.to_csv("mean.csv")
std.to_csv("std.csv")

print("Berikut Data Mean:")
print(mean)
print("Berikut Data Standard Deviation:")
print(std)
print("File Berhasil Dibuat")