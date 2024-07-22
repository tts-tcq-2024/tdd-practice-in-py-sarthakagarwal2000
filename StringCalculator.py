import re

def remove_delimiters(input_string):
    delimiters = [",", "\n"]
    if input_string.startswith("//"):
        parts = input_string.split("\n", 1)
        custom_delimiter = parts[0][2:]
        delimiters.append(custom_delimiter)
        input_string = parts[1]
    
    for delimiter in delimiters:
        input_string = input_string.replace(delimiter, ',')
    
    return input_string

def add(numbers):
    if not numbers:
        return 0

    def parse_numbers(num_str):
        num_list = remove_delimiters(num_str).split(',')
        return [int(num) for num in num_list if num]

def validate_numbers(nums):
    # Separate negative numbers and sum of valid numbers in one pass
    total = 0
    negatives = []

    for n in nums:
        if n < 0:
            negatives.append(n)
        elif n <= 1000:
            total += n

    return total, negatives


    nums = parse_numbers(numbers)
    total, negatives = validate_numbers(nums)

    if negatives:
        raise ValueError(f"Negative numbers not allowed: {negatives}")

    return total
