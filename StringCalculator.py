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
    
    cleaned_numbers = remove_delimiters(numbers)
    total = 0
    
    for num in cleaned_numbers.split(','):
        if num:
            total += int(num)
    
    return total
