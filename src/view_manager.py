import tkinter as tk
import importlib

class ViewManager:
    def __init__(self, container):
        self.container = container
        self.views = {}

    def register_view(self, name, view_class):
        #Instantiate and register a view with a unique name.
        view = view_class(self.container, self)
        self.views[name] = view
        view.grid(row=0, column=0, sticky='nsew')

    def load_project_view(self, project_name):
        # Dynamically load a project view fromthe projects folder.
        if project_name is self.views:
            self.show_view(project_name)
            return
        
        try:
            module_path = f"projecthub.projects.{project_name}.view"
            project_module = importlib.import_module(module_path)
            ProjectViewClass = getattr(project_module, "ProjectView")

            view_instance = ProjectViewClass(self.container, self)
            self.views[project_name] = view_instance
            view_instance.grid(row=0, column=0, sticky="nsew")

            self.show_view(project_name)
        
        except (ModuleNotFoundError, AttributeError) as e:
            print(f"Error loading project {project_name}: {e}")
            

    def show_view(self, name):
        view = self.views.get(name)
        if view:
            view.tkraise()
        else:
            raise ValueError(f"View '{name}' not found.")