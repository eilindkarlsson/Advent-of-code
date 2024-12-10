# package for regular expressions, used to search for digits
import re


#For the second part, matching spelled out digits with their number
digits_map = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}
# List of numbers sorted by length (longest first for greedy matching)
sorted_words = sorted(digits_map.keys(), key=len, reverse=True)

# Function to replace spelled-out numbers with digits
def replace_spelled_digits(input_string):
    result = ""
    i = 0
    while i < len(input_string):
        match_found = False
        # Check if the current character is a digit
        if input_string[i].isdigit():
            result += input_string[i]
            i += 1
            continue
        # Check each number word in sorted order
        for word in sorted_words:
            if input_string[i:i + len(word)].lower() == word:
                # Append the corresponding digit
                result += digits_map[word]
                # Advance the pointer by the length of the matched word minus 1 = the last letter
                i += len(word)-1
                match_found = True
                break
        if not match_found:
            # If no match, just move forward
            i += 1
    return result

# intermediate test to check if the new function works as intended
#input_string_test = "one3five"
#output_string_test= replace_spelled_digits(input_string_test)
#print(output_string_test)


# Open the file in read mode
with open('2023/input-day1-23.txt', 'r') as file:
    # Read lines into a list of strings
    lines = file.readlines()

# Optionally, strip newline characters from each line
lines = [line.strip() for line in lines]

#initialize an empty list for first and last digits and 0 for the total sum
first_and_last_digits = []
total_sum = 0

# Extract the first and last digit from each line
#test lines to check how the code works
lines_test = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]

for line in lines:
    print(line)
    line = replace_spelled_digits(line)
    matches = re.findall(r'\d', line)  # Find all single digits in the line
    if matches:
        # Concatenate the first and last digit
        concat_digits = matches[0] + matches[-1]
        print(concat_digits)
        # Convert the concatenated digits to an integer and add to the sum
        total_sum += int(concat_digits)
     #   first_and_last_digits.append(concat_digits)
    else:
        first_and_last_digits.append(None)  # Handle lines without digits


print(total_sum)










