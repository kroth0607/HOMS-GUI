import tkinter as tk
from tkinter import messagebox, Label, Button, Entry, ttk

# Holster Order Management System (HOMS)
# This application allows users to place holster orders, view order details, and manage order statuses.
# It is built using Python's Tkinter for GUI-based interaction.

class HolsterOrderApp:
    def __init__(self, root):
        """
        Initializes the main application window.
        :param root: The root Tkinter window.
        """
        self.root = root
        self.root.title("Holster Order Management System (HOMS)")
        self.root.geometry("500x400")

        # Title Label - Displays the application title
        self.title_label = Label(root, text="Holster Order Management System", font=("Arial", 14, "bold"))
        self.title_label.pack(pady=10)

        # Buttons - Navigation buttons for the application
        self.order_button = Button(root, text="Place New Order", command=self.open_order_form, width=20)  # Opens order form
        self.order_button.pack(pady=5)

        self.view_orders_button = Button(root, text="View Orders", command=self.open_admin_panel, width=20)  # Opens admin panel
        self.view_orders_button.pack(pady=5)

        self.exit_button = Button(root, text="Exit", command=self.exit_app, width=20)  # Exits the application
        self.exit_button.pack(pady=5)

    def open_order_form(self):
        """
        Opens a new window for placing an order.
        """
        order_window = tk.Toplevel(self.root)
        order_window.title("Place Order")
        order_window.geometry("400x300")

        # Label for order entry section
        Label(order_window, text="Enter Customer Details", font=("Arial", 12, "bold")).pack(pady=5)
        
        # Name entry field
        Label(order_window, text="Name:").pack()
        name_entry = Entry(order_window)
        name_entry.pack()

        # Holster type dropdown selection
        Label(order_window, text="Holster Type:").pack()
        holster_type = ttk.Combobox(order_window, values=["IWB", "OWB", "Appendix", "Duty"])  # Available holster types
        holster_type.pack()

        # Submit order button
        submit_button = Button(order_window, text="Submit Order", command=lambda: self.submit_order(name_entry.get(), holster_type.get()))
        submit_button.pack(pady=10)
    
    def submit_order(self, name, holster_type):
        """
        Validates and submits the order.
        :param name: Customer's name.
        :param holster_type: Selected holster type.
        """
        if not name or not holster_type:
            messagebox.showerror("Input Error", "All fields are required!")  # Show error if fields are empty
            return
        messagebox.showinfo("Order Submitted", f"Order for {name} ({holster_type}) has been placed successfully!")

    def open_admin_panel(self):
        """
        Opens a new window for admin to manage orders.
        """
        admin_window = tk.Toplevel(self.root)
        admin_window.title("Admin Panel")
        admin_window.geometry("400x300")

        # Label for admin panel
        Label(admin_window, text="Order Management", font=("Arial", 12, "bold")).pack(pady=5)
        
        # Update order status button (Feature to be implemented in future updates)
        Button(admin_window, text="Update Order Status", command=lambda: messagebox.showinfo("Feature", "Feature coming soon!"))
        
    def exit_app(self):
        """
        Closes the application.
        """
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = HolsterOrderApp(root)
    root.mainloop()

