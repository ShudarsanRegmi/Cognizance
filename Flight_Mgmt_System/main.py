import tkinter as tk
from tkinter import ttk
from sidebar import Sidebar
from pages.book_flight import BookFlightPage
from pages.view_flight import ViewBookedFlightPage
from pages.admin_page import AdminPage
from pages.view_flights import ViewAvailableFlightsPage
from pages.homepage import HomePage

from database import Database


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.db = Database(host='localhost', user='shudarsan', password='shudarsan@localhost', database='flight_management')
        self.db.connect()

        # Set up the main container
        self.title("Flight Booking System")
        self.geometry("900x500")
        self.config(bg="#EDEDED", padx=10, pady=10)  # Background color for the main window #EDEDED

        # Create main layout with sidebar and content area
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Initialize sidebar
        self.sidebar = Sidebar(self)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        # Right-side content area that will hold different pages
        self.content_area = tk.Frame(self, bg="#dedede") # black is content area
        self.content_area.grid(row=0, column=1, sticky="ns", padx=20, pady=20)

        # Dictionary to hold pages
        self.frames = {}

        # Add pages to the application
        for Page in (BookFlightPage, ViewBookedFlightPage, AdminPage, ViewAvailableFlightsPage, HomePage):
            page_name = Page.__name__
            frame = Page(parent=self.content_area, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=1, column=1, sticky="nsew")

        # Show the initial page
        self.show_frame("HomePage")
        # Todo: change this into homepage

    def show_frame(self, page_name):
        """Raise the frame corresponding to the page name."""
        frame = self.frames[page_name]
        frame.tkraise()

    def __del__(self):
        self.db.disconnect()    

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
