from tkinter import *

t = Tk()
t.title("Test Tkinter")
t["bg"] = "black"
txt = Text(t, background="white", foreground="black")
lbl = Label(text="Bu yerga nima yozsangiz chiqadi")


def clicked():
    try:
        lbl["text"] = txt.get("1.0", "end-1c")
        txt.insert(END, "Salom")
        txt['bg'] = "#245454"
    except:
        lbl['text'] = "dssdds"


btn = Button(text="Click me", background="gold", command=clicked)
txt.pack(anchor="center")
lbl.pack(pady=100)
btn.pack(anchor="center")
t.mainloop()
