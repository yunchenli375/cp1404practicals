# question 1
out_file = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=out_file, end="")
out_file.close()

# question 2
in_file = open("name.txt", "r")
name = in_file.read()
print(f"Hi {name}!")
in_file.close()