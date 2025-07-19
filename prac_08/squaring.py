"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Lindsay Ward, IT@JCU, modified by Yunchen Li
Started 13/10/2015, modified in 2025
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = "Lindsay Ward and Yunchen Li"


class SquareNumberApp(App):
    """SquareNumberApp is a Kivy App for squaring a number"""

    def build(self):
        """build the Kivy app from the kv file"""
        Window.size = (200, 100)
        self.title = "Square Number"
        self.root = Builder.load_file("squaring.kv")
        return self.root
