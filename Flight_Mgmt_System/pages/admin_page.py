import tkinter as tk
from tkinter import ttk, messagebox

class AdminPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg="#FFFFFF")

        # Page content for "Admin Page"
        label = tk.Label(self, text="Admin Page", font=("Helvetica", 22, "bold"), fg="#2C3E50", bg="#FFFFFF")
        label.pack(pady=30)

        # Notebook (Tabbed Interface)
        notebook = ttk.Notebook(self)
        notebook.pack(pady=20, padx=20, expand=True)

        # Add Flight Tab
        self.add_flight_tab = tk.Frame(notebook, bg="#FFFFFF")
        notebook.add(self.add_flight_tab, text="Add Flight")

        # View/Delete Flight Tab
        self.view_delete_flight_tab = tk.Frame(notebook, bg="#FFFFFF")
        notebook.add(self.view_delete_flight_tab, text="View/Delete Flights")

        # Add content to each tab
        self.create_add_flight_tab_content()
        self.create_view_delete_flight_tab_content()

        # Bind the tab change event to refresh data in View/Delete Flights tab
        notebook.bind("<<NotebookTabChanged>>", self.on_tab_change)

    def create_add_flight_tab_content(self):
        """Create the UI content for the Add Flight tab."""
        # Flight form
        form_frame = tk.Frame(self.add_flight_tab, bg="#FFFFFF")
        form_frame.pack(pady=20, padx=20, fill="x")

        tk.Label(form_frame, text="Flight Number:", bg="#FFFFFF").grid(row=0, column=0, sticky="e", padx=10, pady=5)
        self.flight_number_entry = tk.Entry(form_frame)
        self.flight_number_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Start Location:", bg="#FFFFFF").grid(row=1, column=0, sticky="e", padx=10, pady=5)
        self.start_entry = tk.Entry(form_frame)
        self.start_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Destination:", bg="#FFFFFF").grid(row=2, column=0, sticky="e", padx=10, pady=5)
        self.destination_entry = tk.Entry(form_frame)
        self.destination_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Price:", bg="#FFFFFF").grid(row=3, column=0, sticky="e", padx=10, pady=5)
        self.price_entry = tk.Entry(form_frame)
        self.price_entry.grid(row=3, column=1, padx=10, pady=5)

        submit_button = tk.Button(self.add_flight_tab, text="Add Flight", command=self.add_flight, bg="#3498DB", fg="#FFFFFF", padx=10, pady=5)
        submit_button.pack(pady=20)

    def create_view_delete_flight_tab_content(self):
        """Create the UI content for the View/Delete Flights tab."""
        # Create a Treeview for displaying flights
        self.tree = ttk.Treeview(self.view_delete_flight_tab, columns=("flight_number", "start", "destination", "price"), show="headings")
        self.tree.heading("flight_number", text="Flight Number")
        self.tree.heading("start", text="Start Location")
        self.tree.heading("destination", text="Destination")
        self.tree.heading("price", text="Price")
        self.tree.column("flight_number", width=120)
        self.tree.column("start", width=150)
        self.tree.column("destination", width=150)
        self.tree.column("price", width=100)
        self.tree.pack(pady=20, fill=tk.BOTH, expand=True)

        # Delete Flight Button
        delete_button = tk.Button(self.view_delete_flight_tab, text="Delete Selected Flight", command=self.delete_flight, bg="#E74C3C", fg="#FFFFFF", padx=10, pady=5)
        delete_button.pack(pady=10)

    def on_tab_change(self, event):
        """Handle the tab change event to load flights when the user switches to the View/Delete Flights tab."""
        notebook = event.widget
        tab_id = notebook.index(notebook.select())

        # Tab index 1 corresponds to the "View/Delete Flights" tab
        if tab_id == 1:
            self.load_flights()

    def add_flight(self):
        """Add a flight to the database."""
        flight_number = self.flight_number_entry.get()
        start = self.start_entry.get()
        destination = self.destination_entry.get()
        price = self.price_entry.get()

        # Basic validation
        if not flight_number or not start or not destination or not price:
            messagebox.showwarning("Input Error", "All fields must be filled out.")
            return

        try:
            price = float(price)
        except ValueError:
            messagebox.showerror("Input Error", "Price must be a valid number.")
            return

        # Access the Database instance through the controller
        db = self.controller.db

        # Insert into the database
        try:
            db.insert_flight(
                flight_number=flight_number,
                start=start,
                destination=destination,
                price=price
            )
            messagebox.showinfo("Success", "Flight added successfully!")
            self.clear_form_fields()  # Clear the input fields
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def clear_form_fields(self):
        """Clear all form fields after submission."""
        self.flight_number_entry.delete(0, tk.END)
        self.start_entry.delete(0, tk.END)
        self.destination_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)

    def load_flights(self):
        """Load flights from the database into the Treeview."""
        # Clear the current content in the Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Fetch flights from the database
        try:
            flights = self.controller.db.get_all_flights()

            # Populate the Treeview with flights
            for flight in flights:
                self.tree.insert("", "end", values=flight)
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to load flights: {str(e)}")

    def delete_flight(self):
        """Delete the selected flight from the database."""
        selected_item = self.tree.selection()

        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a flight to delete.")
            return

        # Get the flight number of the selected flight
        flight_number = self.tree.item(selected_item[0])['values'][0]

        # Access the Database instance through the controller
        db = self.controller.db

        try:
            db.delete_flight(flight_number)
            messagebox.showinfo("Success", "Flight deleted successfully!")
            self.load_flights()  # Refresh the flights list
        except Exception as e:
            messagebox.showerror("Database Error", str(e))
