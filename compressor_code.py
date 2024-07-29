import tkinter as tk
import zipfile
from tkinter import filedialog
from tkinter import messagebox


root = tk.Tk()
root.geometry("350x100")
root.title("Folder and File Compressor")


def compress():
   input_file = filedialog.askopenfilename()
   output_file = filedialog.asksaveasfilename(defaultextension=".zip")
   with zipfile.ZipFile(output_file, 'w') as jungle_zip:
       jungle_zip.write(input_file, compress_type=zipfile.ZIP_DEFLATED)
   messagebox.showinfo("(Congrats)", "Compressed file is saved!")




frame1 = tk.Frame(root)
frame1.pack(pady=20)




l1 = tk.Label(frame1, text="SELECT:")
l1.pack(side="left", padx=10)
button1 = tk.Button(frame1, text="Compress your File", width=20, command=compress)
button1.pack(side="right", padx=10)
root.mainloop()
