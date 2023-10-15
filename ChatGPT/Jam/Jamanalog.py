import tkinter as tk
import time
import math

# Membuat objek utama dari Tkinter
root = tk.Tk()
root.title("Jam Analog Berjalan")

# Membuat kanvas untuk jam analog
canvas = tk.Canvas(root, width=400, height=400, bg='white')
canvas.pack()

# Fungsi untuk menggambar jam analog
def draw_clock():
    canvas.delete("all")  # Menghapus gambar sebelumnya

    # Menghitung waktu saat ini
    current_time = time.localtime()
    hours, minutes, seconds = current_time.tm_hour, current_time.tm_min, current_time.tm_sec

    # Menggambar lingkaran jam
    canvas.create_oval(50, 50, 350, 350, width=2)

    # Menggambar jarum-jarum jam
    draw_hand(150, 150, 30, hours * 30 + minutes / 2, 100)
    draw_hand(150, 150, 10, minutes * 6 + seconds / 10, 150)
    draw_hand(150, 150, 3, seconds * 6, 150)

    # Membuat jam berjalan dengan interval 1000ms (1 detik)
    root.after(1000, draw_clock)

# Fungsi untuk menggambar jarum jam
def draw_hand(x, y, width, angle, length):
    angle_rad = math.radians(angle - 90)
    x1 = x + length * math.cos(angle_rad)
    y1 = y + length * math.sin(angle_rad)
    canvas.create_line(x, y, x1, y1, width=width)

draw_clock()  # Memanggil fungsi pertama kali

root.mainloop()
