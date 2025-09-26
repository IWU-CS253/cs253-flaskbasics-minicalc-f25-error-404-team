def average_length(user_string):
    words = user_string.split()
    if words:  # Ensure the string is not empty
        avg = sum(len(word) for word in words) / len(words)
    else:
        avg = 0
    return avg

def hex(user_string: str):
    bytes = user_string.encode("utf-8")
    hex = bytes.hex()
    return hex