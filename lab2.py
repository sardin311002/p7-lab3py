# Praktikum 3 - Latihan 2 - Pertemuan 7

print("Tugas Pertemuan 7 - Praktikum 3 - Latihan 2")

xangka=0
while True:
    xbilangan = int(input("Masukkan Bilangan : "))
    if (xangka < xbilangan):
        xangka=xbilangan
    if (xbilangan == 0):
        break

print("Bilangan terbesar adalah: ",xangka)
print()