def print_diamond(size):
    """Returns a string that looks like a diamond shape, using asterisk * chars"""

    if size % 2 != 1 or size < 0:
        return None
    
    # Empty list to hold asterisks and newline chars
    diamond_list = []

    # Find middle of diamond
    mid = size // 2     # if size = 3, mid = 1 (1.5 rounded down)

    for i in range(0, size):
        if i <= mid:
            spaces = " " * (mid - i)
            asterisks = (1 + (i * 2)) * "*"  
        else:
            spaces = " " * (i - mid)
            asterisks = (size - ((i - mid) * 2)) * "*" 
        diamond_list.append(spaces)
        diamond_list.append(asterisks)
        diamond_list.append("\n")
    
    return "".join(diamond_list)

print(print_diamond(11))
