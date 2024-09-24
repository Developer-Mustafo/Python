import datetime

e = []
for vaqt in "yil", "oy", "kun":
    d = int(input("Tugilgan " + vaqt + ": "))
    e.append(d)

tugilgan_vaqt = datetime.date(e[0], e[1], e[2])
hozirgi_vaqt = datetime.date.today()

kunlar = (hozirgi_vaqt - tugilgan_vaqt).days

print("Siz yashagan kunlar:", kunlar)
