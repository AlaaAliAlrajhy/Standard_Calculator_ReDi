import math
import tkinter as tk
from tkinter import *

root = Tk()
root.title("My First Calculator")
root.geometry("570x600")
root.configure(bg="#FFFDD0")

Default_values = {"x": 0, "y": 0}

mathOperation = ""

def show(value):
    global mathOperation

# Check if the value is a decimal point and there is already a decimal point in the mathOperation:
    if value == "." and "." in mathOperation:
        return
# Check if the value is the symbol for π (pi) and if the last character in mathOperation is a digit:

    if value == "π" and mathOperation[-1].isdigit():
        return

# Append the current value to the mathOperation string:

    mathOperation += value
    label_result.config(text=mathOperation)

# define the functions:
def clear():
    global mathOperation
    mathOperation = ""
    label_result.config(text=mathOperation)

def backspace():
    global mathOperation
    mathOperation = mathOperation[:-1]
    label_result.config(text=mathOperation)

# Perform the calculation based on the mathOperation string
def calculate():
    global mathOperation

    try:
        for var in Default_values:
            mathOperation = mathOperation.replace(var, str(Default_values[var]))

        result = eval(mathOperation)
        mathOperation = str(result)
        label_result.config(text=result)
    except Exception as e:
        label_result.config(text="Error")
    
# define the key press functions:
def key_pressed(event):
    key = event.char
    if key.isdigit() or key == ".":
        show(key)
    elif key == "+":
        show("+")
    elif key == "-":
        show("-")
    elif key == "*":
        show("*")
    elif key == "/":
        show("/")
    elif key == "\r":
        calculate()
    elif key == "\x08":
        backspace()
    elif key == "\x1b":
        clear()

label_result = Label(root, width=25, height=2, text="", font=('Arial', 30), bg="#F5F5DC")
label_result.pack()

Button(root, text="C", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#e61736", command=clear, takefocus=False).place(x=10, y=100)
Button(root, text="/", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("/"), takefocus=False).place(x=150, y=100)
Button(root, text="*", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("*"), takefocus=False).place(x=430, y=300)
Button(root, text="-", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("-"), takefocus=False).place(x=430, y=200)
Button(root, text="7", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("7"), takefocus=False).place(x=10, y=200)
Button(root, text="8", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("8"), takefocus=False).place(x=150, y=200)
Button(root, text="9", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("9"), takefocus=False).place(x=290, y=200)
Button(root, text="+", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#7FFF00", bg="#17183d", command=lambda: show("+"), takefocus=False).place(x=430, y=400)
Button(root, text="4", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("4"), takefocus=False).place(x=10, y=300)
Button(root, text="5", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("5"), takefocus=False).place(x=150, y=300)
Button(root, text="6", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("6"), takefocus=False).place(x=290, y=300)
Button(root, text="1", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("1"), takefocus=False).place(x=10, y=400)
Button(root, text="2", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("2"), takefocus=False).place(x=150, y=400)
Button(root, text="3", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("3"), takefocus=False).place(x=290, y=400)
Button(root, text="=", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#e61736", bg="#17183d", command=calculate, takefocus=False).place(x=430, y=500)
Button(root, text="0", width=10, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("0"), takefocus=False).place(x=10, y=500)
Button(root, text=".", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("."), takefocus=False).place(x=290, y=500)
Button(root, text="π", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=lambda: show("3.141592653589793"), takefocus=False).place(x=290, y=100)
Button(root, text="⌫", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#17183d", command=backspace, takefocus=False).place(x=430, y=100)

root.bind("<Key>", key_pressed)

root.mainloop()

