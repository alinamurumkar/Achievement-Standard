import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import random
import json


class ThePartyHireStore:
    def __init__(self, root, menu_window):
        self.root = root
        self.menu_window = menu_window
        self.root.title("Party Hire Store")
        self.root.configure(bg='#FFC0CB')  # Light pink background

        # Store the data of the inputs
        self.hire_data = []

        # Define widgets
        self.create_widgets()

        # Load existing data from file
        self.load_data()

    def create_widgets(self):
        custom_font = ("Anonymous Pro", 10)
        text_color = "#4B0082"  # Dark purple color for text

        # Set the image file name
        image_file = "hire.png"  # Replace with the name of your image file

        # Load image
        self.image = tk.PhotoImage(file=image_file)

        # Logo
        logo_label = tk.Label(self.root, image=self.image)
        logo_label.image = self.image  # Keep a reference to avoid garbage collection
        logo_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Validation command to ensure only letters and spaces are allowed
        vcmd = (self.root.register(self.validate_name), '%P')

        # Labels and entries
        tk.Label(self.root, text="Customer Full Name:", bg='#FFC0CB', font=custom_font, fg=text_color).grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.customer_name_entry = tk.Entry(self.root, font=custom_font, fg=text_color, validate="key", validatecommand=vcmd)
        self.customer_name_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Receipt Number:", bg='#FFC0CB', font=custom_font, fg=text_color).grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.receipt_number_entry = tk.Entry(self.root, state='readonly', font=custom_font, fg=text_color)
        self.receipt_number_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Item Hired:", bg='#FFC0CB', font=custom_font, fg=text_color).grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        self.item_combobox = ttk.Combobox(self.root, values=["Table", "Chair", "Tent", "Sound System", "Lights"], font=custom_font, foreground=text_color)
        self.item_combobox.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Quantity:", bg='#FFC0CB', font=custom_font, fg=text_color).grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
        self.quantity_entry = tk.Entry(self.root, font=custom_font, fg=text_color)
        self.quantity_entry.grid(row=4, column=1, padx=10, pady=5)

        # Buttons with consistent width
        button_width = 15  # Define a consistent width for buttons

        self.add_button = tk.Button(self.root, text="Hire Item", command=self.add_hire_item, font=custom_font, bg='#FF69B4', fg=text_color, width=button_width)
        self.add_button.grid(row=5, column=0, padx=10, pady=10)

        self.return_button = tk.Button(self.root, text="Return Item", command=self.return_hire_item, font=custom_font, bg='#FF69B4', fg=text_color, width=button_width)
        self.return_button.grid(row=5, column=1, padx=10, pady=10)

        self.history_button = tk.Button(self.root, text="History", command=self.show_history, font=custom_font, bg='#FF69B4', fg=text_color, width=button_width)
        self.history_button.grid(row=6, column=0, padx=10, pady=10)

        self.quit_button = tk.Button(self.root, text="Quit", command=self.quit_application, font=custom_font, bg='#FF69B4', fg=text_color, width=button_width)
        self.quit_button.grid(row=6, column=1, padx=10, pady=10)

        self.back_button = tk.Button(self.root, text="Back to Menu", command=self.back_to_menu, font=custom_font, bg='#FF69B4', fg=text_color, width=button_width)
        self.back_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        # Listbox to display hire items
        self.hire_listbox = tk.Listbox(self.root, width=60, font=custom_font, bg='#FFF0F5', fg=text_color)
        self.hire_listbox.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

    def validate_name(self, new_value):
        if all(char.isalpha() or char.isspace() for char in new_value):
            return True
        else:
            return False

    def quit_application(self):
        self.root.destroy()

    def back_to_menu(self):
        self.root.withdraw()
        self.menu_window.deiconify()

    def add_hire_item(self):
        customer_name = self.customer_name_entry.get()
        item_hired = self.item_combobox.get()
        quantity = self.quantity_entry.get()

        if not customer_name:
            messagebox.showerror("Error", "Please enter customer name.")
            return
        if not item_hired:
            messagebox.showerror("Error", "Please select an item to hire.")
            return
        if not quantity.isdigit() or not (1 <= int(quantity) <= 500):
            messagebox.showerror("Error", "Quantity must be between 1 and 500.")
            return

        receipt_number = random.randint(1000, 9999)
        self.receipt_number_entry.config(state='normal')
        self.receipt_number_entry.delete(0, tk.END)
        self.receipt_number_entry.insert(0, receipt_number)
        self.receipt_number_entry.config(state='readonly')

        hire_details = f"{customer_name} - Receipt: {receipt_number} - Item: {item_hired} - Quantity: {quantity}"
        self.hire_listbox.insert(tk.END, hire_details)
        self.hire_data.append((receipt_number, hire_details))
        self.save_data()

        self.customer_name_entry.delete(0, tk.END)
        self.item_combobox.set("")
        self.quantity_entry.delete(0, tk.END)

    def return_hire_item(self):
        receipt_number = simpledialog.askinteger("Return Item", "Enter receipt number:")
        if receipt_number is None:
            return

        for i, (rn, details) in enumerate(self.hire_data):
            if rn == receipt_number:
                self.hire_listbox.delete(i)
                self.hire_data.pop(i)
                messagebox.showinfo("Returned", f"Item with receipt number {receipt_number} has been returned.")
                self.save_data()
                return

        messagebox.showerror("Error", f"No item found with receipt number {receipt_number}.")

    def save_data(self):
        with open("hire_data.json", "w") as file:
            json.dump(self.hire_data, file)

    def load_data(self):
        try:
            with open("hire_data.json", "r") as file:
                self.hire_data = json.load(file)
                for _, details in self.hire_data:
                    self.hire_listbox.insert(tk.END, details)
        except FileNotFoundError:
            pass

    def show_history(self):
        history_window = tk.Toplevel(self.root)
        history_window.title("Hire History")
        history_window.configure(bg='#FFC0CB')

        custom_font = ("Anonymous Pro", 10)
        text_color = "#4B0082"

        history_listbox = tk.Listbox(history_window, width=60, font=custom_font, bg='#FFF0F5', fg=text_color)
        history_listbox.pack(padx=10, pady=10)

        for _, details in self.hire_data:
            history_listbox.insert(tk.END, details)


class TheOpeningMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome")
        self.root.geometry("300x150")
        self.root.configure(bg='#FFC0CB')

        custom_font = ("Merriweather", 12)
        text_color = "#4B0082"

        # Set the image file name
        image_file = "hire.png"  # Replace with the name of your image file
        self.image = tk.PhotoImage(file=image_file)

        tk.Label(self.root, text="Welcome to Party Hire Store", bg='#FFC0CB', font=custom_font, fg=text_color).pack(pady=20)
        tk.Button(self.root, text="Start", command=self.start_application, font=custom_font, bg='#FF69B4', fg=text_color, padx=20, pady=10).pack(pady=10)
        tk.Button(self.root, text="Quit", command=self.root.quit, font=custom_font, bg='#FF69B4', fg=text_color, padx=20, pady=10).pack(pady=10)

    def start_application(self):
        self.root.withdraw()
        main_window = tk.Toplevel(self.root)
        ThePartyHireStore(main_window, self.root)


if __name__ == "__main__":
    root = tk.Tk()
    TheOpeningMenu(root)
    root.mainloop()
