import tkinter as tk
from view_manager import ViewManager
from views.home_view import HomeView
from views.project_selector import ProjectSelector


def main():
    root = tk.Tk()
    root.title("Project Hub")
    root.geometry("800x600")

    # Configure
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    # Initialize the view manager
    view_manager = ViewManager(root)

    # Register all views
    view_manager.register_view("home", HomeView)
    view_manager.register_view("selector", ProjectSelector)

    # Start with the home view
    view_manager.show_view("home")

    root.mainloop()

if __name__ == "__main__":
    main()


