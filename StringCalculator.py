import re

def extract_custom_delimiters(input_string):
    if input_string.startswith("//"):
        delimiter_part = input_string.split("\n", 1)[0][2:]
        return re.findall(r'\[(.*?)\]', delimiter_part) or [delimiter_part]
    return []

def get_default_delimiters():
    return [",", ";", "\n"]

def combine_delimiters(default_delimiters, custom_delimiters):
    return default_delimiters + custom_delimiters

def replace_delimiters(input_string, delimiters):
    for delimiter in delimiters:
        input_string = input_string.replace(delimiter, ',')
    return input_string

def extract_number_string(input_string):
    if input_string.startswith("//"):
        return input_string.split("\n", 1)[1]
    return input_string

def parse_numbers(number_string):
    return [int(num) for num in number_string.split(',') if num]

def get_negative_numbers(nums):
    return [num for num in nums if num < 0]

def format_negative_error_message(negatives):
    return "Negative numbers not allowed: " + ", ".join(map(str, negatives))

def check_for_negatives(nums):
    negatives = get_negative_numbers(nums)
    if negatives:
        raise ValueError(format_negative_error_message(negatives))

def sum_valid_numbers(nums):
    return sum(num for num in nums if 0 <= num <= 1000)

def add(numbers):
    if not numbers:
        return 0

    custom_delimiters = extract_custom_delimiters(numbers)
    default_delimiters = get_default_delimiters()
    all_delimiters = combine_delimiters(default_delimiters, custom_delimiters)
    
    number_string = extract_number_string(numbers)
    cleaned_string = replace_delimiters(number_string, all_delimiters)
    nums = parse_numbers(cleaned_string)

    check_for_negatives(nums)
    
    return sum_valid_numbers(nums)
