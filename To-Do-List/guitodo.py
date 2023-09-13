import tkinter as tk
from tkinter import ttk

def add_task():
    task = task_entry.get()
    tasks_listbox.insert(tk.END, task)
    task_entry.delete(0, tk.END)

def remove_task():
    selected_index = tasks_listbox.curselection()
    if selected_index:
        tasks_listbox.delete(selected_index)

# Create the main window
root = tk.Tk()
root.title("To-Do List Application")

# Create widgets
task_label = ttk.Label(root, text="Enter task:")
task_entry = ttk.Entry(root)
add_button = ttk.Button(root, text="Add Task", command=add_task)
remove_button = ttk.Button(root, text="Remove Selected Task", command=remove_task)
tasks_listbox = tk.Listbox(root)

# Arrange widgets using grid layout
task_label.grid(row=0, column=0, padx=10, pady=10)
task_entry.grid(row=0, column=1, padx=10, pady=10)
add_button.grid(row=0, column=2, padx=10, pady=10)
remove_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
tasks_listbox.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
