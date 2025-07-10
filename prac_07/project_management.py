"""
CP1404 Practical
Load and save a data file and use a list of Project objects
"""

from project import ProjectManager

DEFAULT_DATA_FILE = "projects.txt"

MAIN_MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd a new project
- (U)pdate a project"""


def main():
    """program entrypoint"""
    print("Welcome to Pythonic Project Management")
    path = DEFAULT_DATA_FILE
    manager = initialize_project_manager(path)
    choice = menu(MAIN_MENU, "LSDFAUQ")
    while choice != "Q":
        if choice == "L":
            new_path = input("Enter the filename to load projects from: ")
            try:
                manager = initialize_project_manager(new_path)
                path = new_path
            except FileNotFoundError:
                print(f"File {new_path} not found. No update made.")
        elif choice == "S":
            new_path = input("Enter the filename to save projects to: ")
            if len(new_path) == 0:
                print("No filename provided, not saving.")
            else:
                manager.dump(open(new_path, "w"))
        elif choice == "D":
            manager.display()
        elif choice == "F":
            manager.display_filtered_projects_by_date()
        elif choice == "A":
            manager.add_project_interactively()
        else:  # U
            manager.update_project_interactively()
        choice = menu(MAIN_MENU, "LSDFAUQ")
    prompt_to_save(manager, path)
    print("Thank you for using custom-built project management software.")

