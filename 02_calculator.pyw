import tkinter as tk
from tkinter import messagebox

# -------- Window --------
root = tk.Tk()
root.title("Soft Lemon Calculator")
root.geometry("350x400")
root.config(bg="#fff9c4")   # soft lemon powder yellow

# -------- Title --------
title = tk.Label(
    root,
    text="Simple Calculator",
    font=("Georgia", 18, "bold"),
    bg="#fff9c4",
    fg="#5f5f00"
)
title.pack(pady=15)

# -------- Input Fields --------
frame = tk.Frame(root, bg="#fff9c4")
frame.pack(pady=10)

num1_entry = tk.Entry(frame, font=("Arial", 14), width=10, justify="center")
num1_entry.grid(row=0, column=0, padx=5)

operation = tk.StringVar()
operation.set("+")

op_menu = tk.OptionMenu(frame, operation, "+", "-", "*", "/")
op_menu.config(font=("Arial", 12), bg="#fff3a3", width=3)
op_menu.grid(row=0, column=1)

num2_entry = tk.Entry(frame, font=("Arial", 14), width=10, justify="center")
num2_entry.grid(row=0, column=2, padx=5)

# -------- Result Label --------
result_label = tk.Label(
    root,
    text="Result: ",
    font=("Arial", 14),
    bg="#fff9c4",
    fg="#444400"
)
result_label.pack(pady=20)

# -------- Calculation Function --------
def calculate():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        op = operation.get()

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
            result = num1 / num2

        result_label.config(text="Result: " + str(result))

    except:
        messagebox.showwarning("Input Error", "Enter valid numbers")

# -------- Button --------
calc_btn = tk.Button(
    root,
    text="Calculate",
    font=("Arial", 12, "bold"),
    bg="#ffe066",
    width=15,
    command=calculate
)
calc_btn.pack(pady=10)

# -------- Run --------
root.mainloop()