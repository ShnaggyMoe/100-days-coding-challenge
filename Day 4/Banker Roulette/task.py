import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

random_num = random.randint(0 , 4)
# first method
# if random_num == 0:
#     print("Alice")
# elif random_num == 1:
#     print("Bob")
# elif random_num == 2:
#     print("Charlie")
# elif random_num == 3:
#     print("David")
# elif random_num == 4:
#     print("Emanuel")

#second method
# print(friends[random_num])

#third method
chosen_friend = random.choice(friends)
print(chosen_friend)