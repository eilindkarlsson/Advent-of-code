from day6_24 import read_file_to_grid, find_start_pos 

#modify previous function to also detect loops
def navigate_grid_detect_loop(grid, start_row, start_col):
    # Directions: [Up, Right, Down, Left]
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    row, col = start_row, start_col
    direction_idx = 0  # Start facing up (index 0 in DIRECTIONS)

    # Set to track visited states (row, col, direction_idx)
    visited_states = set()
    max_steps = 10
    step_count = 0

    while True:
        # # Break if maximum steps are exceeded
        # if step_count >= max_steps:
        #     print("Maximum steps reached. Exiting to prevent infinite loop.")
        #     break
        # step_count += 1
        # Check if out of bounds
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            print("Out of bounds!")
            break

        # # Record the current state
        # current_state = (row, col, direction_idx)
        # if current_state in visited_states:
        #     print("Detected a loop!")
        #     break
        # visited_states.add(current_state)

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
        elif symbol_ahead in {'#', 'O'}:  # Turn 90° to the right
            direction_idx = (direction_idx + 1) % 4
        else:
            print("Encountered unknown symbol, stopping.")
            break

    print(f"Ended at position ({row}, {col})")

file_path = '2024/input_day6_24.txt'
grid = read_file_to_grid(file_path)
#print(grid)

start_pos = find_start_pos(grid)
#print(grid)

#use function to simulate the guards movements
navigate_grid_detect_loop(grid, start_pos[0], start_pos[1])



