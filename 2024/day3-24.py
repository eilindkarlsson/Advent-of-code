# import re to search for regular expressions
import re

def modify_input(input):
    return "do()" + input


# Open the file and read its contents into a string
with open("2024/input-day3-24.txt", "r") as file:
    file_contents = file.read()

# add do() to the start of the file to capture first mul() (unless there's a don't() appearing)
modified_file = modify_input(file_contents)

# Define the regex-pattern for either do(), don't() OR mul(x,y)
pattern = r"(do\(\)|don't\(\)|mul\(\d+,\d+\))"


# Find all matches
matches = re.findall(pattern, modified_file)
#print(matches)

# Initialize the sum
total_sum = 0

# Process each match - used for part 1
# for x, y in matches:
#     product = int(x) * int(y)  # Convert to integers and multiply
#     total_sum += product       # Add the product to the total sum

## modified version for part 2

mul_pattern = r"mul\((\d+),(\d+)\)"

# Initialize a list to store results
results = []

# Initialize variables
processing = False  # Indicates if we are in a 'do()' block

# # Iterate through the list of strings
for entry in matches:
    if entry == 'do()':
        # Start a new processing block
        if processing:
            # Append the current product of the previous block
            results.append(current_product)
        processing = True
        current_product = 0  # Reset the product for the new block
    elif entry == "don't()":
        # End the current processing block
        if processing:
            results.append(current_product)
        processing = False
        current_product = None  # Reset the product outside any block
    elif processing:
        # Process mul(x, y) if inside a 'do()' block
        match = re.match(mul_pattern, entry)
        if match:
            x, y = map(int, match.groups())  # Extract x and y as integers
            current_product += x * y

# Handle the case where the last block doesn't end with "don't()"
if processing and current_product is not None:
    results.append(current_product)


# Display the total sum
print("The total sum of the products is:", sum(results))


