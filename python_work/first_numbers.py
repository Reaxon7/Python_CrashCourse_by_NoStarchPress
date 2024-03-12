for value in range(1, 5):
    print(value)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

#This can be summarized with one line of code (aka list comprehension)
squares = [value**2 for value in range(1, 11)]

print(squares)

print(sum(squares))