"""
CP1404 Practical
Kivy GUI program to convert miles to kilometers
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

KM_PER_MILE = 1.60934


class MilesToKmConverterApp(App):
    """Kivy App to convert miles to kilometers."""

    output_text = StringProperty()

