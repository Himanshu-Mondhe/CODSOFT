import tkinter as tk
from tkinter import ttk

def calculate():
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    operation = operation_combobox.get()

    if operation == "+":
        result.set(num1 + num2)
    elif operation == "-":
        result.set(num1 - num2)
    elif operation == "*":
        result.set(num1 * num2)
    elif operation == "/":
        if num2 != 0:
            result.set(num1 / num2)
        else:
            result.set("Cannot divide by zero")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create widgets
num1_label = ttk.Label(root, text="Enter first number:")
num1_entry = ttk.Entry(root)
num2_label = ttk.Label(root, text="Enter second number:")
num2_entry = ttk.Entry(root)
operation_label = ttk.Label(root, text="Select operation:")
operation_combobox = ttk.Combobox(root, values=["+", "-", "*", "/"])
calculate_button = ttk.Button(root, text="Calculate", command=calculate)
result = tk.StringVar()
result_label = ttk.Label(root, textvariable=result)

# Arrange widgets using grid layout
num1_label.grid(row=0, column=0, padx=10, pady=10)
num1_entry.grid(row=0, column=1, padx=10, pady=10)
num2_label.grid(row=1, column=0, padx=10, pady=10)
num2_entry.grid(row=1, column=1, padx=10, pady=10)
operation_label.grid(row=2, column=0, padx=10, pady=10)
operation_combobox.grid(row=2, column=1, padx=10, pady=10)
calculate_button.grid(row=3, columnspan=2, padx=10, pady=10)
result_label.grid(row=4, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
