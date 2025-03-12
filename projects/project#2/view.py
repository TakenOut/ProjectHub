import tkinter as tk

class ProjectView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()


    def create_widgets(self):
        tk.Label(self, text="Welcome to Project#1", font=("Arial", 16)).pack(pady=20)
        tk.Button(self, text="Back", command=lambda: self.controller.show_view("home")).pack()
