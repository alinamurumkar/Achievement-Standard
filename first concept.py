import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import random


class PartyHireStore:
    def __init__(self, root):
        self.root = root
        self.root.title("Party Hire Store")
        self.root.configure(bg='#FFC0CB')  # Light pink background

        # Store data
        self.hire_data = []

        # Define widgets
        self.create_widgets()

    def create_widgets(self):
        # Font and style settings
        custom_font = ("Merriweather", 10)
        text_color = "#4B0082"  # Dark purple

        # Labels and entries
        tk.Label(self.root, text="Customer Full Name:", bg='#FFC0CB', font=custom_font, fg=text_color).grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.customer_name_entry = tk.Entry(self.root, font=custom_font, fg=text_color)
        self.customer_name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Receipt Number:", bg='#FFC0CB', font=custom_font, fg=text_color).grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.receipt_number_entry = tk.Entry(self.root, state='readonly', font=custom_font, fg=text_color)
        self.receipt_number_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Item Hired:", bg='#FFC0CB', font=custom_font, fg=text_color).grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.item_combobox = ttk.Combobox(self.root, values=["Table", "Chair", "Tent", "Sound System", "Lights"], font=custom_font, foreground=text_color)
        self.item_combobox.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Quantity:", bg='#FFC0CB', font=custom_font, fg=text_color).grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        self.quantity_entry = tk.Entry(self.root, font=custom_font, fg=text_color)
        self.quantity_entry.grid(row=3, column=1, padx=10, pady=5)

        # Buttons
        self.add_button = tk.Button(self.root, text="Hire Item", command=self.add_hire_item, font=custom_font, bg='#FF69B4', fg=text_color)
        self.add_button.grid(row=4, column=0, padx=10, pady=10)

        self.return_button = tk.Button(self.root, text="Return Item", command=self.return_hire_item, font=custom_font, bg='#FF69B4', fg=text_color)
        self.return_button.grid(row=4, column=1, padx=10, pady=10)

        # Listbox to display hire items
        self.hire_listbox = tk.Listbox(self.root, width=60, font=custom_font, bg='#FFF0F5', fg=text_color)
        self.hire_listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def add_hire_item(self):
        # Get the input values
        customer_name = self.customer_name_entry.get()
        item_hired = self.item_combobox.get()
        quantity = self.quantity_entry.get()

        # Validate inputs
        if not customer_name:
            messagebox.showerror("Error", "Customer name is required.")
            return
        if not item_hired:
            messagebox.showerror("Error", "Item hired is required.")
            return
        if not quantity.isdigit() or not (1 <= int(quantity) <= 500):
            messagebox.showerror("Error", "Quantity must be a number between 1 and 500.")
            return

        # Generate receipt number
        receipt_number = random.randint(1000, 9999)
        self.receipt_number_entry.config(state='normal')
        self.receipt_number_entry.delete(0, tk.END)
        self.receipt_number_entry.insert(0, receipt_number)
        self.receipt_number_entry.config(state='readonly')

        # Add hire details to the list
        hire_details = f"{customer_name} - Receipt: {receipt_number} - Item: {item_hired} - Quantity: {quantity}"
        self.hire_listbox.insert(tk.END, hire_details)
        self.hire_data.append((receipt_number, hire_details))

        # Clear inputs
        self.customer_name_entry.delete(0, tk.END)
        self.item_combobox.set("")
        self.quantity_entry.delete(0, tk.END)

    def return_hire_item(self):
        receipt_number = simpledialog.askinteger("Return Item", "Enter receipt number:")
        if receipt_number is None:
            return

        # Find and remove the hire item
        for i, (rn, details) in enumerate(self.hire_data):
            if rn == receipt_number:
                self.hire_listbox.delete(i)
                self.hire_data.pop(i)
                messagebox.showinfo("Returned", f"Item with receipt number {receipt_number} has been returned.")
                return

        messagebox.showerror("Error", f"No item found with receipt number {receipt_number}.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PartyHireStore(root)
    root.mainloop()
tk.toplevel()
