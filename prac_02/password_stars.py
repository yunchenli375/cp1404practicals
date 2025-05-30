import getpass

true_password = "151515"

def main():
    password = get_password()
    if password == true_password:
        print("You are login Successful")
    else:
        print("You are login Failure")

def get_password():
    password = getpass.getpass("Enter your password: ")
    return password

if __name__ == "__main__":
    main()
