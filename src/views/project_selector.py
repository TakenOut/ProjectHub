import tkinter as tk

class ProjectSelector(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Select a Project", font=("Arial", 16)).pack(pady=20)

        projects = ["project1", "project2"]

        for project in projects:
            tk.Button(self, text=project, command=lambda p=project: self.controller.load_project_view(p)).pack(pady=5)

        tk.Button(self, text="Back", command=lambda: self.controller.show_view("home")).pack(pady=20)