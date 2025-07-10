"""
CP1404 Practical
Estimated time: 45 minutes
Actual time: 120 minutes
"""

from datetime import datetime
import csv

DATE_FORMAT = "%d/%m/%Y"
FILE_DELIMITER = "\t"


class Project:
    """Represent a project instance."""

    def __init__(self, name, date, priority, cost_estimate, completion_percentage):
        """Initialize a project with name, date, priority, cost estimate, and completion percentage."""
        self.name = name
        self.date = datetime.strptime(date, DATE_FORMAT)
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __lt__(self, other):
        """Compare projects based on their priority."""
        return self.priority < other.priority

    def __str__(self):
        """Return a string representation of the project."""
        return (
            f"{self.name}, start: {self.date.strftime(DATE_FORMAT)}, priority {self.priority}, "
            f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"
        )


# Since creating a class can deal with many problems,
# why not creating another class to deal with more problems?
class ProjectManager:
    """Manage a collection of projects."""

    def __init__(self, source):
        """Initialize an empty project manager from a input file-like object."""
        self.projects = []
        source.readline()
        reader = csv.reader(source, delimiter=FILE_DELIMITER)
        for row in reader:
            name, date, priority, cost_estimate, completion_percentage = row
            project = Project(
                name,
                date,
                int(priority),
                float(cost_estimate),
                int(completion_percentage),
            )
            self.projects.append(project)

    def __len__(self):
        """Return the number of projects."""
        return len(self.projects)

    def dump(self, sink):
        """Dump all projects to a file-like object"""
        print(
            FILE_DELIMITER.join(
                [
                    "Name",
                    "Start Date",
                    "Priority",
                    "Cost Estimate",
                    "Completion Percentage",
                ]
            ),
            file=sink,
        )
        # use default line terminator will result in an extra empty line
        writer = csv.writer(sink, delimiter=FILE_DELIMITER, lineterminator="\n")
        for project in self.projects:
            writer.writerow(
                [
                    project.name,
                    project.date.strftime(DATE_FORMAT),
                    project.priority,
                    project.cost_estimate,
                    project.completion_percentage,
                ]
            )

    def get_selected_project_interactively(self):
        """Return a project index selected by the user interactively."""
        selected_project = input("Enter the project index to update: ")
        while (
            not selected_project.isdigit()
            or int(selected_project) < 0
            or int(selected_project) >= len(self.projects)
        ):
            selected_project = input("Invalid index, please try again: ")
        return int(selected_project)

    def display(self):
        """Display two groups: incomplete projects; completed projects, both sorted by priority"""
        # Sorting through indices(pointers) could be more efficient than sorting the whole list
        uncompleted_idx = []
        completed_idx = []
        for idx, project in enumerate(self.projects):
            if project.completion_percentage == 100:
                completed_idx.append(idx)
            else:
                uncompleted_idx.append(idx)

        # It would become very verbose, were it not for the lambda expression
        uncompleted_idx.sort(key=lambda x: self.projects[x])
        completed_idx.sort(key=lambda x: self.projects[x])

        print("Incomplete Projects:")
        for idx in uncompleted_idx:
            print(f"\t{self.projects[idx]}")

        print("Completed Projects:")
        for idx in completed_idx:
            print(f"\t{self.projects[idx]}")

    def update_project_interactively(self):
        """Modify the completion % and/or priority of a project interactively."""
        for idx, project in enumerate(self.projects):
            print(f"{idx} {project}")

        project_idx = self.get_selected_project_interactively()
        print(f"{self.projects[project_idx]}")
        updated_percentage = get_valid_completion_percentage_interactively(
            "New percentage: ",
            omittable=True,
        )

        if updated_percentage != -1:
            self.projects[project_idx].completion_percentage = updated_percentage

        updated_priority = get_valid_priority_interactively(
            "New priority: ",
            omittable=True,
        )
        if updated_priority != -1:
            self.projects[project_idx].priority = updated_priority

    def add_project_interactively(self):
        """Add a new project interactively."""
        print("Let's add a new project")
        name = get_valid_name_interactively("Name: ")
        date = get_valid_date_interactively("Start date (dd/mm/yyyy): ")
        priority = get_valid_priority_interactively("Priority: ")
        cost_estimate = get_valid_cost_estimate_interactively("Cost estimate: $")
        completion_percentage = get_valid_completion_percentage_interactively(
            "Percent complete: "
        )
        new_project = Project(
            name, date, priority, cost_estimate, completion_percentage
        )
        self.projects.append(new_project)

    def display_filtered_projects_by_date(self):
        """Display projects start after the user-specified date, sorted by date"""
        date_filter = get_valid_date_interactively(
            "Show projects that start after date (dd/mm/yyyy): "
        )
        date_filter = datetime.strptime(date_filter, DATE_FORMAT)
        filtered_idx = []
        for idx, project in enumerate(self.projects):
            if project.date >= date_filter:
                filtered_idx.append(idx)
        for i in sorted(filtered_idx, key=lambda x: self.projects[x].date):
            print(f"{self.projects[i]}")


def get_valid_name_interactively(prompt="Project name: "):
    """Get a valid project name from the user interactively."""
    name = input(prompt)
    while name == "":
        print("Project name cannot be empty.")
        name = input(prompt)
    return name


def get_valid_date_interactively(prompt="Project start date (dd/mm/yyyy): "):
    """Get a valid project start date from the user interactively."""
    date = input(prompt)
    while not is_valid_datetime(date, DATE_FORMAT):
        print("Invalid date format. Please use dd/mm/yyyy.")
        date = input(prompt)
    return date


def is_valid_datetime(date, format):
    """Helper function of ProjectManager.interactively_add_project
    to parse date strings, returns None when parsing fails."""
    # Using try-except handling the logic will unavoidably introduce while True loops,
    # which may lead to very low marks.
    try:
        datetime.strptime(date, format)
    except ValueError:
        return False
    return True


def get_valid_priority_interactively(prompt="Project priority: ", omittable=False):
    """Get a valid project priority from the user interactively.
    Returns -1 if the input is empty and omittable is True."""
    priority = input(prompt)
    while not (
        (priority.isdigit() and int(priority) >= 0) or (omittable and priority == "")
    ):
        print("Priority must be a non-negative integer.")
        priority = input(prompt)
    if priority == "":
        return -1
    return int(priority)


def get_valid_cost_estimate_interactively(prompt="Project cost estimate: "):
    """Get a valid project cost estimate from the user interactively."""
    cost_estimate = input(prompt)
    while not is_valid_cost_estimate(cost_estimate):
        print("Cost estimate must be a valid number.")
        cost_estimate = input(prompt)
    return float(cost_estimate)


def is_valid_cost_estimate(cost_estimate):
    """Helper function of ProjectManager.interactively_add_project,
    returns None when parsing fails or the cost is negative."""
    # Directly parse the string with possible dots,
    # like cost.estimate.replace('.', '') is error-prone,
    # users can enter a string with multiple dots like "1.2.3",
    # which is not a valid float.
    try:
        return float(cost_estimate) >= 0
    except ValueError:
        return False


def get_valid_completion_percentage_interactively(
    prompt="Project completion percentage: ", omittable=False
):
    """Get a valid project completion percentage from the user interactively.
    Returns -1 if the input is empty and omittable is True."""
    completion_percentage = input(prompt)
    while not (
        (
            completion_percentage.isdigit()
            and int(completion_percentage) >= 0
            and int(completion_percentage) <= 100
        )
        or (omittable and completion_percentage == "")
    ):
        print("Completion percentage must be a number between 0 and 100.")
        completion_percentage = input(prompt)
    if completion_percentage == "":
        return -1
    return int(completion_percentage)
