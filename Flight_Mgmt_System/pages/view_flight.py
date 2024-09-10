import tkinter as tk
from tkinter import ttk, messagebox

class ViewBookedFlightPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg="#FFFFFF")

        # Page content for "View booked flight"
        label = tk.Label(self, text="View Booked Flights", font=("Helvetica", 22, "bold"), fg="#2C3E50", bg="#FFFFFF")
        label.pack(pady=30)

        # Create a Treeview for displaying booked flights
        self.tree = ttk.Treeview(self, columns=("booking_id", "flight_number", "start", "destination"), show="headings")
        self.tree.heading("booking_id", text="Booking ID")
        self.tree.heading("flight_number", text="Flight Number")
        self.tree.heading("start", text="Departure")
        self.tree.heading("destination", text="Destination")
        self.tree.column("booking_id", width=100)
        self.tree.column("flight_number", width=120)
        self.tree.column("start", width=150)
        self.tree.column("destination", width=150)
        self.tree.pack(pady=20, fill=tk.BOTH, expand=True)

        # Refresh button to manually reload booked flights
        refresh_button = tk.Button(self, text="Refresh", cursor="hand2", font=("Helvetica", 14, "bold"), bg="#3498DB", fg="#FFFFFF", activebackground="#2980B9", activeforeground="#FFFFFF", bd=0, padx=10, pady=5, command=self.load_booked_flights)
        refresh_button.pack(pady=10)

    def load_booked_flights(self):
        """Load booked flights into the Treeview."""
        user_name = "Guest"  # Replace with actual user name retrieval logic

        # Clear the current content in the treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Fetch booked flights from the database
        booked_flights = self.controller.db.get_booked_flights(user_name)

        # Populate the Treeview with booked flights
        if booked_flights:
            for flight in booked_flights:
                booking_id, flight_number, start, destination = flight
                self.tree.insert("", "end", values=(booking_id, flight_number, start, destination))
        else:
            messagebox.showinfo("Info", "No flights booked yet.")

    def tkraise(self, aboveThis=None):
        """Override tkraise to load booked flights whenever the page is shown."""
        super().tkraise(aboveThis)
        self.load_booked_flights()
