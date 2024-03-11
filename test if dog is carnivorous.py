carnivores = {"Lion", "Tiger", "Leopard", "Wolf"}
herbivores = {"Elephant", "Giraffe",  "Deer","goat", "Horse"}

animal = "goat"
for animal in animal:
    if animal in carnivores and animal in herbivores:
        print(animal, "is both a carnivore and herbivore!")
    elif animal in carnivores:
        print(animal, "is a carnivore.")
    elif animal in herbivores:
        print(animal, "is a herbivore.")
    else:
         print(animal, "is neither a carnivore nor herbivore.")
