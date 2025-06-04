# question 1
out_file = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=out_file, end="")
out_file.close()