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

# question 3
with open("numbers.txt") as in_file:
    sum = 0
    # to keep the integrity of DRY rules is not as intuitive as it seems
    for line, _ in zip(in_file, range(2)):
        sum += int(line)
    print(sum)

