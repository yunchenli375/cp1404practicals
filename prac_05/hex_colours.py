"""
CP1404 Practical
Hexadecimal colour codes in a dictionary
"""

HEX_COLOURS = {
    "black": "#000000",
    "gray": "#BEBEBE",
    "white": "#FFFFFF",
    "red1": "#FF0000",
    "green1": "#00FF00",
    "blue1": "#0000FF",
    "yellow1": "#FFFF00",
    "cyan1": "#00FFFF",
    "magenta1": "#FF00FF",
}


def main():
    """program entrypoint"""
    color_name = input("Enter a colour name: ")
    while color_name != "":
        color_name = color_name.lower()
        if color_name in HEX_COLOURS:
            print(f"{HEX_COLOURS[color_name].lower()}")
        else:
            print("Color not found")
        color_name = input("Enter a colour name: ")


main()
