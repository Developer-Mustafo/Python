# from tkinter import *
#
# oyna = Tk()
# oyna["bg"]="#00BFFF"
#
# username = Label(text="Username",bg="#00BFFF",font="TkFixedFont")
# username.pack(pady=10)
#
# user_entry = Entry()
# user_entry.pack()
#
# password = Label(text="Password",bg="#00BFFF",font="TkFixedFont")
# password.pack(pady=10)
#
# pass_entry = Entry()
# pass_entry.pack()
#
# login = Button(text="Login",bg="gold")
# login.pack(pady=10)
#
# oyna.mainloop()
from tkinter import *
from tkinter import ttk

root = Tk()
root["bg"] = "gold"

Label(text="Telefon raqamni kiriting:", bg="gold").pack()

raqamni_olish = Entry()
raqamni_olish.pack()

malumotlar = []

ustunlar = ("number", "company")
tree = ttk.Treeview(columns=ustunlar, show="headings")
tree.heading("number", text="Tel-raqam")
tree.heading("company", text="Kompaniya")
tree.pack(fill=BOTH, expand=1)


def saqlash():
    t = raqamni_olish.get()
    kod = t[:2]
    ikod = int(kod)
    malumotlar.clear()
    c = ""
    if ikod in [91, 90]:
        c = "Beeline"
    elif ikod == 33:
        c = "Humans"
    elif ikod in [99, 95]:
        c = "Uzmobile"
    elif ikod in [93, 94, 50]:
        c = "Ucell"
    elif ikod == 97:
        c = "MobiUZ"
    else:
        c = "-"
    malumotlar.append((f"+998 ({kod}) {t[2:]}", c))
    for malumot in malumotlar:
        tree.insert("", END, values=malumot)


Button(text="Slash", command=saqlash, bg="gold").pack()

root.mainloop()