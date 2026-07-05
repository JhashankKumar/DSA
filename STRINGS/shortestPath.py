# finding shortest path on based on North South East West directions

"""
N -> North
S -> South
E -> East
W -> West

formula: shortest distance = \(d = \sqrt{x^2 + y^2}\)
"""

def shortestPath(path):
    # Initialize the coordinates
    x, y = 0, 0

    # Iterate through the path and update the coordinates
    for direction in path:
        if direction == 'N':
            y += 1
        elif direction == 'S':
            y -= 1
        elif direction == 'E':
            x += 1
        elif direction == 'W':
            x -= 1

    # Return shortest path using the coordinates
    return (x**2 + y**2)**0.5

dirctions = ["N", "S", "E", "W", "N", "E", "S", "W", "N", "E"]
shortest_distance = shortestPath(dirctions)
print(f"The shortest distance from the origin is: {shortest_distance}")