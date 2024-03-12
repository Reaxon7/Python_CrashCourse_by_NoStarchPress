pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

#Summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")

#arbitrary number of arguments *. This produce a tuple with toppings. Must be placed last
def make_pizza(size, *toppings):
    """Print the list of topping that have been requested"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
