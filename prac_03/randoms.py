import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# Random number between 5 and 20, inclusive.

# What was the smallest number you could have seen, what was the largest?
# 6 and 19

# What did you see on line 2?
# Random odd number between 3 and 9, inclusive.

# What was the smallest number you could have seen, what was the largest?
# 3 and 9

# Could line 2 have produced a 4?
# No, because the range is odd numbers only.

# What did you see on line 3?
# Random floating point number between 2.5 and 5.5.

# What was the smallest number you could have seen, what was the largest?
# 3.1552587326880097 and 5.244601983663225

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.

import random

random_number = random.randint(1, 100)
print(f"{random_number} ")
