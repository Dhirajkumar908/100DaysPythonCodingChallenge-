import tkinter as tk
from PIL import Image, ImageTk

window=tk.Tk()
window.title("Guess Who?")
window.geometry("400x400")

label="Guess Who?"

def showImage():
    person=text.get("1.0", "end")
    if person.lower().strip()=="mo":
        canvas.itemconfig(container, image=mo)
    elif person.lower().strip()=="charlotte":
        canvas.itemconfig(container, image=charlotte)
    elif person.lower().strip()=="gerald":
        canvas.itemconfig(container, image=gerald)
    elif person.lower().strip()=="katie":
        canvas.itemconfig(container, image=Katie)
    else:
        header['text']="Unable to find this user"

header=tk.Label(text=label)
header.pack()
text=tk.Text(window, height=1, width=30)
text.pack()

button=tk.Button(text="find", command=showImage)
button.pack()

canvas=tk.Canvas(window, width=400, height=380)
canvas.pack()
charlotte=ImageTk.PhotoImage(Image.open("guessWho/omimg.png"))
gerald=ImageTk.PhotoImage(Image.open("guessWho/mo.jpg"))
Katie=ImageTk.PhotoImage(Image.open("guessWho/download.jpg"))
mo=ImageTk.PhotoImage(Image.open("guessWho/mo.jpg"))
container=canvas.create_image(150,1,image=mo)


tk.mainloop()

