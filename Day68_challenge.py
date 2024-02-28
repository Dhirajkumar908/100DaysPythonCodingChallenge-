import tkinter as tk
from PIL import Image, ImageTk

window=tk.Tk()
window.title("Guess Who?")
window.geometry("400x400")

label="Guess Who?"

def showImage():
    person=text.get("1.0", "end")
    if person.lower().strip()=="a":
        canvas.itemconfig(container, image=mo)
    elif person.lower().strip()=="b":
        canvas.itemconfig(container, image=charlotte)
    elif person.lower().strip()=="c":
        canvas.itemconfig(container, image=gerald)
    elif person.lower().strip()=="d":
        canvas.itemconfig(container, image=Katie)
    else:
        canvas.pack_forget()
        warning.pack()
        return
    canvas.pack_forget()
    warning.pack()

header=tk.Label(text=label)
header.pack()
text=tk.Text(window, height=1, width=30)
text.pack()

button=tk.Button(text="find", command=showImage)
button.pack()

canvas=tk.Canvas(window, width=400, height=380)
canvas.pack()
charlotte=ImageTk.PhotoImage(Image.open("img/omimg.png"))
gerald=ImageTk.PhotoImage(Image.open("img/11.jpg"))
Katie=ImageTk.PhotoImage(Image.open("img/download.jpg"))
mo=ImageTk.PhotoImage(Image.open("img/mo.jpg"))
container=canvas.create_image(150,1,image=mo)

warning=tk.Label(text="Unable to find this user")

tk.mainloop()

