# File ini digunakan untuk Tugas Latihan 1 pada materi Praktikum 3

n=int(input("Masukkan Nilai N : "))

import random

for x in list(range(1, n+1, 1)):
    print(f"Data ke: {x} ->",random.uniform(0, 0.5))

print()

print("==============================")
print("= Nama  : Sardin             =")
print("= NIM   : 312010135          =")
print("= Kelas : TI.20.A.1          =")
print("==============================")
