import tkinter

tk = tkinter.Tk()
lbl = tkinter.Label(text="Hello world!")
text = tkinter.Text(tk)


def edit():
    lbl["text"] = text.get("1.0","end-1c")


btn = tkinter.Button(text="Show", foreground="black", command=edit)
lbl.pack(anchor="center")
text.pack(anchor="center")
btn.pack(anchor="center")
tk.mainloop()
