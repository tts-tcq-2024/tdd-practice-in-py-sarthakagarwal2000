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
    
    num_list = remove_delimiters(numbers).split(',')
    total = 0
    negatives = []
    
    for num in num_list:
        if num:
            n = int(num)
            if n < 0:
                negatives.append(n)
            elif n <= 1000:
                total += n
    
    if negatives:
        raise Exception(f"negatives not allowed: {', '.join(map(str, negatives))}")
    
    return total
