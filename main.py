""" Saya Villeneuve Andhira Suwandhi NIM 2108067 mengerjakan Latihan 9
dalam mata kuliah Desain Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan.
Aamiin. """

""" import """
from apartemen import Apartemen
from indekos import Indekos
from rumah import Rumah
from tkinter import *
from PIL import ImageTk, Image

""" program """
# new
hunians = []
hunians.append(Apartemen("Nelly Joy", 5, 4, "20", "100 x 100", "apartment.jpg"))
hunians.append(Rumah("Sekar MK", 2, 2, "100 x 100", "rumah1.jpg"))
hunians.append(Indekos("Bp. Romi", "Cahya", "6", "5 x 5", "kost.jpg"))
hunians.append(Rumah("Satria", 3, 3, "100 x 100", "rumah2.jpg"))

root = Tk()
root.title("Praktikum DPBO Python")

img_img = []

# detail
def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    d_summary = Label(d_frame, text="Summary: " + "\n" + hunians[index].get_summary() + hunians[index].get_detail(), anchor="w",).grid(row=0, column=0, sticky="w")

    img = Image.open("assets/" + hunians[index].get_foto())
    img = img.resize((250, 250))
    photo_image = ImageTk.PhotoImage(img)
    img_img.append(photo_image)
    img_label = Label(d_frame, image=photo_image)
    img_label.grid(row=1, column=0)

    # d_summary = Label(d_frame, text="Summary\n" + hunians[index].get_detail() + hunians[index].get_summary() + "\n" + hunians[index].get_dokumen(), anchor="w", justify=LEFT).grid(row=0, column=0, sticky="w")

    # btn = LabelFrame(top, padx=0, pady=0)
    # btn.pack(padx=10, pady=10)
    # b_close = Button(btn, text="Close", command=top.destroy)
    # b_close.grid(row=0, column=0)

# halaman utama
def landing_page():
    label.destroy()
    frameland.destroy()
    img_label.destroy()
    button.destroy()

    frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    opts = LabelFrame(root, padx=10, pady=10)
    opts.pack(padx=10, pady=10)

    b_add = Button(opts, text="Add Data", state="disabled")
    b_add.grid(row=0, column=0)

    b_exit = Button(opts, text="Exit", command=root.quit)
    b_exit.grid(row=0, column=1)

    for index, h in enumerate(hunians):
        idx = Label(frame, text=str(index + 1), width=5, borderwidth=1, relief="solid")
        idx.grid(row=index, column=0)
        type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
        type.grid(row=index, column=1)
        if h.get_jenis() != "Indekos":
            name = Label(
                frame,
                text=" " + h.get_nama_pemilik(),
                width=40,
                borderwidth=1,
                relief="solid",
                anchor="w",
            )
            name.grid(row=index, column=2)
        else:
            name = Label(
                frame,
                text=" " + h.get_nama_penghuni(),
                width=40,
                borderwidth=1,
                relief="solid",
                anchor="w",
            )
            name.grid(row=index, column=2)
        b_detail = Button(
            frame, text="Details ", command=lambda index=index: details(index)
        )
        b_detail.grid(row=index, column=3)


label = Label(root, text="=== Landing Page ===", font=("Times New Roman", 18))
label.pack()

img = Image.open("assets/landing.jpg")
img = img.resize((250, 250))
photo_image = ImageTk.PhotoImage(img)
img_img.append(photo_image)

frameland = Frame(root, padx=20, pady=20)
frameland.pack(padx=20, pady=20)

img_label = Label(frameland, image=photo_image)
img_label.pack()

button = Button(root, text="Enter", font=("Times New Roman", 18), command=landing_page)
button.pack(side=BOTTOM)
root.mainloop()