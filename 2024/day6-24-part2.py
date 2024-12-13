
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
#                grid[row_idx][col_idx] = 'X'
    return start_pos  

## Modify function that captures the guards movements to capture loops
#The 4 directions the guard can walk: up, right, down, left
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # (row_delta, col_delta)

def detect_loop(grid, start_row, start_col):
    visited_states = set()

    row, col = start_row, start_col
    direction_idx = 0  # Start facing up

    while True:
        current_state = (row, col, direction_idx)
        if current_state in visited_states:
            return True  # Loop detected
        visited_states.add(current_state)

        # Compute the next position
        next_row = row + directions[direction_idx][0]
        next_col = col + directions[direction_idx][1]

        # Check boundaries
        if next_row < 0 or next_row >= len(grid) or next_col < 0 or next_col >= len(grid[0]):
            return False  # No loop, went out of bounds

        # Handle navigation based on the grid
        symbol_ahead = grid[next_row][next_col]
        if symbol_ahead in {'#', 'O'}:  # Turn right at an obstacle
            direction_idx = (direction_idx + 1) % 4
        else:  # Move forward
            row, col = next_row, next_col


def test_grid_for_loops(grid, start_row, start_col):
    """Replace each '.' in the grid with 'O' and check for loops."""
    loop_count = 0  # Counter for cells that cause loops

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '.':  # Only replace empty cells
                # Temporarily replace the cell with 'O'
                original_value = grid[row][col]
                grid[row][col] = 'O'
                #print(grid) # for debugging
                # Check for loops
                loop_detected = detect_loop(grid, start_row, start_col)
                if loop_detected == True:
                    loop_count += 1  # Increment loop counter
                    print(f"Replacing cell ({row}, {col}) with 'O' causes a loop.")

                # Restore the original cell value
                grid[row][col] = original_value

    print(f"Total number of cells that cause a loop: {loop_count}")
    return loop_count


## start of actual code
# first use predefine function to read txt-file into a grid
filename = '2024/input_day6_24.txt'
grid = read_file_to_grid(filename)

#use predefined function to find starting position
start_pos = find_start_pos(grid)
#print(grid)

#run function that tests the grid for loops
test_grid_for_loops(grid, start_pos[0], start_pos[1])