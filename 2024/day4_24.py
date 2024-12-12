
#define a function to search a grid in different directions for a word = XMAS in this task
def search_word(grid, word):
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    directions = [
        (0, 1),   # Horizontal right
        (0, -1),  # Horizontal left
        (1, 0),   # Vertical down
        (-1, 0),  # Vertical up
        (1, 1),   # Diagonal down-right
        (-1, -1), # Diagonal up-left
        (1, -1),  # Diagonal down-left
        (-1, 1)   # Diagonal up-right
    ]

# check that we do not exceed the boundaries of the text 
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

#the actual search-function
    def search_from(x, y, dx, dy):
        """Search for the word starting at (x, y) in direction (dx, dy)."""
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

    # Search for the word from every position in the grid
    found_positions = []
    for r in range(rows):
        for c in range(cols):
            for dx, dy in directions:
                if search_from(r, c, dx, dy):
                    found_positions.append(((r, c), (dx, dy)))

    return found_positions

# function to get a grid from the txt-file
def read_file_to_grid(filename):
    with open(filename, 'r') as file:
        grid = [list(line.strip()) for line in file]
    return grid

# Read the file and create the grid
filename = "2024/input_day4_24.txt"
grid = read_file_to_grid(filename)

# Print the grid (for debugging purposes)
#for row in grid:
#    print(row)

# Word to search for
word = "XMAS"

# Find the word in the grid
positions = search_word(grid, word)

#initialize 0 as how many times the word is found
sum_xmas = 0

# Print the results
if positions:
    for pos, direction in positions:
        #print(f"Start: {pos}, Direction: {direction}") # for debugging the code
        sum_xmas += 1
else:
    print(f"The word '{word}' was not found.")

print('The word XMAS was found', sum_xmas, 'times')