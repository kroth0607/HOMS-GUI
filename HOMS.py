# Holster Order Management System (HOMS)
# A GUI application for managing custom holster orders using tkinter
# Allows users to place new orders and administrators to view/manage existing orders

import tkinter as tk
from tkinter import messagebox, Label, Button, Entry, ttk

class HolsterOrderApp:
    """
    Main application class for the Holster Order Management System
    Handles the creation of the main window and manages all order operations
    """
    def __init__(self, root):
        self.root = root  # Main window instance
        self.root.title("Holster Order Management System (HOMS)")
        self.root.geometry("500x400")  # Set initial window size
        
        self.orders = []  # List to store all order dictionaries

        # Create main title label with custom styling
        self.title_label = Label(root, text="Holster Order Management System", 
                               font=("Arial", 14, "bold"), bg="#2c3e50", fg="white",
                               pady=10, width=40)
        self.title_label.pack(pady=20)

        # Create frame to organize buttons
        button_frame = tk.Frame(root)
        button_frame.pack(expand=True)

        # Define common button styling
        button_style = {"font": ("Arial", 11), "width": 20, "pady": 5}
        
        # Create main navigation buttons
        self.order_button = Button(button_frame, text="Place New Order", 
                                 command=self.open_order_form, bg="#3498db", fg="black",
                                 **button_style)
        self.order_button.pack(pady=10)

        self.view_orders_button = Button(button_frame, text="View Orders", 
                                       command=self.open_admin_panel, bg="#2ecc71", 
                                       fg="black", **button_style)
        self.view_orders_button.pack(pady=10)

        self.exit_button = Button(button_frame, text="Exit", command=self.exit_app,
                                bg="#e74c3c", fg="black", **button_style)
        self.exit_button.pack(pady=10)

    def open_order_form(self):
        """
        Creates and displays a new window for placing orders
        Contains form fields for customer details and order specifications
        """
        order_window = tk.Toplevel(self.root)
        order_window.title("Place Order")
        order_window.geometry("400x500")
        order_window.configure(bg="#f0f0f0")

        # Create frame to contain form elements
        form_frame = tk.Frame(order_window, bg="#f0f0f0", pady=20)
        form_frame.pack(expand=True)

        # Form title
        Label(form_frame, text="Enter Customer Details", font=("Arial", 12, "bold"),
              bg="#f0f0f0").pack(pady=10)
        
        # Customer name input field
        Label(form_frame, text="Name:", bg="#f0f0f0").pack()
        name_entry = Entry(form_frame, width=30)  # Text field for customer name
        name_entry.pack(pady=5)

        # Customer email input field
        Label(form_frame, text="Email:", bg="#f0f0f0").pack()
        email_entry = Entry(form_frame, width=30)  # Text field for customer email
        email_entry.pack(pady=5)

        # Holster type dropdown selection
        Label(form_frame, text="Holster Type:", bg="#f0f0f0").pack()
        holster_type = ttk.Combobox(form_frame, values=["IWB", "OWB", "Appendix", "Duty"],
                                   width=27)  # Dropdown for holster types
        holster_type.pack(pady=5)

        # Color dropdown selection
        Label(form_frame, text="Color:", bg="#f0f0f0").pack()
        color = ttk.Combobox(form_frame, values=["Black", "Brown", "FDE", "OD Green"],
                            width=27)  # Dropdown for color options
        color.pack(pady=5)

        # Submit button with lambda function to pass form values
        submit_button = Button(form_frame, text="Submit Order", 
                             command=lambda: self.submit_order(name_entry.get(),
                                                            email_entry.get(),
                                                            holster_type.get(),
                                                            color.get(),
                                                            order_window),
                             bg="#3498db", fg="white", width=20)
        submit_button.pack(pady=20)

    def submit_order(self, name, email, holster_type, color, window):
        """
        Processes the order submission
        Args:
            name (str): Customer's name
            email (str): Customer's email
            holster_type (str): Selected holster type
            color (str): Selected color
            window (Toplevel): Reference to order form window
        """
        # Validate that all fields are filled
        if not all([name, email, holster_type, color]):
            messagebox.showerror("Input Error", "All fields are required!")
            return
        
        # Create new order dictionary with customer and product details
        order = {
            "name": name,
            "email": email,
            "holster_type": holster_type,
            "color": color,
            "status": "Pending"  # Initial status for new orders
        }
        
        self.orders.append(order)  # Add order to master list
        messagebox.showinfo("Success", "Order placed successfully!")
        window.destroy()  # Close order form window

    def open_admin_panel(self):
        """
        Creates and displays the admin panel window
        Shows all orders in a table format with ability to refresh
        """
        admin_window = tk.Toplevel(self.root)
        admin_window.title("Order Management")
        admin_window.geometry("600x400")
        admin_window.configure(bg="#f0f0f0")

        # Create table structure for orders
        columns = ("Name", "Email", "Holster Type", "Color", "Status")
        tree = ttk.Treeview(admin_window, columns=columns, show="headings")

        # Configure column headers
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100)

        # Populate table with existing orders
        for order in self.orders:
            tree.insert("", "end", values=(order["name"], order["email"],
                                         order["holster_type"], order["color"],
                                         order["status"]))

        tree.pack(pady=20, padx=20, fill="both", expand=True)

        # Add refresh button to update order list
        refresh_btn = Button(admin_window, text="Refresh", command=lambda: self.refresh_orders(tree),
                           bg="#2ecc71", fg="white", width=15)
        refresh_btn.pack(pady=10)

    def refresh_orders(self, tree):
        """
        Updates the order list display in the admin panel
        Args:
            tree (ttk.Treeview): Reference to the order table widget
        """
        # Remove all current entries
        for item in tree.get_children():
            tree.delete(item)
        
        # Repopulate with current order list
        for order in self.orders:
            tree.insert("", "end", values=(order["name"], order["email"],
                                         order["holster_type"], order["color"],
                                         order["status"]))

    def exit_app(self):
        """
        Handles application exit with confirmation dialog
        """
        if messagebox.askokcancel("Exit", "Do you want to exit the application?"):
            self.root.quit()

# Application entry point
if __name__ == "__main__":
    root = tk.Tk()  # Create main window
    app = HolsterOrderApp(root)  # Initialize application
    root.mainloop()  # Start event loop
