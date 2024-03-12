pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

#Default Arguments
def describe_pet(animal_type='dog', pet_name=None):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

#Positional Arguments
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

#Keyword Arguments
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry')