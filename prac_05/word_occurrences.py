"""
Word Occurrences
Estimate: 10 minutes
Actual:   5 minutes
"""


def main():
    """program entrypoint"""
    text = input("Enter some text: ")
    word_count = {}
    longest_word_length = 0
    for word in text.split():
        word = word.lower().strip(".,!?\"'()[]{};:")

