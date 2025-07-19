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

    def build(self):
        """Build the GUI from the kv file."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        for name in self.names:
            self.root.ids.main.add_widget(Label(text=name))
        return self.root
