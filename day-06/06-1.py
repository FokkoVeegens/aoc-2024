def read_map(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file]

def find_guard_position_and_direction(map_data):
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    for i, row in enumerate(map_data):
        for j, cell in enumerate(row):
            if cell in directions:
                return (i, j), directions[cell]
    return None, None

def turn_right(direction):
    if direction == (-1, 0):  # Up
        return (0, 1)  # Right
    elif direction == (0, 1):  # Right
        return (1, 0)  # Down
    elif direction == (1, 0):  # Down
        return (0, -1)  # Left
    elif direction == (0, -1):  # Left
        return (-1, 0)  # Up

def is_within_bounds(position, map_data):
    x, y = position
    return 0 <= x < len(map_data) and 0 <= y < len(map_data[0])

def simulate_guard(map_data):
    position, direction = find_guard_position_and_direction(map_data)
    if position is None:
        return 0

    visited_positions = set()
    visited_positions.add(position)

    while True:
        next_position = (position[0] + direction[0], position[1] + direction[1])
        if not is_within_bounds(next_position, map_data):
            break
        if map_data[next_position[0]][next_position[1]] == '#':
            direction = turn_right(direction)
        else:
            position = next_position
            visited_positions.add(position)
            if not is_within_bounds(position, map_data):
                break

    return len(visited_positions)

if __name__ == "__main__":
    map_data = read_map('input.txt')
    result = simulate_guard(map_data)
    print(result)