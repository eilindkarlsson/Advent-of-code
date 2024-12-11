from functools import cmp_to_key

#define function to read the ordering rules from the input
def read_ordering_rules(file_path):
    ordering_rules = []  # List to store tuples (a, b)
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()  # Remove surrounding whitespace
            if line == "":  # Stop at a blank line
                break
            # Split the line into two numbers using '|'
            a, b = map(int, line.split('|'))
            ordering_rules.append((a, b))  # Add as a tuple
    return ordering_rules

#define function that reads the updates from the input-list (i.e. the lines appearing after a blank line)
def read_updates(file_path):
    updates = []
    blank_found = False  # Flag to start collecting lines
    
    with open(file_path, 'r') as file:
        for line in file:
            if not blank_found:
                # Check for the blank line
                if line.strip() == "":
                    blank_found = True
                continue  # Skip lines before the blank line
            # Convert line into a tuple by splitting it then append it
            line_list = list(map(int, line.split(",")))
            updates.append(line_list)   
    return updates

#function to get the middle number of the list numbers
def get_middle_number(numbers):
    if not numbers:
        raise ValueError("The list is empty.")  # Handle empty lists
    middle_index = len(numbers) // 2
    return numbers[middle_index]


# Step 1: Read off partial ordering rules from the input-file
file_path = "2024/input-day5-24.txt"
rules_list = read_ordering_rules(file_path)
#print(rules_list)

#Step 2: Read off list of (safe and unsafe) updates from the input-file
updates = read_updates(file_path)
#print(updates)

# Step 2: Define custom comparator
def custom_comparator(a, b):
    if (a, b) in rules_list:
        return -1
    if (b, a) in rules_list:
        return 1
    return 0

# Step 3: Sort the lists
def sorted_updates(updates):
    sorted_all = []  # To store all sorted lists
    for lst in updates:
        sorted_lst = sorted(lst, key=cmp_to_key(custom_comparator))
        sorted_all.append(sorted_lst) 
    
    return sorted_all


sorted_updates = sorted_updates(updates)

#printing the updates and sorted version for debugging
#print('The original updates are', updates)
#print('The sorted updates are', sorted_updates)

#initialize the sum of middle numbers
#sum_mid_page = 0 # used for part 1
sum_mid_page_unsafe = 0

for lst,lst_sorted in zip(updates, sorted_updates): 
    if lst==lst_sorted: 
        None
        #print('The update is safe')
        #sum_mid_page += get_middle_number(lst) # used for solving part 1
    else: 
        sum_mid_page_unsafe += get_middle_number(lst_sorted)
        #print('The update is not safe')


#print the answer
print('The sum of the middle pages of the safe reports is', sum_mid_page_unsafe)