# Complete the function that takes two numbers as input, num and nth 
# and return the nth digit of num (counting from right to left).

# Note
# If num is negative, ignore its sign and treat it as a positive value
# If nth is not positive, return -1
# Keep in mind that 42 = 00042. This means that findDigit(42, 5) would return 0

def find_digit(num, nth):
    # If nth is not positive, return -1
    if nth =< 0:
        return -1

    # If num is negative, multiply by -1 so we can work with pos num
    if num < 0:
        num = num * -1

    # Turn num into a string. If the nth is longer than the len of string, return 0.
    # Else, turn nth into a negative index and return the int version of the digit found at index
    num_str = str(num)

    if nth > len(num_str):
        return 0
    else:
        neg_index = nth * -1
        str_digit = num_str[neg_index]
        return int(str_digit)