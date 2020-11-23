def calc(s):
    """Implement a polish notation calculator that takes in string.

    calc("* 2 + 1 2") => 6
    This is same as 2 * (1 + 2)

    """

    # Create stack (list of lists) from string
    # [['*', 2], ['+', '1', '2']]

    operations = s # hard coding for now

    # Keep a running sum that starts at zero
    running_sum = 0

    # While there are still operations in the stack, pop one off to evaluate and combine with running sum
    while operations:
        operation = operations.pop()
        operator = operation[0]
        # Each operation will result in a subtotal that gets combined with the running sum
        subtotal = 0

        for i in range(1, len(operation)):
            if operator == '+':
                num = float(operation[i])
                subtotal += num
        
        running_sum += subtotal

    # When stack is empty, return the running sum
    return running_sum

print(calc([['+', '2', '5']]))