
## function that checks if a report is safe by increasing numbers (part 1)
def safe_increasing(numbers):
    for i in range(len(numbers)-1):  # Loop until the second-to-last index
        if not ((numbers[i] < numbers[i+1]) and (numbers[i+1] - numbers[i]) <= 3):
            #print(numbers[i], numbers[i+1]) # for debugging, checks when condition fails
            return False  # If any pair doesn't meet the condition, the report is not safe
    return True  # If all pairs meet the condition, the report is safe

## function that checks if a report is safe by decreasing numbers (part 1)
def safe_decreasing(numbers):
    for i in range(len(numbers)-1):  
       # print(numbers[i], numbers[i+1]) # for debugging, checks when condition fails
        if not ((numbers[i] > numbers[i+1]) and (numbers[i]-numbers[i+1]) <= 3):
            return False  # If any pair doesn't meet the condition, the report is not safe
    return True  # If all pairs meet the condition, the report is safe

## function for part 2 - checks for safe-increasing or decreasing + the dampened condition where the report can still be safe if it is safe when one number is omitted
def safe_dampened(numbers):
    # Check each sublist formed by removing one number
    for i in range(len(numbers)):
        modified_list = numbers[:i] + numbers[i + 1:]  # Remove the i-th number
        if safe_increasing(modified_list) or safe_decreasing(modified_list):
            return True
    # If no valid sublist satisfies the condition
    return False



# Initialize a list to store the lines
lines_as_lists = []

# Open the file and read each line
with open("2024/input-day2-24.txt", "r") as file:
    for line in file:
        # Split the line into elements and convert them to integers (if numeric)
        line_list = list(map(int, line.split()))
        lines_as_lists.append(line_list)

# Initialize the number of safe reports as 0
safe_reports = 0

# Check if the list is non-empty
if lines_as_lists:
    # Now check each report from the input file for either safe increasing or decreasing:
    for report in lines_as_lists:
        if safe_increasing(report) or safe_decreasing(report) or safe_dampened(report):
            safe_reports += 1
            print(report)

print('The number of safe reports is:', safe_reports)


