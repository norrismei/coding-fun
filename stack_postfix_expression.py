"""
Given a postfix expression as string, implement a function that will compute the result of the postfix expression.

Ex.
'638*+4-' => 26
6 + 3 * 8 - 4

'921*-8-4+' => 3
For *, pop off 1 and 2, eval and push on stack
For -, pop off 2 and 9
9 - 2 * 1 - 8 + 4

'38+67*-2+' => 3+8-6*7+2

Look at each char to build operation, stopping at operator.

If it's addition or mult, add to a running sum.


"""

from data_structures import Stack

def evaluate_postfix(expr):

    if len(expr) == 0:
        return "Expression is invalid"

    nums = Stack()

    for char in expr:
        if char in "+*-":
            num1 = nums.pop()
            num2 = nums.pop()
            if char == "+":
                subtotal = num1 + num2
            elif char == "*":
                subtotal = num1 * num2
            elif char == "-":
                subtotal = num2 - num1
            nums.push(subtotal)
        else:
            nums.push(int(char))
    
    if len(nums._items) > 1:
        return "Expression is invalid"

    return nums.pop()


print(evaluate_postfix('921*-8-4+'))

# print('5'.isdigit())
# print(eval('5+1'))
# eval(num1 + char + num2)
