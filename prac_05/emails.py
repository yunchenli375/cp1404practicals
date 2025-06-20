"""
Emails
Estimate: 10 minutes
Actual:   11 minutes
"""


def main():
    """program entrypoint"""
    emails_to_names = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        response = input(f"Is your name {name}? (Y/n) ")
        if response.lower() == "y" or response == "":
            emails_to_names[email] = name
        else:
            name = input("Name: ")
            emails_to_names[email] = name
        email = input("Email: ")
    print()

    for email, name in emails_to_names.items():
        print(f"{name} ({email})")


def extract_name(email):
    """return the name from an email address"""
    return " ".join(email[: email.find("@")].split(".")).title()


main()
