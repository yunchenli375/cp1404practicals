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
        longest_word_length = max(longest_word_length, len(word))
        word_count[word] = word_count.get(word, 0) + 1
    words_with_counts = list(word_count.items())
    words_with_counts.sort()
    for word, count in words_with_counts:
        print(f"{word:{longest_word_length}} : {count}")


main()
