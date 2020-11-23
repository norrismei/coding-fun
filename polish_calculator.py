def calc(s):
    """Implement a polish notation calculator that takes in string.

    calc("* 2 + 1 2") => 6
    This is same as 2 * (1 + 2)

    """

    # Create stack (list of lists) from string
    # [['*', 2], ['+', '1', '2']]

    # Stack to hold operations to perform in FILO order
    operations = []
    tokens = s.split()
    
    operation = []

    for token in tokens:
        # If token is an operator
        if not token.isdigit():
            # If operation is not empty list, need to add operation to stack before moving to next operation
            if operation:
                operations.append(operation)
            operation = []
            operation.append(token)
        else:
            operation.append(float(token))
    
    # Addressing fence post bug. One last add to stack
    operations.append(operation)

    # Keep a running sum that starts at zero
    running_total = 0

    # While there are still operations in the stack, pop one off to evaluate and combine with running sum
    while operations:
        curr_operation = operations.pop()
        operator = curr_operation[0]
        # Each operation will result in a subtotal that gets combined with the running sum
        subtotal = 0

        for i in range(1, len(curr_operation)):
            num = curr_operation[i]
            if operator == '+':
                subtotal += num
        
        running_total += subtotal

    # When stack is empty, return the running sum
    return running_total

print(calc("* 9 + 1 2"))