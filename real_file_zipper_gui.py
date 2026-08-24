import tkinter as tk
from tkinter import filedialog, messagebox
import zipfile       
import os # Day 1 more activation          
 
#Compression Code  
def compress():
    file_path = filedialog.askopenfilename()  
 
    if not file_path:
        return

    save_path = filedialog.asksaveasfilename(
        defaultextension=".zip",
        filetypes=[("Zip files", "*.zip")]
    )

    if not save_path:
        return

    if not save_path.endswith(".zip"):
        save_path += ".zip"

    try:
        with zipfile.ZipFile(save_path, "w", zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(file_path, os.path.basename(file_path))

        original = os.path.getsize(file_path)/1024
        compressed = os.path.getsize(save_path)/1024

        result.set(
            f"Compressed Successfully\n"
            f"Original: {original:.2f} KB\n"
            f"Compressed: {compressed:.2f} KB"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Decompress
def decompress():
    zip_path = filedialog.askopenfilename(
        filetypes=[("Zip files", "*.zip")]
    )

    if not zip_path:
        return

    extract_folder = filedialog.askdirectory()

    if not extract_folder:
        return

    with zipfile.ZipFile(zip_path, 'r') as zipf:
        zipf.extractall(extract_folder)

    result.set("✅ File Extracted Successfully")


#  For GUI Interface
root = tk.Tk()
root.title("Real File Zipper")
root.geometry("420x300")
root.config(bg="#f4f6f7")

title = tk.Label(
    root,
    text="Real File Zipper",
    font=("Segoe UI", 16, "bold"),
    bg="#f4f6f7"
)
title.pack(pady=15)

compress_btn = tk.Button(
    root,
    text="📂 Select File & Compress",
    command=compress,
    width=25,
    bg="#27ae60",
    fg="white",
    font=("Segoe UI", 11)
)
compress_btn.pack(pady=10)

decompress_btn = tk.Button(
    root,
    text="📦 Extract ZIP File",
    command=decompress,
    width=25,
    bg="#2980b9",
    fg="white",
    font=("Segoe UI", 11)
)
decompress_btn.pack(pady=10)

result = tk.StringVar()
result_label = tk.Label(
    root,
    textvariable=result,
    bg="#f4f6f7",
    font=("Segoe UI", 10)
)
result_label.pack(pady=20)

root.mainloop()
