def average_length(user_string):
    words = user_string.split()
    if words:  # Ensure the string is not empty
        avg = sum(len(word) for word in words) / len(words)
    else:
        avg = 0
    return avg
def char_count(user_string):
    chars = 0
    for c in user_string:
        chars = chars + 1
    return chars
def word_count(user_string):
    words = len(user_string.split(' '))
    return words


