def calc(s):
    """Implement a polish notation calculator that takes in string.
    
    calc("* 2 + 1 2") => 6
    This is same as 2 * (1 + 2)
   
    """

    # Create stack (list of lists) from string
    # [['*', 2], ['+', '1', '2']]

    # Keep a running sum that starts at zero

    # While there are still operations in the stack, pop one off to evaluate and combine with running sum

    # When stack is empty, return the running sum