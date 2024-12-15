#used to combine + and * into all the possible combinations for an equation
from itertools import product

#function that reads the file line by line and outputs a list (of lists)
def read_file(file_path):
    number_tuple = []
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line at the colon
            key_part, values_part = line.split(':')
            
            # Convert key and values to integers
            key = int(key_part.strip())
            values = [int(value) for value in values_part.split()]
            
            # Create a tuple with the key and values
            number_tuple.append([key, *values])
    return number_tuple

#function that checks if the target-number can be obtained by applying + and * in a suitable way between the numbers
# for part 1 just take away anything related to "concat" in this function
def has_solution(target, numbers):
    n = len(numbers)
    if n < 2:
        raise ValueError("At least two numbers are required.")
    # Generate all combinations of operators (+, *) for n-1 positions
    operators = ['+', '*', 'concat']
    for ops in product(operators, repeat=n-1):
        # Evaluate left-to-right dynamically without creating an overly long equation string
        current_value = numbers[0]
        operations = [str(numbers[0])]  # To store operations as a list for a concise string
        for i in range(1, n):
            if ops[i-1] == '+':
                current_value += numbers[i]
            elif ops[i-1] == '*':
                current_value *= numbers[i]
            elif ops[i-1] == 'concat':
                current_value = int(str(current_value) + str(numbers[i]))
            operations.append(f"{ops[i-1]} {numbers[i]}")  # Store the operation

        # Check if the current value matches the target
        if current_value == target:
            # Print the solution in a concise mathematical form
            print(f"Solution found: {' '.join(operations)} = {target}")
            return True
    

#read the file into a tuple or tuples
file_path = '2024/input_day7_24.txt'
file = read_file(file_path)
#print(file)


# initialize the total calibration result
total_cal_result = 0

# run through the file-input and apply has_solution to each entry & add true equations to the 
for tuple in file:
    target = tuple[0]
    numbers = tuple[1:]
    if has_solution(target, numbers):
        total_cal_result += target
        #print('the total calibration-result is now', total_cal_result)
    #else:
        #print(f"the tuple {tuple} does not contribute to the calibration result")

print('The total calibration result is', total_cal_result)