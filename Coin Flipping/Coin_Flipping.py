# Coin Flipping
#
# The program that flipping a single coin that how many times the user decides.
#

from random import *

outcomes = []

flips = int(input("Number of coin flipping? "))

while flips > 0:
    result = randint(1,2)
    outcomes.append(result)
    flips -= 1

print ("Heads: %d" % outcomes.count(1))
print ("Tails: %d" % outcomes.count(2))