
def find_x_pattern_outwards(grid, word):
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    #length to search from center of X. OBS: will only work for words with odd number of letters
    word_len_from_center = int((len(word)-1)*0.5)
    word_reverse = word[::-1]
    found_positions = []

    for r in range(rows):
        for c in range(cols):
            # Check if we can expand outwards from this position
            if (r - word_len_from_center >= 0 and r + word_len_from_center < rows and
                c - word_len_from_center >= 0 and c + word_len_from_center < cols):

                # Check diagonals outward from the center
                diag1 = "".join(grid[r + i][c + i] for i in range(-word_len_from_center, word_len_from_center+1))
                diag2 = "".join(grid[r + i][c - i] for i in range(-word_len_from_center, word_len_from_center+1))
                #print(diag1, diag2) # for debugging-purposes

                # Reverse the diagonals to check outward patterns
                diag1 = diag1[::-1]
                diag2 = diag2[::-1]

                # Verify if the diagonals match the word or its reverse
                if (diag1 == word or diag1 == word_reverse) and (diag2 == word or diag2 == word_reverse):
                    found_positions.append((r+1, c+1))

    return found_positions


# function to get a grid from the txt-file
def read_file_to_grid(filename):
    with open(filename, 'r') as file:
        grid = [list(line.strip()) for line in file]
    return grid

# Read the file and create the grid
filename = "2024/input-day4-24.txt"
grid = read_file_to_grid(filename)


# Word to search for
word = "MAS"

# Find the positions
positions = find_x_pattern_outwards(grid, word)

#initialize sum
sum_X_mas = 0

# Print results
if positions:
    for pos in positions:
        #print(f"Center: {pos}") # also for debugging-purposes
        sum_X_mas += 1
else:
    print(f"The word '{word}' (or its reverse) does not form an outward X pattern in the grid.")


print('MAS appears in an X-shape', sum_X_mas, 'times')