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


def menu(prompt, expected_choice):
    """display a menu and get a valid user choice in expected choice"""
    print(prompt)
    choice = input(">>> ")
    while len(choice) == 0 or choice[0].upper() not in expected_choice:
        choice = input("Invalid choice, please try again. >>> ")
    return choice[0].upper()


def initialize_project_manager(filename):
    """create a ProjectManager instance from a file"""
    in_file = open(filename)
    project_manager = ProjectManager(in_file)
    in_file.close()
    print(f"Loaded {len(project_manager)} projects from {filename}")
    return project_manager


def prompt_to_save(manager, path):
    """Prompt the user to save the project manager's data."""
    if input(f"Would you like to save to {path}? ").lower()[0] == "y":
        manager.dump(open(path, "w"))
        print(f"Projects saved to {path}")


main()
