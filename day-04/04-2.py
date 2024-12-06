def read_grid(filename):
    with open(filename, 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    return grid

def find_x_mas(grid, print_patterns=False):
    count = 0
    rows = len(grid)
    cols = len(grid[0])
    
    # Find all occurrences of 'A' and their positions
    positions_of_a = [(i, j) for i in range(rows) for j in range(cols) if grid[i][j] == 'A']
    
    for x, y in positions_of_a:
        # Check the four diagonal positions
        diagonals = [
            (x-1, y-1), (x+1, y-1),
            (x-1, y+1), (x+1, y+1)
        ]
        
        # Filter out invalid positions
        valid_diagonals = [(i, j) for i, j in diagonals if 0 <= i < rows and 0 <= j < cols]
        
        # Ensure all four diagonal positions are valid
        if len(valid_diagonals) != 4:
            continue
        
        # Check if each pair of diagonal positions contains both 'M' and 'S'
        top_left = grid[x-1][y-1]
        top_right = grid[x-1][y+1]
        bottom_left = grid[x+1][y-1]
        bottom_right = grid[x+1][y+1]
        
        if (top_left in 'MS' and top_right in 'MS' and
            bottom_left in 'MS' and bottom_right in 'MS' and
            {top_left, bottom_right} == {'M', 'S'} and
            {top_right, bottom_left} == {'M', 'S'}):
            count += 1
            # Log the pattern found if print_patterns is True
            if print_patterns:
                pattern = [['.' for _ in range(cols)] for _ in range(rows)]
                pattern[x][y] = 'A'
                for i, j in valid_diagonals:
                    pattern[i][j] = grid[i][j]
                print(f"Pattern found at A({x},{y}):")
                for row in pattern:
                    print(''.join(row))
                print()
    
    return count

grid = read_grid('input.txt')
x_mas_count = find_x_mas(grid, print_patterns=False)
print(f"Total X-MAS patterns found: {x_mas_count}")