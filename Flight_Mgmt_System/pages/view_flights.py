import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ViewAvailableFlightsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg="#F2F2F2")  # Light grey background for a clean look

        # Page content for "View Available Flights"
        label = tk.Label(self, text="Available Flights", font=("Helvetica", 22, "bold"), fg="#2C3E50", bg="#F2F2F2")
        label.pack(pady=30)

        # Treeview for displaying flight details
        self.tree = ttk.Treeview(self, columns=("flight_number", "start", "destination", "price"), show="headings")
        self.tree.heading("flight_number", text="Flight Number")
        self.tree.heading("start", text="Start Location")
        self.tree.heading("destination", text="Destination")
        self.tree.heading("price", text="Price")

        self.tree.column("flight_number", width=150, anchor="center")
        self.tree.column("start", width=200, anchor="center")
        self.tree.column("destination", width=200, anchor="center")
        self.tree.column("price", width=100, anchor="center")

        self.tree.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        # Refresh button to reload flight data
        refresh_button = tk.Button(self, text="Refresh", cursor="hand2", font=("Helvetica", 14, "bold"), bg="#1ABC9C", fg="#FFFFFF", activebackground="#16A085", activeforeground="#FFFFFF", bd=0, padx=10, pady=5, command=self.load_flights)
        refresh_button.pack(pady=20)

        # Load flights on page initialization
        self.load_flights()

    def load_flights(self):
        """Load flight data from the database and populate the Treeview."""
        try:
            # Assuming you have a method in your Database class to get all flights
            # flights = self.controller.db.execute_query("SELECT flight_number, start, destination, price FROM flights")
            flights = self.controller.db.get_all_flights()
            print(flights)
            # Clear the current data in the Treeview
            for item in self.tree.get_children():
                self.tree.delete(item)
                
            # Insert new data
            for flight in flights:
                self.tree.insert("", tk.END, values=flight)
                
        except Exception as e:
            messagebox.showerror("Database Error", str(e))
