import tkinter as tk
from tkinter import ttk, messagebox

class BookFlightPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg="#F8F9FA")  # Light gray background

        # Page content for "Book a new flight"
        label = tk.Label(self, text="Book a New Flight", font=("Helvetica", 22, "bold"), fg="#2C3E50", bg="#F8F9FA")
        label.pack(pady=30)

        # Departure input
        departure_label = tk.Label(self, text="Departure:", font=("Helvetica", 14), bg="#F8F9FA", fg="#2C3E50")
        departure_label.pack(pady=5)
        self.departure_entry = ttk.Entry(self, width=30)
        self.departure_entry.pack(pady=5)

        # Destination input
        destination_label = tk.Label(self, text="Destination:", font=("Helvetica", 14), bg="#F8F9FA", fg="#2C3E50")
        destination_label.pack(pady=5)
        self.destination_entry = ttk.Entry(self, width=30)
        self.destination_entry.pack(pady=5)

        # Search button
        search_button = tk.Button(self, text="Search", cursor="hand2", font=("Helvetica", 14, "bold"), bg="#1ABC9C", fg="#FFFFFF", activebackground="#16A085", activeforeground="#FFFFFF", bd=0, padx=10, pady=5, command=self.search_flights)
        search_button.pack(pady=20)

        # Treeview for displaying available flights
        self.tree = ttk.Treeview(self, columns=("flight_number", "start", "destination", "price"), show="headings", selectmode="browse")
        self.tree.heading("flight_number", text="Flight Number")
        self.tree.heading("start", text="Departure")
        self.tree.heading("destination", text="Destination")
        self.tree.heading("price", text="Price")
        self.tree.column("price", width=100, anchor="e")
        self.tree.pack(pady=20, fill=tk.BOTH, expand=True)

        # Book Flight button
        self.book_button = tk.Button(self, text="Book Selected Flight", cursor="hand2", font=("Helvetica", 14, "bold"), bg="#E74C3C", fg="#FFFFFF", activebackground="#C0392B", activeforeground="#FFFFFF", bd=0, padx=10, pady=5, command=self.book_flight)
        self.book_button.pack(pady=20)

    def search_flights(self):
        """Search for flights and display results in the Treeview."""
        departure = self.departure_entry.get()
        destination = self.destination_entry.get()
        
        # Clear previous results
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Fetch available flights from the database
        flights = self.controller.db.get_available_flights(departure, destination)
        
        # Insert flights into Treeview
        for flight in flights:
            flight_number, start, dest, price = flight
            self.tree.insert("", "end", values=(flight_number, start, dest, price))

    def book_flight(self):
        """Handle flight booking."""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a flight to book.")
            return
        
        flight_number = self.tree.item(selected_item[0])['values'][0]
        user_name = "Guest"  # Replace this with actual username retrieval
        self.controller.db.book_flight(user_name, flight_number)
        messagebox.showinfo("Booking", f"Flight {flight_number} booked successfully!")
