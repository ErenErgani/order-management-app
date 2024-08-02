import tkinter as tk
from tkinter import messagebox
from datetime import datetime


class OrderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Order Management")

        self.orders = {}

        self.label = tk.Label(root, text="Enter Order Number:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.add_button = tk.Button(root, text="Add Order", command=self.add_order)
        self.add_button.pack()

        self.listbox = tk.Listbox(root)
        self.listbox.pack()

        self.update_button = tk.Button(root, text="Update Order", command=self.update_order)
        self.update_button.pack()

        self.delete_button = tk.Button(root, text="Delete Order", command=self.delete_order)
        self.delete_button.pack()

        self.archive_button = tk.Button(root, text="Archive Order", command=self.archive_order)
        self.archive_button.pack()


    def add_order(self):
        order_number = self.entry.get()
        if order_number:
            self.orders[order_number] = "Received"
            self.listbox.insert(tk.END, f"{order_number} - Received")
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter an order number.")


    def update_order(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_order = self.listbox.get(selected_index)
            order_number = selected_order.split(" - ")[0]
            current_status = self.orders[order_number]

            if current_status == "Received":
                new_status = "Preparing"
            elif current_status == "Preparing":
                new_status = "Shipped"
            elif current_status == "Shipped":
                new_status = "Delivered"
            else:
                new_status = "Delivered"

            self.orders[order_number] = new_status
            self.listbox.delete(selected_index)
            self.listbox.insert(selected_index, f"{order_number} - {new_status}")
        else:
            messagebox.showwarning("Selection Error", "Please select an order to update.")


    def delete_order(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_order = self.listbox.get(selected_index)
            order_number = selected_order.split(" - ")[0]
            del self.orders[order_number]
            self.listbox.delete(selected_index)
        else:
            messagebox.showwarning("Selection Error", "Please select an order to delete.")


    def archive_order(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_order = self.listbox.get(selected_index)
            order_number = selected_order.split(" - ")[0]
            with open("order_archive.txt", "a") as file:
                file.write(f"{datetime.now()} - {order_number}\n")
            self.delete_order()
        else:
            messagebox.showwarning("Selection Error", "Please select an order to archive.")


if __name__ == "__main__":
    root = tk.Tk()
    app = OrderApp(root)
    root.mainloop()
