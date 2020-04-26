from operator import attrgetter

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.fraction = 1.0  # represents fraction of item

class Knapsack:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.items = []
    
    def add(self, item):
        self.items.append(item)

    def __str__(self):
        return ", ".join([f"[{i.weight} ${i.value}]" for i in self.items])


def knapsack01(knapsack, items):
    num_items = len(items)
    sorted_items = sorted(items, key=attrgetter("value"), reverse=True)
    remaining = knapsack.max_weight
    for item in sorted_items:
        if item.weight <= remaining:
            knapsack.add(item)
            remaining -= item.weight


def value_to_weight_ratio(item):
    # key function
    return item.value / item.weight

def fractional_knapsack(knapsack, items):
    num_items = len(items)
    # sort by value/weight ratio
    sorted_items = sorted(items, key=value_to_weight_ratio, reverse=True)
    # for i in sorted_items:
    #     print(f"[{i.weight} ${i.value}]", end=" ")
    # print()
    remaining = knapsack.max_weight
    for item in sorted_items:
        if item.weight <= remaining:
            knapsack.add(item)
            remaining -= item.weight
        else:
            fractional_item = Item(item.weight, item.value)
            fractional_item.fraction = remaining / item.weight
            knapsack.add(fractional_item)
            break


def test_knapsack_01():
    items = [
        # weight, value
        Item(6, 25),
        Item(8, 42),
        Item(12, 60),
        Item(18, 95),
        # Item(20, 100)
    ]
    ks = Knapsack(30)
    knapsack01(ks, items)
    print(ks)

def test_knapsack_fractional():
    items = [Item(40, 80), Item(12, 18), Item(8, 8)]
    ks = Knapsack(48)
    fractional_knapsack(ks, items)
    print(ks)


def main():
    # test_knapsack_01()
    test_knapsack_fractional()

if __name__ == "__main__":
    main()