"""
CP1404 Practical
A program prompting the user for a page title or search phrase, printing the
details of the page
"""

import wikipedia


def main():
    """program entrypoint"""
    query = input("Enter page title: ")
    while query != "":
        try:
            page = wikipedia.page(query, auto_suggest=False)
            print(page.content.splitlines()[0])
            print(page.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print(
                "We need a more specific title. Try one of the following, or a new search:"
            )
            print(e.options)
        except wikipedia.exceptions.PageError:
            print("Page id does not match any pages. Try another id!")
        print()
        query = input("Enter page title: ")
    print("Thank you.")


