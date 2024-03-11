animal = str(input("enter mammal:"))
carnivores = {"Lion", "Tiger", "Leopard", "dog", "Wolf"}
herbivores = {"Elephant", "Giraffe", "Deer", "goat", "dog", "Horse"}
omnivores = {"humans", "chimpanzee", "racoon", "cat"}

if animal in carnivores and animal in herbivores:
    print(animal, "is an omnivore!")
elif animal in carnivores:
    print(animal, "is a carnivore.")
elif animal in herbivores:
    print(animal, "is a herbivore.")
elif animal in omnivores:
    print(animal, "is an omnivore")
else:
    print(animal, "is not an animal.")
