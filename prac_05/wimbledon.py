"""
Wimbledon
Estimate: 15 minutes
Actual:   11 minutes
"""


def main():
    """program entrypoint"""
    names_to_championships = {}
    countries_with_champions = set()
    # utf-8 encoding must be specified, otherwise it will fail with a UnicodeDecodeError
    with open("wimbledon.csv", encoding="utf-8") as in_file:
        # skip the header line
        in_file.readline()
        for entry in in_file:
            # strip is used to removing the trailing newline character
            items = entry.strip().split(",")
            countries_with_champions.add(items[1])
            names_to_championships[items[2]] = (
                names_to_championships.get(items[2], 0) + 1
            )

