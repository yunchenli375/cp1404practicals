"""
CP1404 Practicals
language program
"""

from programming_language import ProgrammingLanguage

YEAR_PYTHON_INVENTED = 1991
YEAR_RUBY_INVENTED = 1995
YEAR_VISUAL_BASIC_INVENTED = 1991


def main():
    """program entrypoint"""
    python = ProgrammingLanguage("Python", "Dynamic", True, YEAR_PYTHON_INVENTED)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, YEAR_RUBY_INVENTED)
    visual_basic = ProgrammingLanguage(
        "Visual Basic", "Static", False, YEAR_VISUAL_BASIC_INVENTED
    )
    print(python)
    print("The dynamically typed languages are:")
    programming_languages = [python, ruby, visual_basic]
    for language in programming_languages:
        if language.is_dynamic():
            print(language.name)


main()
