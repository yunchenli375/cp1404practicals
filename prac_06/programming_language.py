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

    def is_dynamic(self):
        """returns whether the language is dynamically typed"""
        return self.dynamic

    def __str__(self):
        """return a readable string representation of the instance"""
        return f"{self.name}, {'Dynamic' if self.dynamic else 'Static'} Typing, Reflection={self.reflection}, Year={self.year}"
