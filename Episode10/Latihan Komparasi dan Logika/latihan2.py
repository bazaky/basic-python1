# episode latihan logika dan komparasi

# membuat gabungan area rentang dari angka

# -----0+++++5-----8+++++11-----

inputuser = float(input("masukan angka yang bernilai\nlebih dari 0 dan kurang dari 5\natau \nlebih besar dari 8 dan kurang dari 11\n:"))

# -----0+++++5-----
# Memeriksa angka lebih dari 0 dan kurang dari 5
angka_pertama = inputuser > 0 and inputuser < 5
print("Lebih dari 0 dan kurang dari 5 =", angka_pertama)

print()

# -----8+++++11-----
# Memeriksa angka lebih dari 8 dan kurang dari 11
angka_kedua = inputuser > 8 and inputuser < 11
print("Lebih dari 8 dan kurang dari 1 =", angka_kedua)

print()
# -----0+++++5-----8+++++11-----
# Operasi or

iscorrect = angka_pertama or angka_kedua
print("Angka yang anda masukkan : ", iscorrect)

print()
# -----0+++++5-----8+++++11-----
# Operasi and

iscorrect = angka_pertama and angka_kedua
print("Angka yang anda masukkan : ", iscorrect)