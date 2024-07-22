# StringCalculator.py

def strip_delimiters(text):
    default_delimiters = [",", ";", "\n"]
    for delimiter in default_delimiters:
        text = text.replace(delimiter, '')
    return text

def add_numbers(number_string):
    if not number_string:
        return 0

    cleaned_string = strip_delimiters(number_string)
    total = 0
    negatives = []

    for number in cleaned_string.split():
        if number:
            value = int(number)
            if value < 0:
                negatives.append(value)
            elif value <= 1000:
                total += value

    if negatives:
        raise ValueError(f"Negative numbers not allowed: {', '.join(map(str, negatives))}")

    return total
