import tkinter
from tkinter import *

root = Tk()
root.title("My First Calculator")
root.geometry("570x700+400+400")
root.configure(bg="#FFFDD0")

equation = ""

def show(value):
    global equation
    equation += value
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate():
    global equation
    try:
        result = eval(equation)
        equation = str(result)
        label_result.config(text=equation)
    except SyntaxError:
        equation = "Syntax Error"
        label_result.config(text=equation)
    except:
        equation = "Error"
        label_result.config(text=equation)

label_result = Label(root, width=25, height=2, text="", font=('Arial', 30,), bg="#F5F5DC")
label_result.pack()

Button(root, text="C", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#e61736", command=lambda: clear()).place(x=10, y=100)
Button(root, text="/", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("/")).place(x=150, y=100)
Button(root, text="%", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("%")).place(x=290, y=100)
Button(root, text="*", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("*")).place(x=430, y=100)
Button(root, text="7", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("7")).place(x=10, y=200)
Button(root, text="8", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("8")).place(x=150, y=200)
Button(root, text="9", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("9")).place(x=290, y=200)
Button(root, text="+", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#7FFF00", bg="#17183d", command=lambda: show("+")).place(x=430, y=200)
Button(root, text="4", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("4")).place(x=10, y=300)
Button(root, text="5", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("5")).place(x=150, y=300)
Button(root, text="6", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("6")).place(x=290, y=300)
Button(root, text="1", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("1")).place(x=10, y=400)
Button(root, text="2", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("2")).place(x=150, y=400)
Button(root, text="3", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("3")).place(x=290, y=400)
Button(root, text="=", width=5, height=3, font=("arial", 30, "bold"), bd=1, fg="#e61736", bg="#17183d", command=calculate).place(x=430, y=410)
Button(root, text="00", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("00")).place(x=10, y=500)
Button(root, text="0", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("0")).place(x=150, y=500)
Button(root, text=".", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show(".")).place(x=290, y=500)
Button(root, text="-", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("-")).place(x=430, y=300)

root.mainloop()
