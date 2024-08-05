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
        self.item_combobox = ttk.Combobox(self.root, values=["Table", "Chair", "Tent", "Sound System", "Lights"], font=custom_font, foreground=te
