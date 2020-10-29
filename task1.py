#!python3

"""
Create a class that will store a database for a veterinarian.
Your class will need the following properties:

animal (dog, cat, fish, bird, turtle, etc)
breed
name (the pet's name)
owner (the owner's name)
birthdate (of the pet, expressed as yyyy-mm-dd)

The constructor will need to ask for each of those values
for the database when the pet is instantiated

Methods:
display() - should show the name of the pet and type followed by their breed and owner


Main block should have a menu that has the following options:
1. Enter a new pet
2. Retrieve a pet
3. Exit

If they choose to retrieve a pet,
display the following:
Enter pet's name:
and then go through the list, looking for the name of the pet.
If the pet is found, it should call the display() method from the object

Example output:
1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? cat
Breed? Domestic Long Hair
Name? Benjamin
Owner? Chris
Birthdate? 20015-10-01

1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? dog
Breed? Shih-tzu
Name? Buster
Owner? Christy
Birthdate? 2008-10-16

1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? cat
Breed? Domestic Long Hair
Name? Casey
Owner? Chris
Birthdate? 20015-10-01

1. Enter a new pet
2. Retrieve a pet
3. Exit
2

Which Pet? Buster

Buster dog
Shih-tzu is owned by Christy
(10 points) 
"""
pets = []
names = []

class pet:

    global pets
    global names

    def __init__(self):
        self.animal = input("Type of animal:\n").strip()
        self.breed = input("Breed\n").strip()
        n = input("Name:\n").strip()
        self.name = n
        names.append(n)
        self.owner = input("Owner:\n").strip()
        self.birth = input("Birthdate\n").strip()

    def __del__(self):
        pass

    def display(self):
        #print( self.name + " " + self.animal + "\n" + self.breed + " is owned by " + self.owner)
        print(self.name + "\n" + self.animal + "\n" + self.breed + "\n" + self.owner)

def main():
    global pets
    global names
    while True:
        x = input("1. Enter a new pet\n2. Retrieve a pet\n3. Exit\n").strip()
        if x == "1":
            pets.append(pet())
            #os.system("cls")
        elif x == "2":
            if len(pets) == 0:
                #os.system("cls")
                print("You have no pets!")
            else:
                #os.system("cls")
                #print(names)
                p = input("Enter pet's name\n").strip()
                #os.system("cls")
                if p in names:
                    pets[names.index(p)].display()
                else:
                    print("You don't have a pet named " + p + "!")
        elif x == "3":
            #os.system("cls")
            #print("Yeah get outta here loser")
            break
        else:
            #os.system("cls")
            pass

main()
