import tkinter as tk
from tkinter import messagebox, Label, Button, Entry, ttk

class HolsterOrderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Holster Order Management System (HOMS)")
        self.root.geometry("500x400")
        
        # Store orders in a list
        self.orders = []

        # Title Label with better styling
        self.title_label = Label(root, text="Holster Order Management System", 
                               font=("Arial", 14, "bold"), bg="#2c3e50", fg="white",
                               pady=10, width=40)
        self.title_label.pack(pady=20)

         # Frame for buttons
        button_frame = tk.Frame(root)
        button_frame.pack(expand=True)

        # Styled buttons
        button_style = {"font": ("Arial", 11), "width": 20, "pady": 5}
        
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
        order_window = tk.Toplevel(self.root)
        order_window.title("Place Order")
        order_window.geometry("400x500")
        order_window.configure(bg="#f0f0f0")

        # Form frame
        form_frame = tk.Frame(order_window, bg="#f0f0f0", pady=20)
        form_frame.pack(expand=True)

        # Customer details
        Label(form_frame, text="Enter Customer Details", font=("Arial", 12, "bold"),
              bg="#f0f0f0").pack(pady=10)
        
        # Name entry
        Label(form_frame, text="Name:", bg="#f0f0f0").pack()
        name_entry = Entry(form_frame, width=30)
        name_entry.pack(pady=5)

        # Email entry
        Label(form_frame, text="Email:", bg="#f0f0f0").pack()
        email_entry = Entry(form_frame, width=30)
        email_entry.pack(pady=5)

        # Holster type selection
        Label(form_frame, text="Holster Type:", bg="#f0f0f0").pack()
        holster_type = ttk.Combobox(form_frame, values=["IWB", "OWB", "Appendix", "Duty"],
                                   width=27)
        holster_type.pack(pady=5)

        # Color selection
        Label(form_frame, text="Color:", bg="#f0f0f0").pack()
        color = ttk.Combobox(form_frame, values=["Black", "Brown", "FDE", "OD Green"],
                            width=27)
        color.pack(pady=5)

        # Submit button
        submit_button = Button(form_frame, text="Submit Order", 
                             command=lambda: self.submit_order(name_entry.get(),
                                                            email_entry.get(),
                                                            holster_type.get(),
                                                            color.get(),
                                                            order_window),
                             bg="#3498db", fg="white", width=20)
        submit_button.pack(pady=20)

    def submit_order(self, name, email, holster_type, color, window):
        if not all([name, email, holster_type, color]):
            messagebox.showerror("Input Error", "All fields are required!")
            return
        
        # Create order dictionary
        order = {
            "name": name,
            "email": email,
            "holster_type": holster_type,
            "color": color,
            "status": "Pending"
        }
        
        self.orders.append(order)
        messagebox.showinfo("Success", "Order placed successfully!")
        window.destroy()

    def open_admin_panel(self):
        admin_window = tk.Toplevel(self.root)
        admin_window.title("Order Management")
        admin_window.geometry("600x400")
        admin_window.configure(bg="#f0f0f0")

        # Create treeview for orders
        columns = ("Name", "Email", "Holster Type", "Color", "Status")
        tree = ttk.Treeview(admin_window, columns=columns, show="headings")

        # Set column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100)

        # Add orders to treeview
        for order in self.orders:
            tree.insert("", "end", values=(order["name"], order["email"],
                                         order["holster_type"], order["color"],
                                         order["status"]))

        tree.pack(pady=20, padx=20, fill="both", expand=True)

        # Refresh button
        refresh_btn = Button(admin_window, text="Refresh", command=lambda: self.refresh_orders(tree),
                           bg="#2ecc71", fg="white", width=15)
        refresh_btn.pack(pady=10)

    def refresh_orders(self, tree):
        # Clear existing items
        for item in tree.get_children():
            tree.delete(item)
        
        # Reload orders
        for order in self.orders:
            tree.insert("", "end", values=(order["name"], order["email"],
                                         order["holster_type"], order["color"],
                                         order["status"]))

    def exit_app(self):
        if messagebox.askokcancel("Exit", "Do you want to exit the application?"):
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = HolsterOrderApp(root)
    root.mainloop()
