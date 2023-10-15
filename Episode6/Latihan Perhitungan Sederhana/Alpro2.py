print("## Program Python diskon potongan harga ##")
print("======================")
print()

total_belanja = int(input("Total belanja : Rp."))

if (total_belanja >= 100000) and (total_belanja < 500000):
    harga_akhir = total_belanja - (0.1*total_belanja)
    print("Selamat anda mendapatkan diskon 10%")
elif (total_belanja >= 500000) and (total_belanja < 1000000):
    harga_akhir = total_belanja - (0.2*total_belanja)
    print("Selamat anda mendapatkan diskon 20%")
elif (total_belanja >= 100000):
    harga_akhir = total_belanja - (0.3*total_belanja)
    print("Selamat anda mendapatkan diskon 30%")
else :
    harga_akhir = total_belanja
    print("Total bayar : Rp", float(harga_akhir,2))