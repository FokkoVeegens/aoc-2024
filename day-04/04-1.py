def read_input(file_name):
    with open(file_name, 'r') as file:
        return [line.strip() for line in file]

def search_word(grid, word):
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    count = 0

    def search_direction(x, y, dx, dy):
        for i in range(word_len):
            if not (0 <= x < rows and 0 <= y < cols) or grid[x][y] != word[i]:
                return 0
            x += dx
            y += dy
        return 1

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == word[0]:
                count += search_direction(i, j, 1, 0)  # down
                count += search_direction(i, j, -1, 0)  # up
                count += search_direction(i, j, 0, 1)  # right
                count += search_direction(i, j, 0, -1)  # left
                count += search_direction(i, j, 1, 1)  # down-right
                count += search_direction(i, j, 1, -1)  # down-left
                count += search_direction(i, j, -1, 1)  # up-right
                count += search_direction(i, j, -1, -1)  # up-left

    return count

def main():
    grid = read_input('input.txt')
    word = "XMAS"
    count = search_word(grid, word)
    print(f"The word '{word}' appears {count} times in the grid.")

if __name__ == "__main__":
    main()