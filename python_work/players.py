#work with a specific group, a slice
players = ['charles', 'martina', 'micheal', 'florence', 'eli']
print(players[1:4])

print(players[:4])
print(players[2:])

#print last three players
print(players[-3:])

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())