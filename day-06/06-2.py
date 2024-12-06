import time

DIRECTION_KEYS = {
    '^': 0,
    '>': 1,
    'v': 2,
    '<': 3
}

DIRECTION_SHIFTS = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]

TURN = [1, 2, 3, 0]  # Right turn for each direction

def load_grid(file_path):
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file.readlines()]
    return grid

def locate_guard(grid):
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell in DIRECTION_KEYS:
                guard_position = (r, c)
                guard_direction = DIRECTION_KEYS[cell]
                grid[r][c] = '.'
                return guard_position, guard_direction
    raise ValueError("Guard not found in the grid.")

def find_obstruction_positions(grid, guard_position):
    possible_positions = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '.' and (r, c) != guard_position:
                possible_positions.append((r, c))
    return possible_positions

def count_loop_inducing_obstructions(grid):
    guard_position, guard_direction = locate_guard(grid)
    possible_obstructions = find_obstruction_positions(grid, guard_position)

    loop_count = 0
    for obstruction in possible_obstructions:
        grid[obstruction[0]][obstruction[1]] = '#'

        r, c = guard_position
        direction = guard_direction
        seen_states = set()

        while True:
            current_state = (r, c, direction)
            if current_state in seen_states:
                loop_count += 1
                break
            seen_states.add(current_state)

            dr, dc = DIRECTION_SHIFTS[direction]
            new_r, new_c = r + dr, c + dc

            if new_r < 0 or new_r >= len(grid) or new_c < 0 or new_c >= len(grid[0]):
                break

            if grid[new_r][new_c] == '#':
                direction = TURN[direction]
            else:
                r, c = new_r, new_c

        grid[obstruction[0]][obstruction[1]] = '.'

    return loop_count

def main():
    file_path = 'input.txt'
    grid = load_grid(file_path)
    result = count_loop_inducing_obstructions(grid)
    print(result)

if __name__ == "__main__":
    main()