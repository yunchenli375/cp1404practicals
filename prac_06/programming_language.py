"""
CP1404 Practicals
Estimated time: 15 minutes
Actual time: 13 minutes
"""


class ProgrammingLanguage:
    """Represent a programming language object."""

    def __init__(self, name, typing, reflection, year):
        """Initialize a ProgrammingLanguage instance.

        name: str, the name of the programming language
        typing: str, could be either "Dynamic" or "Static"
        reflection: bool, whether the language supports reflection
        year: int, the year when the language was invented
        """
        self.name = name
        self.dynamic = typing == "Dynamic"
        self.reflection = reflection
        self.year = year

