# Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

# Examples:
# solution('abc') # should return ['ab', 'c_']
# solution('abcdef') # should return ['ab', 'cd', 'ef']

def solution(s):
    # create list to hold string pairs
    pairs = []

    # if string is even, endpoint is end of string
    if len(s) % 2 == 0:
        endpoint = len(s)
    # else, endpoint is end of string minus one pair
    else:
        endpoint = len(s) - 1

    first_char_index = 0

    # go through loop
    for i in range(0, endpoint//2):
        next_pair_index = first_char_index + 2
        pair = s[first_char_index:next_pair_index]
        # add the two chars to list of strings
        pairs.append(pair)
        # index moves two spaces
        first_char_index = next_pair_index
    # if string is odd
    if endpoint != len(s):
        # make one more pair with last char and underscore
        odd_pair = s[first_char_index] + "_"
        # add to list of strings
        pairs.append(odd_pair)
    
    return pairs

print(solution('abc'))

# best practice solution that uses step
# def solution(s):
#     result = []
#     if len(s) % 2:
#         s += '_'
#     for i in range(0, len(s), 2):
#         result.append(s[i:i+2])
#     return result