motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)

motorcycles.insert(0, 'benz')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

popped_motorcycle = motorcycles.pop(1)
print(motorcycles)
print(popped_motorcycle)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)