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




