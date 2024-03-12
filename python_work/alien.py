alien_0 = {'color': 'green', 'point': 5}

print(alien_0['color'])
print(alien_0['point'])

print(f"You just earned {alien_0['point']} points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print(f"This alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"This alien is now {alien_0['color']}.")


alien_0['speed'] = 'medium'
#removing point
#del alien_0['point']
print(alien_0)
print(f"Original position: {alien_0['x_position']}")

#Move the alien to the right
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #This must be a fast alien.
    x_increment = 3

alien_0['x_position'] += x_increment

print(f"New position: {alien_0['x_position']}")

point_value = alien_0.get('point', 'No point value assigned')
print(point_value)