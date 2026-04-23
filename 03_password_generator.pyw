import tkinter as tk
import random
import string

# -------- Window --------
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.configure(bg="#0f172a")   # dark background

# -------- Title --------
title = tk.Label(
    root,
    text="Password Generator",
    font=("Arial", 18, "bold"),
    bg="#0f172a",
    fg="#14b8a6"   # dark turquoise
)
title.pack(pady=15)

# -------- Length Input --------
length_label = tk.Label(
    root,
    text="Enter Password Length:",
    font=("Arial", 11),
    bg="#0f172a",
    fg="white"
)
length_label.pack()

length_entry = tk.Entry(
    root,
    width=10,
    font=("Arial", 12),
    justify="center",
    bg="#1e293b",
    fg="white",
    insertbackground="white"
)
length_entry.pack(pady=5)

# -------- Result Box --------
result_box = tk.Entry(
    root,
    width=25,
    font=("Arial", 12),
    justify="center",
    bg="#1e293b",
    fg="#14b8a6",
    insertbackground="white"
)
result_box.pack(pady=15)

# -------- Function --------
def generate_password():
    length = int(length_entry.get())

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""
    for i in range(length):
        password += random.choice(characters)

    result_box.delete(0, tk.END)
    result_box.insert(0, password)

# -------- Button --------
generate_btn = tk.Button(
    root,
    text="Generate Password",
    font=("Arial", 11),
    bg="#14b8a6",
    fg="black",
    width=18,
    command=generate_password
)
generate_btn.pack()

# -------- Run --------
root.mainloop()