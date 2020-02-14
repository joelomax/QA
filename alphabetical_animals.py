'''
Create a new Python file and create a program that outputs animals that come first alphabetically.

The program should:

Ask user for two animals, stored in two variables
Calculates which animal is first alphabetically
Outputs the name of that animal
'''

animal1 = input str("first animal: ")
animal2 = input str("second animal: ")

animal_list= [animal1, animal2]

print sorted(animal_list)
