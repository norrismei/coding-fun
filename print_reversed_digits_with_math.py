def print_digits(num):
    """Given int, print digits in reverse order, starting with the ones place.

    Solve problem with math, not just converting number to string and reversing it.
    
    >>> print_digits(1)
    1
    >>> print_digits(314)
    4
    1
    3
    >>> print_digits(32)
    2
    3
    >>> print_digits(0)
    0
    """

    if num == 0:
        print(num)
    
    # Start at ones place
    curr_place = 1
    
    # Each loop prints a digit. To exit loop, we subtract from num until it eventually reaches zero
    while num != 0:
        divide_by = curr_place * 10
        # Get remainder by dividing num with the place one higher up
        rem = num % divide_by  
        # The digit to print is the remainder divided by the current place the count is at
        curr_digit = int(rem / curr_place)
        print(curr_digit)
        # Decrease num
        num -= rem  
        # Move to next place left of curr digit by multiplying by 10
        curr_place *= 10
    
    # Hackbright solution:
    # while num:
    #     next_digit = num % 10
    #     print(next_digit)
    #     num = (num - next_digit) // 10



