import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Requires Pillow library for handling images

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg="#F4F4F9")  # A light background color

        # Make the layout responsive
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create the hero section with a background image and text overlay
        self.create_hero_section()

    def create_hero_section(self):
        """Creates the hero section with a background image and text overlay."""
        # Load a background image for the hero section
        self.bg_image = Image.open("plane_hero.jpg")  # Make sure the image is in the correct directory
        self.bg_image = self.bg_image.resize((1600, 900), Image.Resampling.LANCZOS)  # Resize for a large resolution
        self.bg_image_tk = ImageTk.PhotoImage(self.bg_image)

        # Create a label with the background image
        bg_label = tk.Label(self, image=self.bg_image_tk)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Make the image fill the window dynamically

        # Create an overlay frame for the hero text and buttons with a semi-transparent background
        overlay_frame = tk.Frame(self, bg="black")  # Semi-transparent black for overlay (80 hex for transparency)
        overlay_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relwidth=0.7, relheight=0.4)  # Center the overlay

        # Add a heading (title) to the hero section
        title_label = tk.Label(
            overlay_frame,
            text="SkyWays Airlines",
            font=("Helvetica", 40, "bold"),
            fg="#FFFFFF",
            bg="black",  # Solid black background for the text
            padx=20,
            pady=20
        )
        title_label.pack(pady=(30, 10))

        # Add a description text below the title with soft white color
        description_label = tk.Label(
            overlay_frame,
            text="Flight Management",
            font=("Helvetica", 18),
            fg="#CCCCCC",
            bg="black",  # Matching background for a cohesive look
            wraplength=800,
            justify="center"
        )
        description_label.pack(pady=10)

        # Add "Get Started" button with improved button styling
        get_started_button = tk.Button(
            overlay_frame,
            text="Get Started",
            font=("Helvetica", 16, "bold"),
            bg="#007BFF",  # Modern blue color for buttons
            fg="#FFFFFF",
            padx=30,
            pady=15,
            activebackground="#0056b3",
            activeforeground="#FFFFFF",
            relief="flat",
            command=self.get_started
        )
        get_started_button.pack(pady=(20, 10))

        # Add "Learn More" button with consistent styling
        learn_more_button = tk.Button(
            overlay_frame,
            text="Learn More",
            font=("Helvetica", 16, "bold"),
            bg="#28A745",  # Modern green color for the Learn More button
            fg="#FFFFFF",
            padx=30,
            pady=15,
            activebackground="#218838",
            activeforeground="#FFFFFF",
            relief="flat",
            command=self.learn_more
        )
        learn_more_button.pack(pady=10)

    def get_started(self):
        """Handle the 'Get Started' button click."""
        self.controller.show_frame("ViewAvailableFlightsPage")

    def learn_more(self):
        """Handle the 'Learn More' button click."""
        tk.messagebox.showinfo("Learn More", "This is where you can learn more about the application.")
