import re

def extract_delimiters(input_string):
    if input_string.startswith("//"):
        delimiter_part = input_string.split("\n", 1)[0][2:]
        custom_delimiters = re.findall(r'\[(.*?)\]', delimiter_part) or [delimiter_part]
        return [",", ";", "\n"] + custom_delimiters, input_string.split("\n", 1)[1]
    return [",", ";", "\n"], input_string

def replace_delimiters(input_string, delimiters):
    for delimiter in delimiters:
        input_string = input_string.replace(delimiter, ',')
    return input_string

def parse_numbers(number_string):
    return [int(num) for num in number_string.split(',') if num]

def check_for_negatives(nums):
    negatives = [num for num in nums if num < 0]
    if negatives:
        raise ValueError(f"Negative numbers not allowed: {', '.join(map(str, negatives))}")

def add(numbers):
    if not numbers:
        return 0

    delimiters, number_string = extract_delimiters(numbers)
    cleaned_string = replace_delimiters(number_string, delimiters)
    nums = parse_numbers(cleaned_string)
    
    check_for_negatives(nums)

    return sum(num for num in nums if 0 <= num <= 1000)
