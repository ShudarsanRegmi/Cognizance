import tkinter as tk

class Sidebar(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#2C3E50", width=250)
        self.parent = parent

        # Title Label
        title_label = tk.Label(self, text="Skyways Flight", font=("Helvetica", 20, "bold"), fg="#FFFFFF", bg="#2C3E50", pady=20)
        title_label.pack(fill="x")

        # Style for sidebar buttons
        button_style = {"font": ("Helvetica", 14), "fg": "#FFFFFF", "bg": "#34495E", "activebackground": "#1ABC9C", "activeforeground": "#FFFFFF", "bd": 0}

        # Buttons for page navigation
        book_flight_btn = tk.Button(self, text="Homepage",cursor="hand2", command=lambda: self.parent.show_frame("HomePage"), **button_style)
        book_flight_btn.pack(fill="x", padx=10, pady=10)

        book_flight_btn = tk.Button(self, text="Book a new flight", cursor="hand2", command=lambda: self.parent.show_frame("BookFlightPage"), **button_style)
        book_flight_btn.pack(fill="x", padx=10, pady=10)

        view_flight_btn = tk.Button(self, text="View booked flight", cursor="hand2", command=lambda: self.parent.show_frame("ViewBookedFlightPage"), **button_style)
        view_flight_btn.pack(fill="x", padx=10, pady=10)

        view_all_flights_btn = tk.Button(self, text="View all Flights", cursor="hand2", command=lambda: self.parent.show_frame("ViewAvailableFlightsPage"), **button_style)
        view_all_flights_btn.pack(fill="x", padx=10, pady=10)

        admin_btn = tk.Button(self, text="Go to admin page", cursor="hand2", command=lambda: self.parent.show_frame("AdminPage"), **button_style)
        admin_btn.pack(fill="x", padx=10, pady=10)
