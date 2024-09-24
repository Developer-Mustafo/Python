import tkinter

t = tkinter.Tk()
t.geometry("300x300")
label = tkinter.Label(background="black", foreground="white", text="Hello world!")
txt = tkinter.Text(t)


def editText():
    label["text"] = txt.get("1.0","end-1c")
    label["foreground"] = "red"


btn = tkinter.Button(text="Click me!", background="#122124", command=editText)
label.pack(anchor="center")
txt.pack(anchor="center")
btn.pack(anchor="center")
t.mainloop()
