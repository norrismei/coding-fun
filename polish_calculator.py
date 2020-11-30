from data_structures import Stack

def calc(s):
    """Implement a polish notation calculator that takes in string.

    calc("* 2 + 1 2") => 6
    This is same as 2 * (1 + 2)

    """

    if len(s) == 0:
        return "Expression is invalid"
        
    nums = Stack()
    # Reverse the string, then work through equation using stack
    for char in s[::-1]:
        if char.isdigit():
            nums.push(char)
        elif char in "+-*/":
            left = nums.pop()
            right = nums.pop()
            subtotal = eval(left + char + right)
            nums.push(str(subtotal))
    
    total = nums.pop()

    # If expression is valid, there should be nothing left in stack
    if nums.is_empty():
        return total
    else:
        return "Expression is invalid"

print(calc("* 3 3 + 4 5"))

    # ARCHIVING OLDER WORK
    # # Create stack (list of lists) from string
    # # [['*', 2], ['+', '1', '2']]

    # # Stack to hold operations to perform in FILO order
    # operations = []
    # tokens = s.split()
    
    # operation = []

    # for token in tokens:
    #     # If token is an operator
    #     if not token.isdigit():
    #         # If operation is not empty list, need to add operation to stack before moving to next operation
    #         if operation:
    #             operations.append(operation)
    #         operation = []
    #         operation.append(token)
    #     else:
    #         operation.append(float(token))
    
    # # Addressing fence post bug. One last add to stack
    # operations.append(operation)

    # # Keep a running sum that starts at zero
    # running_total = 0

    # # While there are still operations in the stack, pop one off to evaluate and combine with running sum
    # while operations:
    #     curr_operation = operations.pop()
    #     operator = curr_operation[0]
    #     # Each operation will result in a subtotal that gets combined with the running sum
    #     subtotal = 0

    #     for i in range(1, len(curr_operation)):
    #         num = curr_operation[i]
    #         if operator == '+':
    #             subtotal += num
        
    #     running_total += subtotal

    # # When stack is empty, return the running sum
    # return running_total
