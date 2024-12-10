## define a function that compares the length of the lists, then makes a list of the absolute differences and sums them up to give total_distance
def total_distance(sorted_list1, sorted_list2): 
    if len(sorted_list1) == len(sorted_list2):
        absolute_differences = []
        for i in range(len(sorted_list1)):
            absolute_differences.append(abs(sorted_list1[i] - sorted_list2[i]))
        total_dist = sum(absolute_differences)
        return(total_dist) 
    else:
        print("The lists must be of the same length.")
        return None

#creating function for the similarty-score
def sim_score(list1, list2): 
    sim_score=0
    for number in list1:
        count_number = list2.count(number)
        sim_score += number*count_number
    return(sim_score)


#Test-case to use when building the code/fixing errors
test_list1=[3,4,2,1,3,3]
test_list2=[4,3,5,3,9,3]


## create two lists from the input txt-file + first initialize them to be empty
list1 = []
list2 = []

# Open the file and read line by line
with open("2024/input-day1-24.txt", "r") as file:
    for line in file:
        # Strip leading/trailing whitespaces and check the content of each line
        line = line.strip()  # Remove any extra spaces/newlines from the start and end of the line
        num1, num2 = map(int, line.split())  # Split and convert to integers
        list1.append(num1)
        list2.append(num2)


#use the in-built sorted-function to create new lists which are sorted
sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)

#print the answer to the first part using total_distance function
print('The total distance is:', total_distance(sorted_list1, sorted_list2))

# use the sim_score function to print the answer to the second part
print('The similarity-score is:', sim_score(list1, list2))



