from decimal import Decimal  # avoid float*100 offset error

# example of a greedy algorithm
def make_change(amount):
    change = []
    amount *= 100
    while amount >= 100:
        change.append(100)
        amount -= 100
    while amount >= 25:
        change.append(25)
        amount -= 25
    while amount >= 10:
        change.append(10)
        amount -= 10
    while amount >= 5:
        change.append(5)
        amount -= 5
    while amount > 0:
        change.append(1)
        amount -= 1
    return change

import sys
print(make_change(Decimal(sys.argv[1])))