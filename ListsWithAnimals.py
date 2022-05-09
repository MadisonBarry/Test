animals = ["Bird", "Fox", "Cat", "Rat", " Alligator", "Lizard"]

print(animals[5])
print(animals[0])
print(animals[1])
print(animals[-1])
print(animals[1:3])
print(animals[0:])

for counter in animals:
    print(counter)
    
animals.append("Giraffe")

moreAnimals = ["Monkey", "Owl", "Lion"]

animals.insert(4, "Snake")

animals.pop(3)

animals.remove("Snake")

del animals[2]

animals.extend(moreAnimals)