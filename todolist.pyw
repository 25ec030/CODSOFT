import tkinter as tk
from tkinter import simpledialog, messagebox

# -------- Window --------
root = tk.Tk()
root.title("Daily Task Manager")
root.geometry("600x450")
root.config(bg="#d8f3f0")   # light aqua background

tasks = []

# -------- Title --------
title = tk.Label(
    root,
    text="Daily Task List",
    font=("Georgia", 24, "bold"),
    bg="#d8f3f0",
    fg="#2f3e46"
)
title.pack(pady=15)

# -------- Task Frame --------
frame = tk.Frame(root, bg="#bcd4e6", bd=2, relief="ridge")
frame.pack(padx=20, pady=10, fill="both", expand=True)

# Scrollbar
scroll = tk.Scrollbar(frame)
scroll.pack(side="right", fill="y")

# Listbox
task_list = tk.Listbox(
    frame,
    font=("Arial", 12),
    bg="#f1f5f9",
    yscrollcommand=scroll.set,
    selectbackground="#a8dadc",
    bd=0,
    height=12
)

task_list.pack(fill="both", expand=True, padx=10, pady=10)
scroll.config(command=task_list.yview)

# -------- Functions --------
def add_task():
    task = simpledialog.askstring("Add Task", "Enter a new task:")
    if task:
        task_list.insert(tk.END, "☐ " + task)

def toggle_done():
    try:
        index = task_list.curselection()[0]
        task = task_list.get(index)

        if task.startswith("☐"):
            task = task.replace("☐", "✔", 1)
        else:
            task = task.replace("✔", "☐", 1)

        task_list.delete(index)
        task_list.insert(index, task)

    except:
        messagebox.showwarning("Warning", "Select a task first")

def delete_task():
    try:
        index = task_list.curselection()[0]
        task_list.delete(index)
    except:
        messagebox.showwarning("Warning", "Select a task to delete")

# -------- Button Frame --------
button_frame = tk.Frame(root, bg="#d8f3f0")
button_frame.pack(pady=15)

add_btn = tk.Button(
    button_frame,
    text="Add Task",
    width=15,
    bg="#90dbf4",
    font=("Arial", 11),
    command=add_task
)
add_btn.grid(row=0, column=0, padx=10)

toggle_btn = tk.Button(
    button_frame,
    text="Toggle Done",
    width=15,
    bg="#a8dadc",
    font=("Arial", 11),
    command=toggle_done
)
toggle_btn.grid(row=0, column=1, padx=10)

delete_btn = tk.Button(
    button_frame,
    text="Delete",
    width=15,
    bg="#ffb5a7",
    font=("Arial", 11),
    command=delete_task
)
delete_btn.grid(row=0, column=2, padx=10)

# -------- Run --------
root.mainloop()