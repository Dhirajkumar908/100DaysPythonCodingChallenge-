from tkinter import *

import speedtest

# Initializing GUI Window:
root=Tk()
root.geometry("300x400")
root.resizable(True,True)
root.title("Speed Test")
root.configure(bg='#E6E6FA')

# Creating Labels and Button:
Label(root,text="Internet Speed Test",font=("Arial,bold",22),bg='#8B8386',fg='White',width=30).pack(pady=10)
l1=Label(root,text="Download Speed :",font=("Arial,bold",15),bg='#E6E6FA')
l1.place(x=10,y=80)
ldspd=Label(root,text="",font=("Arial,bold",15),bg='#E6E6FA',fg='#089927')
ldspd.place(x=180,y=80)
l2=Label(root,text="Upload Speed :",font=("Arial,bold",15),bg='#E6E6FA')
l2.place(x=10,y=130)
luspd=Label(root,text="",font=("Arial,bold",15),bg='#E6E6FA',fg='#089927')
luspd.place(x=180,y=130)

btn=Button(root,text="Check",font=('Arial,bold',15),bd=5,bg='#8B8386',fg='White',activebackground='#8B8386',activeforeground='White')
btn.place(x=125,y=190)


root.mainloop()



def check():
    spd=speedtest.Speedtest()
    spd.get_servers()
    dspd=str(round(spd.download() / (10**6),3)) + " Mbps"
    uspd=str(round(spd.upload() / (10**6),3)) + " Mbps"
    ldspd.config(text=dspd)
    luspd.config(text=uspd)