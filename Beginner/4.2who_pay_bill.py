import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

name_len=len(names)

selected_person=random.randint(0,name_len-1)

print(f"{names[selected_person]} is going to buy the meal today!")

# selected_person = random.choice(names)

# print(f"{selected_person} is going to buy the meal today!")
