import random
import string
import tkinter as tk
from tkinter import ttk

def generate_password(length, complexity):
    if complexity == "low":
        characters = string.ascii_letters
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits
    elif complexity == "high":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return "Invalid complexity level."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_button_clicked():
    length = int(length_entry.get())
    complexity = complexity_combobox.get().lower()

    password = generate_password(length, complexity)
    generated_password_label.config(text="Generated Password: " + password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create widgets
length_label = ttk.Label(root, text="Enter desired password length:")
length_entry = ttk.Entry(root)
complexity_label = ttk.Label(root, text="Select complexity level:")
complexity_combobox = ttk.Combobox(root, values=["Low", "Medium", "High"])
generate_button = ttk.Button(root, text="Generate Password", command=generate_button_clicked)
generated_password_label = ttk.Label(root, text="Generated Password: ")

# Arrange widgets using grid layout
length_label.grid(row=0, column=0, padx=10, pady=10)
length_entry.grid(row=0, column=1, padx=10, pady=10)
complexity_label.grid(row=1, column=0, padx=10, pady=10)
complexity_combobox.grid(row=1, column=1, padx=10, pady=10)
generate_button.grid(row=2, columnspan=2, padx=10, pady=10)
generated_password_label.grid(row=3, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
