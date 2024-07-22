delimiters = ["//", ",", ";", "\n"]

def preprocess_input(input_text):
    for delimiter in delimiters:
        input_text = input_text.replace(delimiter, ' ')
    
    tokens = input_text.split()
    return filter_numbers_beyond_limit(tokens)

def filter_numbers_beyond_limit(numbers):
    return [int(num) for num in numbers if 0 <= int(num) <= 1000]

def add(input_text):
    if not input_text:
        return 0
    
    valid_numbers = preprocess_input(input_text)
    return sum(valid_numbers)
