import tkinter as tk
from time import strftime

# Membuat objek utama dari Tkinter
root = tk.Tk()
root.title("Jam Berjalan")

# Fungsi untuk memperbarui waktu
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)  # Memperbarui waktu setiap 1000 milidetik (1 detik)

# Membuat label untuk menampilkan waktu
label = tk.Label(root, font=('calibri', 40, 'bold'), background='purple', foreground='white')
label.pack(anchor='center')

time()  # Memanggil fungsi time() agar jam berjalan

root.mainloop()
