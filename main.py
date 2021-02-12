names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

import random

random_position = random.randrange(0, len(names))
picked_name = names[random_position]

print(f"The person who pays for the meal is {picked_name}.")