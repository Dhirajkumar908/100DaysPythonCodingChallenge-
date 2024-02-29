import tkinter as tk

window=tk.Tk()
window.title("Visual Novel")
window.geometry("400x400")

story="You meet a woman on the way to a Replit meetup"

def iCode():
    global story
    canvas.itemconfig(container, image=codes)
    story="She tries to pull out her laptop and drops it on the floor"
    storyLable["text"]=story
    button.pack_forget()
    button2.pack_forget()
    button3.pack()
    button4.pack()

def iReplit():
    global story
    canvas.itemconfig(container, image=replit)
    story="Why i use Replit of course, like every sane individual!"
    storyLable["text"]=story
    button.pack_forget()
    button2.pack_forget()
    button5.pack()
    button6.pack()

def iEdit():
    global story
    canvas.itemconfig(container, image=vs)
    story="She spends two hours loading up a code editor\nand getting it working"
    storyLable["text"]=story
    button3.pack_forget()
    button4.pack_forget()
    button.pack()
    restartButton.pack()

def iUse():
    global story
    canvas.itemconfig(container, image=amazing)
    story="you both celebrate using the best\n coding platform on your way"
    storyLable["text"]=story
    button3.pack_forget()
    button4.pack_forget()
    button6.pack()
    restartButton.pack()

def iToo():
    global story
    canvas.itemconfig(container, image=days)
    story="She tells you all about 100 days of code!"
    storyLable["text"]=story
    button5.pack_forget()
    button6.pack_forget()
    button2.pack
    restartButton.pack()

def iWin():
  global story
  canvas.itemconfig(container, image=amazing)
  story = "You both celebrate using the best\n coding platform on your way to the meetup\nand talk about 100 days of code"
  storyLable["text"] = story
  button5.pack_forget()
  button6.pack_forget()
  button3.pack()
  restartButton.pack()

  
def restart():
  global story
  canvas.itemconfig(container, image=start)
  story = "You meet a woman on the way to a Replit meetup IRL"
  storyLable["text"] = story
  restartButton.pack_forget()
  button.pack()
  button2.pack()


start= tk.PhotoImage(file="img/1.png")
start=start.subsample(4)

codes=tk.PhotoImage(file="img/2.png")
codes=codes.subsample(4)

replit=tk.PhotoImage(file="img/3.png")
replit=codes.subsample(4)

days=tk.PhotoImage(file="img/4.png")
days=codes.subsample(4)

amazing=tk.PhotoImage(file="img/5.png")
amazing=codes.subsample(4)

vs=tk.PhotoImage(file="img/6.png")
vs=codes.subsample(4)


canvas=tk.Canvas(window, width=300, height=200)
canvas.pack()

container=canvas.create_image(150, 150, image=start)

storyLable=tk.Label(text=story)
storyLable.pack()

button=tk.Button(text="Ask her how she code?", command=iCode)
button.pack()

button2=tk.Button(text="Tell her about Replit", command=iReplit)
button2.pack()

button3=tk.Button(text="She says' I use a local editor", command=iEdit)
button4=tk.Button(text="She says' I use Replit0", command=iUse)
button5=tk.Button(text="You says' I use Replit too", command=iToo)
button6=tk.Button(text="You say' Im actually going through 100day code", command=iWin)
restartButton=tk.Button(text="Restart", command=restart)

tk.mainloop()