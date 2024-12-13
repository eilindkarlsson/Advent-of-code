
#(reuse) function (from day 4) to get a grid from the txt-file
def read_file_to_grid(filename):
    with open(filename, 'r') as file:
        grid = [list(line.strip()) for line in file]
    return grid

#define function that finds the starting position and writes "." over it
def find_start_pos(grid):
    start_pos = []
    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            if cell == "^":
                print('The starting position is:',(row_idx, col_idx))
                start_pos = [row_idx, col_idx]
                grid[row_idx][col_idx] = 'X'
    return start_pos   


## Define function that corresponds to the guard navigating through the lab=the grid
#The 4 directions the guard can walk: up, right, down, left
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # (row_delta, col_delta)

def navigate_grid(grid, start_row, start_col):
    row, col = start_row, start_col
    direction_idx = 0  # Start facing up (index 0 in DIRECTIONS)

    # Iterate through movements
    while True:
        # Check if out of bounds
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            print("Out of bounds!")
            break

        # Compute the next position
        next_row = row + directions[direction_idx][0]
        next_col = col + directions[direction_idx][1]

        # Check if the next position is within bounds
        if next_row < 0 or next_row >= len(grid) or next_col < 0 or next_col >= len(grid[0]):
            print("Out of bounds!")
            break

        # Get the symbol ahead
        symbol_ahead = grid[next_row][next_col]
        print(f"At position ({row}, {col}) the symbol ahead is {symbol_ahead}")

        if symbol_ahead in {'.', 'X', '^'}:  # Move straight
            row, col = next_row, next_col
            grid[row][col] = "X"  # Mark the position
        elif symbol_ahead == '#':  # Turn 90° to the right
            direction_idx = (direction_idx + 1) % 4
        else:
            print("Encountered unknown symbol, stopping.")
            break

    print(f"Ended at position ({row}, {col})")

#define function to count the number of X's in the end
def count_unique_pos(grid):
    total_count = 0
    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            if cell == "X":
                total_count +=1
    return total_count  


## start of actual code
# first use predefine function to read txt-file into a grid
filename = '2024/input_day6_24.txt'
grid = read_file_to_grid(filename)

#use predefined function to find starting position
start_pos = find_start_pos(grid)
#print(grid)

#use function to simulate the guards movements
navigate_grid(grid, start_pos[0], start_pos[1])
#print(grid)

#finally use function to count the number of X's = distinct positions of the guard
count=count_unique_pos(grid)
print('The number of distinct positions are', count)