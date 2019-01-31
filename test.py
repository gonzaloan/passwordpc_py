import random

random_numbers = []
for x in range(0,10):
    random_numbers.append(random.randint(0, 100))

print(random_numbers)

orderer_numbers = sorted(random_numbers)
print(orderer_numbers)