import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import random

class ThePartyHireStore:
    def _initial_ (self, root, menu_window):
        self.root = root
        self.menu_window = menu_window
        self.root.title("Party Hire Store")
        #Light pink background
        self.root.configure(bg='#FFC0CB')  

        #Store the data of the inputs
        self.hire_data = []

        #Define what widgets are
        self.create_widgets()

    def create_widgets(self):
        #Choosing the font and style settings
        custom_font = ("Anonymous Pro", 10)
         #Dark purple colour for text
        text_color = "#4B0082" 
        #Making the labels and entries
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

        #Making the buttons
        self.add_button = tk.Button(self.root, text="Hire Item", command=self.add_hire_item, font=custom_font, bg='#FF69B4', fg=text_color)
        self.add_button.grid(row=4, column=0, padx=10, pady=10)

        self.return_button = tk.Button(self.root, text="Return Item", command=self.return_hire_item, font=custom_font, bg='#FF69B4', fg=text_color)
        self.return_button.grid(row=4, column=1, padx=10, pady=10)

        self.quit_button = tk.Button(self.root, text="Quit", command=self.quit_application, font=custom_font, bg='#FF69B4', fg=text_color)
        self.quit_button.grid(row=4, column=2, padx=10, pady=10)

        self.back_button = tk.Button(self.root, text="Back to Menu", command=self.back_to_menu, font=custom_font, bg='#FF69B4', fg=text_color)
        self.back_button.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

        #Making the listbox to display hire items
        self.hire_listbox = tk.Listbox(self.root, width=60, font=custom_font, bg='#FFF0F5', fg=text_color)
        self.hire_listbox.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

    def quit_application(self):
        self.root.destroy()

    def back_to_menu(self):
        #Hide the main application window
        self.root.withdraw()
        #Show the opening menu window
        self.menu_window.deiconify() 

    def add_hire_item(self):
        #Get input values
        customer_name = self.customer_name_entry.get()
        item_hired = self.item_combobox.get()
        quantity = self.quantity_entry.get()

        #Make sure to validate inputs
        if not customer_name:
            messagebox.showerror("Error", "Please enter customer name in order to proceed.")
            return
        if not item_hired:
            messagebox.showerror("Error", "You need to enter the item you choose to hire.")
            return
        if not quantity.isdigit() or not (1 <= int(quantity) <= 500):
            messagebox.showerror("Error", "The quantity must be between 1 and 500.")
            return

        #Generate receipt number
        receipt_number = random.randint(1000, 9999)
        self.receipt_number_entry.config(state='normal')
        self.receipt_number_entry.delete(0, tk.END)
        self.receipt_number_entry.insert(0, receipt_number)
        self.receipt_number_entry.config(state='readonly')

        #Add hire details to the list
        hire_details = f"{customer_name} - Receipt: {receipt_number} - Item: {item_hired} - Quantity: {quantity}"
        self.hire_listbox.insert(tk.END, hire_details)
        self.hire_data.append((receipt_number, hire_details))

        #Make sure clear inputs
        self.customer_name_entry.delete(0, tk.END)
        self.item_combobox.set("")
        self.quantity_entry.delete(0, tk.END)

    def return_hire_item(self):
        receipt_number = simpledialog.askinteger("Return Item", "Please enter your receipt number:")
        if receipt_number is None:
            return

        #Find and remove the hire item/s
        for i, (rn, details) in enumerate(self.hire_data):
            if rn == receipt_number:
                self.hire_listbox.delete(i)
                self.hire_data.pop(i)
                messagebox.showinfo("Returned", f"The item/s you hired with receipt number {receipt_number} has been returned back to the store.")
                return

        messagebox.showerror("Error", f"No item was found with receipt number {receipt_number}. Please try again")

class TheOpeningMenu:
    def __initial__(self, root):
        self.root = root
        self.root.title("Welcome")
         #The Width x Height
        self.root.geometry("300x150")
        #Light pink background
        self.root.configure(bg='#FFC0CB')  

        #The font and style settings
        custom_font = ("Merriweather", 12)
        #Dark purple text
        text_color = "#4B0082" 

        #The welcome label
        tk.Label(self.root, text="Welcome to Party Hire Store", bg='#FFC0CB', font=custom_font, fg=text_color).pack(pady=20)

        # The start button
        tk.Button(self.root, text="Start", command=self.start_application, font=custom_font, bg='#FF69B4', fg=text_color, padx=20, pady=10).pack(pady=10)

        #The quit button
        tk.Button(self.root, text="Quit", command=self.root.quit, font=custom_font, bg='#FF69B4', fg=text_color, padx=20, pady=10).pack(pady=10)

    def start_application(self):
        #Hide the opening menu window
        self.root.withdraw()
        #Create a new window for the main application
        main_window = tk.Toplevel(self.root)
        #Initialize the main application
        ThePartyHireStore(main_window, self.root)  

if __name__ == "__main__":
    root = tk.Tk()
     #Initialise the opening menu
    TheOpeningMenu(root) 
    root.mainloop()
