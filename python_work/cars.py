cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

#reserve sort
cars.sort(reverse=True)
print(cars)

#temporary list
print(sorted(cars))

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)

print(len(cars))

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

