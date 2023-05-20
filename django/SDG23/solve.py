######################################################################################
############################## Question 1: ###########################################
#### Write a function called getMaxSum that takes a list of integers as input ########
#### Return: the maximum sum of any contiguous subarray of the given array. If the
#### array is empty or contains only negative integers, the function should return 0.
######################################################################################


# changed the function parameter so as not to override the list type
def getMaxSum(array: list):
    if not array:
        return 0

    if all(number < 0 for number in array):
        return 0

    current_sum = 0
    max_sum = 0

    for number in array:
        local_sum = current_sum + number

        if number > local_sum:
            current_sum = number
        else:
            current_sum = local_sum

        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum


######################################################################################
############################## Question 2: ###########################################
#### Write a function called uniqueChars that takes a string as input ################
#### Return: a new string containing only the unique characters in the input string,
#### in the order that they first appear. If the input string is empty or contains
#### only whitespaces, the function should return an empty string.
######################################################################################


# changed the function parameter so as not to override the str type
def uniqueChars(string: str):
    string = string.strip().lower()

    if not string:
        return ""

    char_list = []

    for index in range(0, len(string)):
        char = string[index]

        if char not in char_list:
            char_list.append(char)

    final_string = "".join(char_list).strip()

    return final_string
