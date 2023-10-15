# Percobaan 1

print("## Program Python menghitung gaji karyawan ##")
print("==================================")
print()

#proses input
nama = input("Nama karyawan : ")
golongan = input("Golongan : ")
jam_kerja = int(input("Jumlah jam kerja :"))

print()

#Tentukan jumlah upah per jam berdasarkan golongan

if golongan == "A":
    upah_per_jam = 5000
elif golongan == "B":
    upah_per_jam = 7000
elif golongan == "C":
    upah_per_jam = 8000
elif golongan == "D":
    upah_per_jam = 10000

    total_upah = jam_kerja * upah_per_jam

# Cek apakah jam kerja lebih dari 48 jam
if (jam_kerja - 48) > 0:
    total_upah = total_upah + ((jam_kerja - 48)*4000)

#Proses output
print(nama, "Menerima upah Rp.", total_upah, "per minggu")