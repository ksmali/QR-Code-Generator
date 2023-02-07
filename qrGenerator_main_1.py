# -*- coding: utf-8 -*-


import tkinter as tk
import qrcode
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk

def generate_qr():
    data = entry.get()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    size = size_var.get()
    img = img.resize((size, size), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    label.config(image=img)
    label.image = img
    save_button.config(state=tk.NORMAL)

def save_qr():
    filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png")])
    if filename:
        label.image.save(filename)
        messagebox.showinfo("Info", "QR Code saved successfully!")

root = tk.Tk()
root.geometry("300x550")
root.title("QR Code Generator")

label = tk.Label(root)
label.pack(pady=20)

data_label = tk.Label(root, text = "Data")
data_label.pack(pady = 10)
entry = tk.Entry(root)
entry.pack(pady=20)

size_var = tk.IntVar(value=200)
size_label = tk.Label(root, text = "Size")
size_label.pack(pady=10)
size_entry = tk.Spinbox(root, from_=100, to=1000, increment=100, textvariable=size_var)
size_entry.pack(pady=20)

generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=20)

save_button = tk.Button(root, text="Save QR Code", state=tk.DISABLED, command=save_qr)
save_button.pack()

root.mainloop()
