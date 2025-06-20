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
