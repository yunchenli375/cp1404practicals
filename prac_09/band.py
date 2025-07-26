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
