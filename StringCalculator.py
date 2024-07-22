import re

def extract_delimiters(input_string):
    default_delimiters = [",", ";", "\n"]
    custom_delimiters = []

    if input_string.startswith("//"):
        parts = input_string.split("\n", 1)
        delimiter_part = parts[0][2:]
        custom_delimiters = re.findall(r'\[(.*?)\]', delimiter_part) or [delimiter_part]
        input_string = parts[1]

    delimiters = default_delimiters + custom_delimiters
    return input_string, delimiters

def remove_delimiters(input_string, delimiters):
    for delimiter in delimiters:
        input_string = input_string.replace(delimiter, ',')
    return input_string

def add(numbers):
    if not numbers:
        return 0

    cleaned_string, delimiters = extract_delimiters(numbers)
    cleaned_string = remove_delimiters(cleaned_string, delimiters)

    nums = [int(num) for num in cleaned_string.split(',') if num]
    
    negatives = [num for num in nums if num < 0]
    if negatives:
        raise ValueError(f"Negative numbers not allowed: {', '.join(map(str, negatives))}")

    total = sum(num for num in nums if 0 <= num <= 1000)

    return total
