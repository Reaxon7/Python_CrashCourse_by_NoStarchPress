#import the whole module. rename to p to avoid confusion
import pizza as p
p.make_pizza(16, 'pepperoni')

#import a specific function. as mp to avoid confusion or conflict
from pizza import make_pizza as mp
mp(12, 'pepperoni', 'mushrooms', 'extra cheese')

#import all functions
from pizza import *
