import pprint
import math

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
    def __str__(self):
        return f"({self.x},{self.y})"

def distFormula(x_1, x_0, y_1, y_0):
    dx = x_1 - x_0
    dy = y_1 - y_0
    dist = math.sqrt(dx*dx + dy*dy)
    return dist

def travel(p: Point, x_steps, y_steps, back_steps):
    cur = Point()  # starting at 0,0
    memory = []    # collection of all previous steps
    i = 0

    while True:
        i += 1
        cur.x += x_steps
        cur.y += y_steps

        if i % 3 == 0:
            cur.x -= back_steps
            cur.y -= back_steps

        current = distFormula(p.x, cur.x, p.y, cur.y)
        memory.append((current, cur.x, cur.y, i))

        if len(memory) >= 3:
            # we can check whether we are definitively moving away
            # by checking that we moved further away twice in a row.
            # If that is the case, we determine the closest point from our
            # memory and return it.
            prev = memory[i-2][0]
            prev_prev = memory[i-3][0]
            
            if current > prev and prev > prev_prev:
                # pprint.pprint(memory)
                min_val = sorted(memory, key=lambda m: m[0])[0]
                # pprint.pprint(f"Min: {min_val}")
                # print()
                return min_val


def main():
    p = Point()
    inputs = [
        (4,5,2,3,1),
        (6,6,1,1,1),
        (5,8,2,3,1)
    ]

    for ins in inputs:
        p.x = ins[0]
        p.y = ins[1]
        x_steps = ins[2]
        y_steps = ins[3]
        back_steps = ins[4]

        result = Point()
        min_dist, result.x, result.y, min_iteration = travel(p, x_steps, y_steps, back_steps)
        print(f"Point P: ({p.x},{p.y})")
        print(f"Arrival point: ({result.x},{result.y})")
        print(f"Distance between P and arrival: {min_dist:.6f}")
        print(f"Number of iterations: {min_iteration}")
        print("--------------------------------------------------")

if __name__ == "__main__":
    main()

# Solutions should be:

# Point P: (4,5)
# Arrival point: (4,6)
# Distance between P and arrival: 1.000000
# Number of iterations: 2

# Point P: (6,6)
# Arrival point: (6,6)
# Distance between P and arrival: 0.000000
# Number of iterations: 8

# Point P: (5,8)
# Arrival point: (5,8)
# Distance between P and arrival: 0.000000
# Number of iterations: 3