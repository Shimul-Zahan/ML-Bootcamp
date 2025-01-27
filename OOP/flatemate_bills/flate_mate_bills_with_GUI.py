import tkinter as tk
from tkinter import messagebox


class Flatmate:
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house


class Bill:
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class FlatmatesBillSplitter:
    def __init__(self):
        self.flatmates = []

    def add_flatmate(self, name, days_in_house):
        flatmate = Flatmate(name, days_in_house)
        self.flatmates.append(flatmate)

    def calculate_shares(self, bill):
        total_days = sum(flatmate.days_in_house for flatmate in self.flatmates)
        shares = {}
        for flatmate in self.flatmates:
            shares[flatmate.name] = round((flatmate.days_in_house / total_days) * bill.amount, 2)
        return shares


class BillSplitterGUI:
    def __init__(self, root):
        self.splitter = FlatmatesBillSplitter()
        self.root = root
        self.root.title("Flatmates Bill Splitter")

        # Flatmate input section
        self.name_label = tk.Label(root, text="Flatmate Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.days_label = tk.Label(root, text="Days Stayed:")
        self.days_label.grid(row=1, column=0, padx=5, pady=5)
        self.days_entry = tk.Entry(root)
        self.days_entry.grid(row=1, column=1, padx=5, pady=5)

        self.add_flatmate_button = tk.Button(root, text="Add Flatmate", command=self.add_flatmate)
        self.add_flatmate_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Bill input section
        self.bill_label = tk.Label(root, text="Total Bill Amount:")
        self.bill_label.grid(row=3, column=0, padx=5, pady=5)
        self.bill_entry = tk.Entry(root)
        self.bill_entry.grid(row=3, column=1, padx=5, pady=5)

        self.period_label = tk.Label(root, text="Billing Period:")
        self.period_label.grid(row=4, column=0, padx=5, pady=5)
        self.period_entry = tk.Entry(root)
        self.period_entry.grid(row=4, column=1, padx=5, pady=5)

        # Calculate and display results
        self.calculate_button = tk.Button(root, text="Calculate Shares", command=self.calculate_shares)
        self.calculate_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.result_text = tk.Text(root, width=50, height=10)
        self.result_text.grid(row=6, column=0, columnspan=2, pady=10)

    def add_flatmate(self):
        name = self.name_entry.get()
        try:
            days = int(self.days_entry.get())
            if not (1 <= days <= 31):
                raise ValueError
        except ValueError:
            messagebox.showerror("Input Error", "Days must be a number between 1 and 31.")
            return

        self.splitter.add_flatmate(name, days)
        self.name_entry.delete(0, tk.END)
        self.days_entry.delete(0, tk.END)
        messagebox.showinfo("Success", f"Flatmate {name} added successfully!")

    def calculate_shares(self):
        try:
            amount = float(self.bill_entry.get())
            period = self.period_entry.get()
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid bill amount.")
            return

        bill = Bill(amount, period)
        shares = self.splitter.calculate_shares(bill)

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Bill Period: {bill.period}\n")
        self.result_text.insert(tk.END, f"Total Bill Amount: ${bill.amount:.2f}\n\n")
        for name, share in shares.items():
            self.result_text.insert(tk.END, f"{name} owes: ${share:.2f}\n")


if __name__ == "__main__":
    root = tk.Tk()
    gui = BillSplitterGUI(root)
    root.mainloop()
