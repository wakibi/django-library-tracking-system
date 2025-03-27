import random

# Create a list of 10 random numbers between 1 and 20.
# Filter Numbers Below 10 (List Comprehension)
# Filter Numbers Below 10 (Using filter)

rand_list = random.randint(1, 20) # Assumption - Only integers and 1 and 20 are inclusive

# Using list comprehension
list_comprehension_below_10 = [ i for i in rand_list if i < 10]

# Using filter
list_comprehension_below_10 = filter(lambda i: i < 10, rand_list)