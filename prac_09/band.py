"""
CP1404 Practical
Band class
It seems that all members of a band could only play guitar,
which is not consistent with our cognition of a band.
It is better to use a more general class(abstract base class) like Instrument,
and let the Guitar class inherit from it.
Then the musician's instruments should be a list of Instrument objects.
"""

from musician import Musician


class Band:
    """Band class consists of musicians."""

    def __init__(self, name):
        """create a band with no musicians."""
        self.name = name
        self.musicians: list[Musician] = []

    def __str__(self):
        """Return a string representation of a Band."""
        return (
            f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"
        )

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing all musicians playing their first instrument."""
        if not self.musicians:
            return f"{self.name} has no musicians!"
        return "\n".join(musician.play() for musician in self.musicians)
