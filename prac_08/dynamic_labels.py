"""
CP1404 Practical
Kivy GUI program having dynamic labels
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Kivy App to demonstrate dynamic labels."""

    def __init__(self, **kwargs):
        """Initialize the app."""
        super().__init__(**kwargs)
        self.title = "Dynamic Labels Example"
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
