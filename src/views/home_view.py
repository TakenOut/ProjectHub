import tkinter as tk

class HomeView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Home View", font=("Arial", 16)).pack(pady=20)
        tk.Button(self, text="Projects", font=("Arial", 16), command=lambda: self.controller.show_view("selector")).pack()