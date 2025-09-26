# calc.py

import math

def calculate(current_value, num, clear, sqrt):
    if clear:
        return ''  # Clear the current value if clear button is pressed
    elif sqrt:
        if sqrt == 'sqrt':
            try:
                return str(math.sqrt(eval(current_value)))
            except:
                return 'Error'
    elif num:
        if num == '=':
            # Calculate result if '=' is pressed
            try:
                # Safely evaluate the current expression
                return str(eval(current_value))
            except:
                return 'Error'
        else:
            # Append the pressed button value to the current value
            return current_value + num
    return current_value

