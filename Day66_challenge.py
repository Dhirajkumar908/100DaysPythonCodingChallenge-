import tkinter as tk
window = tk.Tk()
window.title("Calculater") 
window.geometry("260x300") 

answer=0
lastNum=0
operator=None

def typeAnswer(value):
    global answer
    answer = f"{answer}{value}"
    answer=int(answer)
    lbl1["text"]=answer

def calAns(Op):
    global answer, lastNum, operator
    lastNum= answer
    answer=0
    if Op=="+":
        operator="+"
    elif Op=="-":
        operator="-"
    elif Op=="*":
        operator="*"
    elif Op=="/":
        operator="/"
    lbl1["text"]=answer

def calc():
    global answer, lastNum, operator
    print(f"{lastNum}\t{answer}\t{operator}")
    if operator=="+":
        total=lastNum + answer
    elif operator =="-":
        total=lastNum - answer
    elif operator == "*":
        total=lastNum * answer
    elif operator=="/":
        total = lastNum / answer
    answer=total
    lbl1["text"]=answer

lbl1=tk.Label(text=answer)
lbl1.grid(row=0, columnspan=5, padx=10, pady=10)

###################
one=tk.Button(text="1", width=5,   command=lambda:typeAnswer(1))
one.grid(row=2, column=0, padx=3, pady=3)

two=tk.Button(text="2", width=5,  command=lambda:typeAnswer(2))
two.grid(row=2, column=1, padx=3, pady=3)

three=tk.Button(text="3", width=5,   command=lambda:typeAnswer(3))
three.grid(row=2, column=2, padx=3, pady=3)

palase=tk.Button(text="+", width=5,  command=lambda:calAns("+") )
palase.grid(row=2, column=3, padx=3, pady=3)

minus=tk.Button(text="-",  width=5,  command=lambda:calAns("-") )
minus.grid(row=2, column=4, padx=3, pady=3)

###########################################

four=tk.Button(text="4", width=5,   command=lambda:typeAnswer(4) )
four.grid(row=3, column=0, padx=3, pady=3)

five=tk.Button(text="5", width=5,  command=lambda:typeAnswer(5))
five.grid(row=3, column=1, padx=3, pady=3)

six=tk.Button(text="6", width=5,   command=lambda:typeAnswer(6))
six.grid(row=3, column=2, padx=3, pady=3)

mul=tk.Button(text="*", width=5,  command=lambda:calAns("*") )
mul.grid(row=3, column=3, padx=3, pady=3)

Divide=tk.Button(text="/",  width=5,  command=lambda:calAns("/") )
Divide.grid(row=3, column=4, padx=3, pady=3)
###########################################

seven=tk.Button(text="7", width=5,  command=lambda:typeAnswer(7) )
seven.grid(row=4, column=0, padx=3, pady=3)

eight=tk.Button(text="8", width=5,  command=lambda:typeAnswer(8))
eight.grid(row=4, column=1, padx=3, pady=3)

nine=tk.Button(text="9", width=5, command=lambda:typeAnswer(9))
nine.grid(row=4, column=2, padx=3, pady=3)

zero=tk.Button(text="0", width=5,  command=lambda:typeAnswer(0) )
zero.grid(row=4, column=3, padx=3, pady=3)

equal=tk.Button(text="=",  width=5,  command=calc )
equal.grid(row=4, column=4, padx=3, pady=3)
###########################################


tk.mainloop()



# import tkinter as tk

# window=tk.Tk()

# window.geometry('450x300')
# window.title('Test App')

# lbl_txt=0

# def update():
#     global lbl_txt 
#     num= int(txt.get("1.0", "end"))
#     lbl_txt +=num
#     lbl1["text"]=lbl_txt

# lbl1=tk.Label(text=lbl_txt).grid(row=0, column=0)

# txt=tk.Text(window, height=1, width=50).grid(row=1, columnspan=3)

# btn1=tk.Button(window, text="Click me!", border=0.5, command=update).grid(row=2, column=0)

# btn2=tk.Button(window, text="Click me2", border=0.5, command=update).grid(row=2, column=1)

# btn3=tk.Button(window, text="Click me3", border=0.5, command=update).grid(row=2, column=2)


# tk.mainloop()

